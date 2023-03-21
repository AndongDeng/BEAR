# WLASL

### [Paper](https://arxiv.org/pdf/1910.11006.pdf) | [Dataset](https://dxli94.github.io/WLASL/)  | [Github](https://github.com/dxli94/WLASL)

WLASL, short for World-Level American Sign Language, is built for sign language understanding, which could make progress for the communications of the blind and deaf. Its original version contains 2000 categories of common sign language; in our benchmark, we use its subset WLASL100 for our evaluation.

## Download and preprocessing

### 1. Download videos

- The dataset can be downloaded via the following command:
    ```
    python download_wlasl.py
    ```

- Put all the files under:  `./data/wlasl/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_wlasl.sh
    ```
