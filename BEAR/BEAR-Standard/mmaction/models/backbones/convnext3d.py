# Copyright (c) Meta Platforms, Inc. and affiliates.

# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import torch
import torch.nn as nn
import torch.nn.functional as F
from timm.models.layers import trunc_normal_, DropPath
from mmcv.runner import _load_checkpoint, load_checkpoint
from mmcv.cnn import NonLocal3d

from ...utils import get_root_logger
from ..builder import BACKBONES


class Block3d(nn.Module):
    """ ConvNeXt Block 3d block for ConvNeXt3D. 
    
    There are two equivalent implementations:
    (1) DwConv -> LayerNorm (channels_first) -> 1x1 Conv -> GELU -> 1x1 Conv; all in (N, C, H, W)
    (2) DwConv -> Permute to (N, H, W, C); LayerNorm (channels_last) -> Linear -> GELU -> Linear; Permute back
    We use (2) as we find it slightly faster in PyTorch
    
    Args:
        dim (int): Number of input channels.
        drop_path (float): Stochastic depth rate. Default: 0.0
        layer_scale_init_value (float): Init value for Layer Scale. Default: 1e-6.
    """
    def __init__(self, 
                 dim, 
                 drop_path=0., 
                 layer_scale_init_value=1e-6,
                 non_local_block=None):
        super().__init__()
        self.dwconv = nn.Conv3d(dim, dim, kernel_size=(3, 7, 7), padding=(1, 3, 3), groups=dim) # depthwise conv
        self.norm = LayerNorm(dim, eps=1e-6)
        self.pwconv1 = nn.Linear(dim, 4 * dim) # pointwise/1x1 convs, implemented with linear layers
        self.act = nn.GELU()
        self.pwconv2 = nn.Linear(4 * dim, dim)
        self.gamma = nn.Parameter(layer_scale_init_value * torch.ones((dim)), 
                                    requires_grad=True) if layer_scale_init_value > 0 else None
        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()

        self.non_local_block = non_local_block

    def forward(self, x):
        input = x
        x = self.dwconv(x)
        x = x.permute(0, 2, 3, 4, 1) # (N, C, T, H, W) -> (N, T, H, W, C)
        x = self.norm(x)
        x = self.pwconv1(x)
        x = self.act(x)
        x = self.pwconv2(x)
        if self.gamma is not None:
            x = self.gamma * x
        x = x.permute(0, 4, 1, 2, 3) # (N, H, W, C) -> (N, C, H, W)
        x = input + self.drop_path(x)

        if self.non_local_block:
            x = self.non_local_block(x)
        return x


@BACKBONES.register_module()
class ConvNeXt3D(nn.Module):
    r""" ConvNeXt3D
        A PyTorch 3D version impl for ConvNeXt : `A ConvNet for the 2020s`  -
          https://arxiv.org/pdf/2201.03545.pdf
    Args:
        in_chans (int): Number of input image channels. Default: 3
        num_classes (int): Number of classes for classification head. Default: 1000
        depths (tuple(int)): Number of blocks at each stage. Default: [3, 3, 9, 3]
        dims (int): Feature dimension at each stage. Default: [96, 192, 384, 768]
        drop_path_rate (float): Stochastic depth rate. Default: 0.
        layer_scale_init_value (float): Init value for Layer Scale. Default: 1e-6.
        head_init_scale (float): Init scaling value for classifier weights and biases. Default: 1.
    """

    arch_settings = {
        'tiny': ([3, 3, 9, 3], [96, 192, 384, 768]),
        'small': ([3, 3, 27, 3], [96, 192, 384, 768]),
        'base': ([3, 3, 27, 3], [128, 256, 512, 1024]),
        'large': ([3, 3, 27, 3], [192, 384, 768, 1536]),
        'xlarge': ([3, 3, 27, 3], [256, 512, 1024, 2048])
    }

    def __init__(self,
                 name,
                 pretrained=None,
                 in_channels=3, 
                 drop_path_rate=0., 
                 frozen_stages=-1,
                 layer_scale_init_value=1e-6, 
                 ):
        super().__init__()

        if name not in self.arch_settings:
            raise KeyError(f'invalid name {name} for resnext')
        self.depths, self.dims = self.arch_settings[name]
        self.in_channels = in_channels
        self.pretrained = pretrained
        self.frozen_stages = frozen_stages
        self.drop_path_rate = drop_path_rate
        self.layer_scale_init_value = layer_scale_init_value
        self.downsample_layers = nn.ModuleList() # stem and 3 intermediate downsampling conv layers
        stem = nn.Sequential(
            nn.Conv3d(in_channels, self.dims[0], kernel_size=(3, 4, 4), stride=(1, 4, 4), padding=(1, 0, 0)),
            LayerNorm(self.dims[0], eps=1e-6, data_format="channels_first")
        )
        self.downsample_layers.append(stem)
        for i in range(3):
            downsample_layer = nn.Sequential(
                    LayerNorm(self.dims[i], eps=1e-6, data_format="channels_first"),
                    nn.Conv3d(self.dims[i], self.dims[i+1], kernel_size=(3, 2, 2), stride=(1, 2, 2), padding=(1, 0, 0)),
            )
            self.downsample_layers.append(downsample_layer)

        self.stages = nn.ModuleList() # 4 feature resolution stages, each consisting of multiple residual blocks
        dp_rates=[x.item() for x in torch.linspace(0, self.drop_path_rate, sum(self.depths))] 
        cur = 0
        for i in range(4):
            stage = nn.Sequential(
                *[Block3d(dim=self.dims[i], drop_path=dp_rates[cur + j], 
                layer_scale_init_value=self.layer_scale_init_value) for j in range(self.depths[i])]
            )
            self.stages.append(stage)
            cur += self.depths[i]

        self.norm = nn.LayerNorm(self.dims[-1], eps=1e-6) # final norm layer
        self._freeze_stages()
    
    def init_weights(self):
        """Initiate the parameters either from existing checkpoint or from
        scratch."""
        if isinstance(self.pretrained, str):
            logger = get_root_logger()
            logger = get_root_logger()
            logger.info(f'load model from: {self.pretrained}')

            load_checkpoint(self, self.pretrained, strict=False, logger=logger)
                    
        elif self.pretrained is None:
            for m in self.modules():
                if isinstance(m, (nn.Conv2d, nn.Linear)):
                    trunc_normal_(m.weight, std=.02)
                    nn.init.constant_(m.bias, 0)
        else:
            raise TypeError('pretrained must be a str or None')

    def _freeze_stages(self):
        """Prevent all the parameters from being optimized before
        ``self.frozen_stages``."""
        if self.frozen_stages >= 1:
            for i in range(0, self.frozen_stages):
                m1 = self.downsample_layers[i]
                m1.eval()
                for param in m1.parameters():
                    param.requires_grad = False

                m2 = self.stages[i]
                m2.eval()
                for param in m2.parameters():
                    param.requires_grad = False

    def forward_features(self, x):
        for i in range(4):
            x = self.downsample_layers[i](x)
            x = self.stages[i](x)
        return x 

    def forward(self, x):
        x = self.forward_features(x)
        x = x.permute(0, 2, 3, 4, 1)
        x = self.norm(x)
        x = x.permute(0, 4, 1, 2, 3)
        return x

    def train(self, mode=True):
        """Convert the model into training mode while keep layers freezed."""
        super(ConvNeXt3D, self).train(mode)
        self._freeze_stages()


class LayerNorm(nn.Module):
    r""" LayerNorm that supports two data formats: channels_last (default) or channels_first. 
    The ordering of the dimensions in the inputs. channels_last corresponds to inputs with 
    shape (batch_size, height, width, channels) while channels_first corresponds to inputs 
    with shape (batch_size, channels, height, width).
    """
    def __init__(self, normalized_shape, eps=1e-6, data_format="channels_last"):
        super().__init__()
        self.weight = nn.Parameter(torch.ones(normalized_shape))
        self.bias = nn.Parameter(torch.zeros(normalized_shape))
        self.eps = eps
        self.data_format = data_format
        if self.data_format not in ["channels_last", "channels_first"]:
            raise NotImplementedError 
        self.normalized_shape = (normalized_shape, )
    
    def forward(self, x):
        if self.data_format == "channels_last":
            return F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)
        elif self.data_format == "channels_first":
            u = x.mean(1, keepdim=True)
            s = (x - u).pow(2).mean(1, keepdim=True)
            x = (x - u) / torch.sqrt(s + self.eps)
            x = self.weight[:, None, None, None] * x + self.bias[:, None, None, None]
            return x