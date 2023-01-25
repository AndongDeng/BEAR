import torch
import torch.nn as nn
from mmcv.cnn import ConvModule, kaiming_init
from mmcv.runner import _load_checkpoint, load_checkpoint
from mmcv.utils import print_log
from timm.models.layers import trunc_normal_

from ...utils import get_root_logger
from ..builder import BACKBONES
from .convnext3d import ConvNeXt3D, Block3d, LayerNorm


class ConvNeXt3DSlow(ConvNeXt3D):
    def __init__(self, name):
        super().__init__(name)

        self.downsample_layers = nn.ModuleList() # stem and 3 intermediate downsampling conv layers
        stem = nn.Sequential(
            nn.Conv3d(3, self.dims[0], kernel_size=(3, 4, 4), stride=(1, 4, 4), padding=(1, 0, 0)),
            LayerNorm(self.dims[0], eps=1e-6, data_format="channels_first")
        )
        self.downsample_layers.append(stem)
        for i in range(3):
            downsample_layer = nn.Sequential(
                    LayerNorm(self.dims[i] + self.dims[i] // 4, eps=1e-6, data_format="channels_first"),
                    nn.Conv3d(self.dims[i] + self.dims[i] // 4, self.dims[i+1], kernel_size=(3, 2, 2), stride=(1, 2, 2), padding=(1, 0, 0)),
            )
            self.downsample_layers.append(downsample_layer)

        self.stages = nn.ModuleList() # 4 feature resolution stages, each consisting of multiple residual blocks
        dp_rates=[x.item() for x in torch.linspace(0, 0., sum(self.depths))] 
        cur = 0
        for i in range(4):
            stage = nn.Sequential(
                *[Block3d(dim=self.dims[i], drop_path=dp_rates[cur + j], 
                layer_scale_init_value=1e-6) for j in range(self.depths[i])]
            )
            self.stages.append(stage)
            cur += self.depths[i]

        self.norm = nn.LayerNorm(self.dims[-1], eps=1e-6) # final norm layer


class ConvNeXt3DFast(ConvNeXt3D):
    def __init__(self, name, channel_ratio):
        super().__init__(name)
        self.dims = [i // channel_ratio for i in self.dims]

        self.downsample_layers = nn.ModuleList() # stem and 3 intermediate downsampling conv layers
        stem = nn.Sequential(
            nn.Conv3d(3, self.dims[0], kernel_size=(3, 4, 4), stride=(1, 4, 4), padding=(1, 0, 0)),
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
        dp_rates=[x.item() for x in torch.linspace(0, 0., sum(self.depths))] 
        cur = 0
        for i in range(4):
            stage = nn.Sequential(
                *[Block3d(dim=self.dims[i], drop_path=dp_rates[cur + j], 
                layer_scale_init_value=1e-6) for j in range(self.depths[i])]
            )
            self.stages.append(stage)
            cur += self.depths[i]

        self.norm = nn.LayerNorm(self.dims[-1], eps=1e-6) # final norm layer


@BACKBONES.register_module()
class ConvNeXt3dSlowFast(nn.Module):

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
                 resample_rate=8,
                 speed_ratio=8,
                 channel_ratio=8,
                 fusion_kernel=5):
        super().__init__()

        self.depths, self.dims = self.arch_settings[name]
        self.pretrained = pretrained
        self.resample_rate = resample_rate
        self.speed_ratio = speed_ratio
        self.channel_ratio = channel_ratio

        self.slow_pathway = ConvNeXt3DSlow(name, channel_ratio)
        self.fast_pathway = ConvNeXt3DFast(name, channel_ratio)

        self.lateral_connections = nn.ModuleList()
        for i in range(3):
            lateral_conv = nn.Conv3d(self.dims[i] // channel_ratio,
                                          self.dims[i] * 2 // self.channel_ratio,
                                          kernel_size=(fusion_kernel, 1, 1),
                                          stride=(speed_ratio, 1, 1),
                                          padding=((fusion_kernel - 1) // 2, 0, 0),
                                          bias=False)
            self.lateral_connections.append(lateral_conv)
        

    def init_weights(self):
        """Initiate the slow pathway parameters either from existing checkpoint or from
        scratch."""

        # random init fast pathway anyway
        for m in self.modules():
            if isinstance(m, (nn.Conv3d, nn.Linear)):
                trunc_normal_(m.weight, std=.02)
                try:
                    nn.init.constant_(m.bias, 0)
                except AttributeError:
                    pass

        if isinstance(self.pretrained, str):
            logger = get_root_logger()
            logger = get_root_logger()
            logger.info(f'load model from: {self.pretrained} to initialize slow pathway')

            load_checkpoint(self, self.pretrained, strict=False, logger=logger)
                    
        elif self.pretrained is None:
            for m in self.slow_pathway.modules():
                if isinstance(m, (nn.Conv3d, nn.Linear)):
                    trunc_normal_(m.weight, std=.02)
                    nn.init.constant_(m.bias, 0)
        else:
            raise TypeError('pretrained must be a str or None')
    


    def forward(self, x):
        x_slow = nn.functional.interpolate(
            x,
            mode='nearest',
            scale_factor=(1.0 / self.resample_rate, 1.0, 1.0))

        x_fast = nn.functional.interpolate(
            x,
            mode='nearest',
            scale_factor=(1.0 / (self.resample_rate // self.speed_ratio), 1.0,
                          1.0))
        
        for i in range(3):

            x_slow = self.slow_pathway.downsample_layers[i](x_slow)
            x_fast = self.fast_pathway.downsample_layers[i](x_fast)

            x_slow = self.slow_pathway.stages[i](x_slow)
            x_fast = self.fast_pathway.stages[i](x_fast)

            x_fast_lateral = self.lateral_connections[i](x_fast)
            x_slow = torch.cat((x_slow, x_fast_lateral), dim=1)

        x_slow = self.slow_pathway.downsample_layers[3](x_slow)
        x_fast = self.fast_pathway.downsample_layers[3](x_fast)

        x_slow = self.slow_pathway.stages[3](x_slow)
        x_fast = self.fast_pathway.stages[3](x_fast)

        x_slow = x_slow.permute(0, 2, 3, 4, 1)
        x_slow = self.slow_pathway.norm(x_slow)
        x_slow = x_slow.permute(0, 4, 1, 2, 3)

        x_fast = x_fast.permute(0, 2, 3, 4, 1)
        x_fast = self.fast_pathway.norm(x_fast)
        x_fast = x_fast.permute(0, 4, 1, 2, 3)

        out = (x_slow, x_fast)
        return out
