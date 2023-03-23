# Copyright (c) Meta Platforms, Inc. and affiliates.

# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.


import torch
import torch.nn as nn
import torch.nn.functional as F

from mmcv.cnn import NonLocal3d
from torch.nn.modules.utils import _ntuple

from ...utils import get_root_logger
from ..builder import BACKBONES
from .convnext3d import ConvNeXt3D, Block3d


@BACKBONES.register_module()
class ConvNeXt3DNonLocal(ConvNeXt3D):

    def __init__(self, 
                 name,
                 pretrained=None,
                 non_local=((0, 0, 0), 
                            (1, 0, 0), 
                            (1, 0, 0, 0, 0, 0, 0,
                             1, 0, 0, 0, 0, 0, 0,
                             1, 0, 0, 0, 0, 0, 0,
                             1, 0, 0, 0, 0, 0), 
                            (0, 0, 0)),
                 non_local_cfg=dict()):
        super().__init__(name, pretrained)

        self.non_local = non_local
        self.non_local_cfg = non_local_cfg

        self.non_local_stages = _ntuple(4)(non_local)
        
        self.stages = nn.ModuleList() # 4 feature resolution stages, each consisting of multiple residual blocks
        dp_rates=[x.item() for x in torch.linspace(0, self.drop_path_rate, sum(self.depths))] 
        cur = 0

        for i in range(4):
            non_local_stage = self.non_local_stages[i]

            stage_list = []            
            for j, non_local_ind in enumerate(non_local_stage):
                if non_local_ind:
                    non_local_block = NonLocal3d(self.dims[i], **self.non_local_cfg)
                else:
                    non_local_block = None
                sub_stage = Block3d(dim=self.dims[i], drop_path=dp_rates[cur + j], 
                    layer_scale_init_value=self.layer_scale_init_value, non_local_block=non_local_block)
                stage_list.append(sub_stage)

            stage = nn.Sequential(*stage_list)
            self.stages.append(stage)
            cur += self.depths[i]

    
    def forward_features(self, x):
        for i in range(4):
            x = self.downsample_layers[i](x)
            x = self.stages[i](x)
        return x