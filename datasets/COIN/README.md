# COIN

### [Paper](https://arxiv.org/pdf/1804.09627.pdf) | [Dataset](https://coin-dataset.github.io/) | [Github](https://github.com/coin-dataset/annotations)

COIN dataset is a large-scale dataset built for comprehensive instructional video analysis based on videos collected from YouTube. It consists of 180 tasks in 12 different domains related to tasks about daily living.

## Download and preprocessing

### 1. Download videos

- You can simply run the officially provided download script to download COIN from YouTube:
```
    python download_videos.py
```

- Put all the files under:  `./data/COIN/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_coin.sh
    ```
