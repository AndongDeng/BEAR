# model settings
model = dict(
    type='Recognizer3D',
    backbone=dict(
        type='ConvNeXt3dSlowFast',
        name='base',
        pretrained=None,
        resample_rate=4,  # tau
        speed_ratio=4,  # alpha
        channel_ratio=8), # beta_inv
    cls_head=dict(
        type='SlowFastHead',
        in_channels=1152,  # 1204 + 128
        num_classes=400,
        spatial_type='avg',
        dropout_ratio=0.5),
    # model training and testing settings
    train_cfg=None,
    test_cfg=dict(average_clips='prob'))