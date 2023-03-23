
# FineGym

### [Project Page](https://sdolivia.github.io/FineGym/) | [Videos](https://www.youtube.com/playlist?list=PL2wRKCL5yrJRBnIxWhmVr3xLJahdK5DGJ) | [Paper](https://arxiv.org/abs/2004.06704)

FineGym is a recently released fine-grained dataset, which considers sub-actions within a sports event. In BEAR, we use one of its versions – FineGym99, including 99 fine-grained gymnastic actions from top-level world competitions.

## Download and preprocessing

- Run the following command for downloading and preprocessing: 
    ```
    bash download_prerpocess_finegym.sh
    ```

- Note: If you want to keep the raw videos, just remove the last line in `download_preprocess_finegym.sh`:
    ```
    rm -rf raw_finegym_videos/
    ```