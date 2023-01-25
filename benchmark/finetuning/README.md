# Video Swin Transformer

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/video-swin-transformer/action-classification-on-kinetics-400)](https://paperswithcode.com/sota/action-classification-on-kinetics-400?p=video-swin-transformer)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/video-swin-transformer/action-classification-on-kinetics-600)](https://paperswithcode.com/sota/action-classification-on-kinetics-600?p=video-swin-transformer)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/video-swin-transformer/action-recognition-in-videos-on-something)](https://paperswithcode.com/sota/action-recognition-in-videos-on-something?p=video-swin-transformer)

By [Ze Liu](https://github.com/zeliu98/)\*, [Jia Ning](https://github.com/hust-nj)\*, [Yue Cao](http://yue-cao.me),  [Yixuan Wei](https://github.com/weiyx16), [Zheng Zhang](https://stupidzz.github.io/), [Stephen Lin](https://scholar.google.com/citations?user=c3PYmxUAAAAJ&hl=en) and [Han Hu](https://ancientmooner.github.io/).

This repo is the official implementation of ["Video Swin Transformer"](https://arxiv.org/abs/2106.13230). It is based on [mmaction2](https://github.com/open-mmlab/mmaction2).

## Updates

***06/25/2021*** Initial commits

## Introduction

**Video Swin Transformer** is initially described in ["Video Swin Transformer"](https://arxiv.org/abs/2106.13230), which advocates an inductive bias of locality in video Transformers, leading to a better speed-accuracy trade-off compared to previous approaches which compute self-attention globally even with spatial-temporal factorization. The locality of the proposed video architecture is realized by adapting the Swin Transformer designed for the image domain, while continuing to leverage the power of pre-trained image models. Our approach achieves state-of-the-art accuracy on a broad range of video recognition benchmarks, including action recognition (`84.9` top-1 accuracy on Kinetics-400 and `86.1` top-1 accuracy on Kinetics-600 with `~20x` less pre-training data and `~3x` smaller model size) and temporal modeling (`69.6` top-1 accuracy on Something-Something v2).


![teaser](figures/teaser.png)

## Results and Models

### Kinetics 400

| Backbone |  Pretrain   | Lr Schd | spatial crop | acc@1 | acc@5 | #params | FLOPs | config | model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  Swin-T  | ImageNet-1K |  30ep   |     224      |  78.8  |  93.6  |   28M   |  87.9G  |  [config](configs/recognition/swin/swin_tiny_patch244_window877_kinetics400_1k.py)  | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_tiny_patch244_window877_kinetics400_1k.pth)/[baidu](https://pan.baidu.com/s/1mIqRzk8RILeRsP2KB5T6fg) |
|  Swin-S  | ImageNet-1K |  30ep   |     224      |  80.6  |  94.5  |   50M   |  165.9G  |  [config](configs/recognition/swin/swin_small_patch244_window877_kinetics400_1k.py)   | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_small_patch244_window877_kinetics400_1k.pth)/[baidu](https://pan.baidu.com/s/1imq7LFNtSu3VkcRjd04D4Q) |
|  Swin-B  | ImageNet-1K |  30ep   |     224      |  80.6  |  94.6  |   88M   |  281.6G  |  [config](configs/recognition/swin/swin_base_patch244_window877_kinetics400_1k.py)   | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_base_patch244_window877_kinetics400_1k.pth)/[baidu](https://pan.baidu.com/s/1bD2lxGxqIV7xECr1n2slng) |
|  Swin-B  | ImageNet-22K |  30ep   |     224      |  82.7  |  95.5  |   88M   |  281.6G  |  [config](configs/recognition/swin/swin_base_patch244_window877_kinetics400_22k.py)   | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_base_patch244_window877_kinetics400_22k.pth)/[baidu](https://pan.baidu.com/s/1CcCNzJAIud4niNPcREbDbQ) |

### Kinetics 600

| Backbone |  Pretrain   | Lr Schd | spatial crop | acc@1 | acc@5 | #params | FLOPs | config | model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  Swin-B  | ImageNet-22K |  30ep   |     224      |  84.0  |  96.5  |   88M   |  281.6G  |  [config](configs/recognition/swin/swin_base_patch244_window877_kinetics600_22k.py)   | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_base_patch244_window877_kinetics600_22k.pth)/[baidu](https://pan.baidu.com/s/1ZMeW6ylELTje-o3MiaZ-MQ) |

### Something-Something V2

| Backbone |  Pretrain   | Lr Schd | spatial crop | acc@1 | acc@5 | #params | FLOPs | config | model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  Swin-B  | Kinetics 400 |  60ep  |     224      |  69.6  |  92.7  |   89M   |  320.6G  |  [config](configs/recognition/swin/swin_base_patch244_window1677_sthv2.py)   | [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_base_patch244_window1677_sthv2.pth)/[baidu](https://pan.baidu.com/s/18MOGf6L3LeUjrLoQEeA52Q) |

**Notes**:

- **Pre-trained image models can be downloaded from [Swin Transformer for ImageNet Classification](https://github.com/microsoft/Swin-Transformer)**.
- The pre-trained model of SSv2 could be downloaded at [github](https://github.com/SwinTransformer/storage/releases/download/v1.0.4/swin_base_patch244_window1677_kinetics400_22k.pth)/[baidu](https://pan.baidu.com/s/1ZnJuX7-x2BflDKHpuvdLUg).
- Access code for baidu is `swin`.

## Usage

###  Installation

Please refer to [install.md](docs/install.md) for installation.

We also provide docker file [cuda10.1](docker/docker_10.1) ([image url](https://hub.docker.com/layers/ninja0/mmdet/pytorch1.7.1-py37-cuda10.1-openmpi-mmcv1.3.3-apex-timm/images/sha256-06d745934cb255e7fdf4fa55c47b192c81107414dfb3d0bc87481ace50faf90b?context=repo)) and [cuda11.0](docker/docker_11.0) ([image url](https://hub.docker.com/layers/ninja0/mmdet/pytorch1.7.1-py37-cuda11.0-openmpi-mmcv1.3.3-apex-timm/images/sha256-79ec3ec5796ca154a66d85c50af5fa870fcbc48357c35ee8b612519512f92828?context=repo)) for convenient usage.

###  Data Preparation

Please refer to [data_preparation.md](docs/data_preparation.md) for a general knowledge of data preparation.
The supported datasets are listed in [supported_datasets.md](docs/supported_datasets.md).

We also share our Kinetics-400 annotation file [k400_val](https://github.com/SwinTransformer/storage/releases/download/v1.0.6/k400_val.txt), [k400_train](https://github.com/SwinTransformer/storage/releases/download/v1.0.6/k400_train.txt) for better comparison.

### Inference
```
# single-gpu testing
python tools/test.py <CONFIG_FILE> <CHECKPOINT_FILE> --eval top_k_accuracy

# multi-gpu testing
bash tools/dist_test.sh <CONFIG_FILE> <CHECKPOINT_FILE> <GPU_NUM> --eval top_k_accuracy
```

### Training

To train a video recognition model with pre-trained image models (for Kinetics-400 and Kineticc-600 datasets), run:
```
# single-gpu training
python tools/train.py <CONFIG_FILE> --cfg-options model.backbone.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]

# multi-gpu training
bash tools/dist_train.sh <CONFIG_FILE> <GPU_NUM> --cfg-options model.backbone.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]
```
For example, to train a `Swin-T` model for Kinetics-400 dataset  with  8 gpus, run:
```
bash tools/dist_train.sh configs/recognition/swin/swin_tiny_patch244_window877_kinetics400_1k.py 8 --cfg-options model.backbone.pretrained=<PRETRAIN_MODEL> 
```

To train a video recognizer with pre-trained video models (for Something-Something v2 datasets), run:
```
# single-gpu training
python tools/train.py <CONFIG_FILE> --cfg-options load_from=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]

# multi-gpu training
bash tools/dist_train.sh <CONFIG_FILE> <GPU_NUM> --cfg-options load_from=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]
```
For example, to train a `Swin-B` model for SSv2 dataset with 8 gpus, run:
```
bash tools/dist_train.sh configs/recognition/swin/swin_base_patch244_window1677_sthv2.py 8 --cfg-options load_from=<PRETRAIN_MODEL>
```

**Note:** `use_checkpoint` is used to save GPU memory. Please refer to [this page](https://pytorch.org/docs/stable/checkpoint.html) for more details.


### Apex (optional):
We use apex for mixed precision training by default. To install apex, use our provided docker or run:
```
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
```
If you would like to disable apex, comment out the following code block in the [configuration files](configs/recognition/swin):
```
# do not use mmcv version fp16
fp16 = None
optimizer_config = dict(
    type="DistOptimizerHook",
    update_interval=1,
    grad_clip=None,
    coalesce=True,
    bucket_size_mb=-1,
    use_fp16=True,
)
```

## Citation
If you find our work useful in your research, please cite:

```
@article{liu2021video,
  title={Video Swin Transformer},
  author={Liu, Ze and Ning, Jia and Cao, Yue and Wei, Yixuan and Zhang, Zheng and Lin, Stephen and Hu, Han},
  journal={arXiv preprint arXiv:2106.13230},
  year={2021}
}

@article{liu2021Swin,
  title={Swin Transformer: Hierarchical Vision Transformer using Shifted Windows},
  author={Liu, Ze and Lin, Yutong and Cao, Yue and Hu, Han and Wei, Yixuan and Zhang, Zheng and Lin, Stephen and Guo, Baining},
  journal={arXiv preprint arXiv:2103.14030},
  year={2021}
}
```

## Other Links

> **Image Classification**: See [Swin Transformer for Image Classification](https://github.com/microsoft/Swin-Transformer).

> **Object Detection**: See [Swin Transformer for Object Detection](https://github.com/SwinTransformer/Swin-Transformer-Object-Detection).

> **Semantic Segmentation**: See [Swin Transformer for Semantic Segmentation](https://github.com/SwinTransformer/Swin-Transformer-Semantic-Segmentation).

> **Self-Supervised Learning**: See [MoBY with Swin Transformer](https://github.com/SwinTransformer/Transformer-SSL).
