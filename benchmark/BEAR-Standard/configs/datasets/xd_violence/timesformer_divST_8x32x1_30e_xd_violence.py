checkpoint_config = dict(interval=1)
log_config = dict(interval=100, hooks=[dict(type='TextLoggerHook')])
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
model = dict(
    type='Recognizer3D',
    backbone=dict(
        type='TimeSformer',
        num_frames=8,
        img_size=224,
        patch_size=16,
        embed_dims=768,
        in_channels=3,
        dropout_ratio=0.0,
        transformer_layers=None,
        attention_type='divided_space_time',
        norm_cfg=dict(type='LN', eps=1e-06)),
    cls_head=dict(type='TimeSformerHead', num_classes=5, in_channels=768),
    train_cfg=None,
    test_cfg=dict(average_clips='prob'))
dataset_type = 'RawframeDataset'
data_root = 'data/xd_violence/frames/'
data_root_val = 'data/xd_violence/frames/'
ann_file_train = 'data/xd_violence/annotations/train.csv'
ann_file_val = 'data/xd_violence/annotations/test.csv'
ann_file_test = 'data/xd_violence/annotations/test.csv'
img_norm_cfg = dict(
    mean=[127.5, 127.5, 127.5], std=[127.5, 127.5, 127.5], to_bgr=False)
train_pipeline = [
    dict(type='SampleFrames', clip_len=8, frame_interval=16, num_clips=1),
    dict(type='RawFrameDecode'),
    dict(type='RandomRescale', scale_range=(256, 320)),
    dict(type='RandomCrop', size=224),
    dict(type='Flip', flip_ratio=0.5),
    dict(
        type='Normalize',
        mean=[127.5, 127.5, 127.5],
        std=[127.5, 127.5, 127.5],
        to_bgr=False),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['imgs', 'label'])
]
val_pipeline = [
    dict(
        type='SampleFrames',
        clip_len=8,
        frame_interval=16,
        num_clips=1,
        test_mode=True),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(
        type='Normalize',
        mean=[127.5, 127.5, 127.5],
        std=[127.5, 127.5, 127.5],
        to_bgr=False),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['imgs', 'label'])
]
test_pipeline = [
    dict(
        type='SampleFrames',
        clip_len=8,
        frame_interval=16,
        num_clips=1,
        test_mode=True),
    dict(type='RawFrameDecode'),
    dict(type='Resize', scale=(-1, 224)),
    dict(type='ThreeCrop', crop_size=224),
    dict(
        type='Normalize',
        mean=[127.5, 127.5, 127.5],
        std=[127.5, 127.5, 127.5],
        to_bgr=False),
    dict(type='FormatShape', input_format='NCTHW'),
    dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['imgs', 'label'])
]
data = dict(
    videos_per_gpu=8,
    workers_per_gpu=4,
    test_dataloader=dict(videos_per_gpu=1),
    train=dict(
        type='RawframeDataset',
        ann_file='data/xd_violence/annotations/train.csv',
        data_prefix='data/xd_violence/frames/',
        filename_tmpl='img_{:05d}.jpg',
        start_index=0,
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=8,
                frame_interval=16,
                num_clips=1),
            dict(type='RawFrameDecode'),
            dict(type='RandomRescale', scale_range=(256, 320)),
            dict(type='RandomCrop', size=224),
            dict(type='Flip', flip_ratio=0.5),
            dict(
                type='Normalize',
                mean=[127.5, 127.5, 127.5],
                std=[127.5, 127.5, 127.5],
                to_bgr=False),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
            dict(type='ToTensor', keys=['imgs', 'label'])
        ]),
    val=dict(
        type='RawframeDataset',
        ann_file='data/xd_violence/annotations/test.csv',
        filename_tmpl='img_{:05d}.jpg',
        start_index=0,
        data_prefix='data/xd_violence/frames/',
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=8,
                frame_interval=16,
                num_clips=1,
                test_mode=True),
            dict(type='RawFrameDecode'),
            dict(type='Resize', scale=(-1, 256)),
            dict(type='CenterCrop', crop_size=224),
            dict(
                type='Normalize',
                mean=[127.5, 127.5, 127.5],
                std=[127.5, 127.5, 127.5],
                to_bgr=False),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
            dict(type='ToTensor', keys=['imgs', 'label'])
        ]),
    test=dict(
        type='RawframeDataset',
        ann_file='data/xd_violence/annotations/test.csv',
        filename_tmpl='img_{:05d}.jpg',
        start_index=0,
        data_prefix='data/xd_violence/frames/',
        pipeline=[
            dict(
                type='SampleFrames',
                clip_len=8,
                frame_interval=16,
                num_clips=1,
                test_mode=True),
            dict(type='RawFrameDecode'),
            dict(type='Resize', scale=(-1, 224)),
            dict(type='ThreeCrop', crop_size=224),
            dict(
                type='Normalize',
                mean=[127.5, 127.5, 127.5],
                std=[127.5, 127.5, 127.5],
                to_bgr=False),
            dict(type='FormatShape', input_format='NCTHW'),
            dict(type='Collect', keys=['imgs', 'label'], meta_keys=[]),
            dict(type='ToTensor', keys=['imgs', 'label'])
        ]))
evaluation = dict(
    interval=3, metrics=['top_k_accuracy', 'mean_class_accuracy'])
optimizer = dict(
    type='SGD',
    lr=0.005,
    momentum=0.9,
    paramwise_cfg=dict(
        custom_keys=dict({
            '.backbone.cls_token': dict(decay_mult=0.0),
            '.backbone.pos_embed': dict(decay_mult=0.0),
            '.backbone.time_embed': dict(decay_mult=0.0)
        })),
    weight_decay=0.0001,
    nesterov=True)
optimizer_config = dict(grad_clip=dict(max_norm=40, norm_type=2))
lr_config = dict(policy='step', step=[10, 20])
total_epochs = 30
work_dir = './work_dirs/timesformer/xd_violence_8frame'
gpu_ids = range(0, 4)
omnisource = False
module_hooks = []
