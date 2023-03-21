
# FineGym

### [Project Page](https://sdolivia.github.io/FineGym/) | [Videos](https://www.youtube.com/playlist?list=PL2wRKCL5yrJRBnIxWhmVr3xLJahdK5DGJ) | [Paper](https://arxiv.org/abs/2004.06704)

FineGym is a recently released fine-grained dataset, which considers sub-actions within a sports event. In BEAR, we use one of its versions – FineGym99, including 99 fine-grained gymnastic actions from top-level world competitions.

## Download and preprocessing

### 1. Download videos

- The split and annotations are officially provided:

	[Gym99 train split](https://sdolivia.github.io/FineGym/resources/dataset/gym99_train_element_v1.1.txt)<br>
	[Gym99 val split](https://sdolivia.github.io/FineGym/resources/dataset/gym99_val_element.txt)<br>
	[Temporal annotation (json)](https://sdolivia.github.io/FineGym/resources/dataset/finegym_annotation_info_v1.1.json)

- You can simply run the following script to download the videos from YouTube:
```
    python download.py
```

- Put all the files under:  `./data/FineGym/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_finegym.sh
    ```
