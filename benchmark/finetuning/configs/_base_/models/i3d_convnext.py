# model settings
model = dict(
    type='Recognizer3D',
    backbone=dict(
        type='ConvNeXt3D',
        name='base'),
    cls_head=dict(
        type='I3DHead',
        num_classes=400,
        in_channels=1024,
        spatial_type='avg',
        dropout_ratio=0.5,
        init_std=0.01),
    # model training and testing settings
    train_cfg=None,
    test_cfg=dict(average_clips='prob'))

# This setting refers to https://github.com/open-mmlab/mmaction/blob/master/mmaction/models/tenons/backbones/resnet_i3d.py#L329-L332  # noqa: E501
