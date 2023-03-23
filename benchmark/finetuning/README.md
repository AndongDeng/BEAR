# BEAR-Standard

## Installation

1. Create conda env
    ```
    conda create -n bear python=3.8
    ```

2. Install PyTorch>=1.7
    ```
    conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch
    ```

3. Install mmcv-full
    ```
    pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
    ```

4. Install MMAction2
    ```
    pip install -v -e . --user
    ```

## Training
The config file for each model in each dataset can be found in `./configs/datasets/{dataset_name}/`.

    Example:
    To finetuning a VideoSwin in UCF-Crime in a distributed manner in 4 GPUs, simply run:
    
    ```
    bash tools/dist_train.sh configs/datasets/ucf_crime/swin_base_patch244_window877_8x16_ucf_crime.py 8 
    --validate \ 
    --cfg-options load_from=checkpoints/videoswin_ssl.pth data.videos_per_gpu=4 \ 
                work_dir=ssl_workdir/videoswin/ucf_crime/ data_root=data/ucf_crime/ \ 
                data_root_val=data/ucf_crime/ \ 
                data.train.ann_file=data/ucf_crime/annotations/train.csv  \
                data.val.ann_file=data/ucf_crime/annotations/test.csv  \
                data.train.data_prefix=data/ucf_crime/ \ 
                data.val.data_prefix=data/ucf_crime/ \ 
                data.test.data_prefix=data/ucf_crime/ \ 
    ```

