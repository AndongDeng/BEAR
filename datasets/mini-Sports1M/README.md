# Mini-Sports1M

### [Paper](https://cs.stanford.edu/people/karpathy/deepvideo/deepvideo_cvpr2014.pdf) | [Dataset](https://cs.stanford.edu/people/karpathy/deepvideo/) | [github](https://github.com/gtoderici/sports-1m-dataset/)


Sports1M is one of the biggest sports video datasets in the vision community, which contains 487 categories and has been well-annotated. Considering the fact that some of its URLs are no longer available as well as its huge amount (the original version contains over 1 million videos), we construct a mini version of it, which only includes 50 samples per class, 40 for training, and 10 for testing.

## Download and preprocessing

### 1. Download videos

- The videos can be download via the following command:

    ```
    python download_mini_sports1m.py
    ```

- Put all the videos under:  `./data/mini_sports1m/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_mini_sports1m.sh
    ```