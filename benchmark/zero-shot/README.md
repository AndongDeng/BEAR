# BEAR-ZeroShot

Direct finetuning on annotated datasets is a commonly adopted paradigm for action recognition, but the recent success of vision-language models, which leverage the rich correspondence between natural language and visual content, has provided a new learning paradigm for vision tasks in a zero-shot setting, which is severely required in applications without labeled data. Therefore, we also provide the zero-shot evaluation on BEAR using the recent CLIP-based models. 


## Installation
This part is borrowed from the official [CLIP repo](https://github.com/openai/CLIP), and you can fine more details there.
```
conda install --yes -c pytorch pytorch=1.7.1 torchvision cudatoolkit=11.0
pip install ftfy regex tqdm
pip install git+https://github.com/openai/CLIP.git
```

## Evaluation

If you want to evaluate with single frame, run:
```
python single_frame.py --dataset ${DATASET}
```

If you want to evaluate with multiple frames, run:
```
python multiple_frame.py --dataset ${DATASET} --num_clip ${NUM_CLIP}
```

If you want to evaluate with ActionCLIP, which takes as input 8 frames as default, run:
```
python action_clip.py --dataset ${DATASET}
```
