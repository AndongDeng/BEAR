# COIN

### [Paper](https://arxiv.org/pdf/1804.09627.pdf) | [Dataset](https://coin-dataset.github.io/) | [Github](https://github.com/coin-dataset/annotations)

COIN dataset is a large-scale dataset built for comprehensive instructional video analysis based on videos collected from YouTube. It consists of 180 tasks in 12 different domains related to tasks about daily living.

## Download and preprocessing

- Run the following command for downloading and preprocessing: 
    ```
    bash download_prerpocess_coin.sh
    ```

- Note: If you want to keep the original videos, just remove the last line in `download_preprocess_charadesego.sh`:
    ```
    rm -rf raw_coin_videos/
    ```