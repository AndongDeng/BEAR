# Standard Finetuning in BEAR

The config file for each model in each dataset can be found in `./configs/datasets/{dataset_name}/`.

Example:
To finetuning a VideoSwin in UCF-Crime in a distributed manner in 4 GPUs, simply run:
    
`bash tools/dist_train.sh configs/datasets/ucf_crime/swin_base_patch244_window877_8x16_ucf_crime.py 8 --validate --cfg-options load_from=checkpoints/videoswin_ssl.pth data.videos_per_gpu=4 work_dir=ssl_workdir/videoswin/ucf_crime/ data_root=data/ucf_crime/frames/ data_root_val=data/ucf_crime/frames/ data.train.ann_file=data/ucf_crime/annotations/train.csv data.val.ann_file=data/ucf_crime/annotations/test.csv data.train.data_prefix=data/ucf_crime/frames/ data.val.data_prefix=data/ucf_crime/frames/ data.test.data_prefix=data/ucf_crime/frames/ `

