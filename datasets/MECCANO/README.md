# MECCANO

### [Paper](https://openaccess.thecvf.com/content/WACV2021/papers/Ragusa_The_MECCANO_Dataset_Understanding_Human-Object_Interactions_From_Egocentric_Videos_in_WACV_2021_paper.pdf) | [Dataset](https://iplab.dmi.unict.it/MECCANO/) | [github](https://github.com/fpv-iplab/MECCANO)


MECCANO is related to an assembly operation but collected with wearable cameras. The target task is to build a toy motorbike given all the components and the booklet, and the whole assembly process is precisely divided into 61 action step.

## Download and preprocessing

- Run the following command for downloading and preprocessing: 
    ```
    bash download_prerpocess_meccano.sh
    ```

- Note3: If you want to keep the original videos, just remove the last line in `download_preprocess_meccano.sh`:
    ```
    rm -rf raw_meccano_videos/
    ```