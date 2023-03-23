# Mini-HACS

### [Paper](https://arxiv.org/pdf/1712.09374.pdf) | [Dataset](http://hacs.csail.mit.edu/) | [github](https://github.com/hangzhaomit/HACS-dataset)


HACS, human action clips and segments, is a large-scale dataset for both action recognition and temporal action localization. We only leverage HACS clips for our action recognition studies; likewise, considering its scale, we randomly sample 50 videos per class to form mini-HACS, 40 for training and 10 for testing.

## Download and preprocessing

- Run the following command for downloading and preprocessing: 

    ```
    bash download_prerpocess_mini_hacs.sh
    ```