# MECCANO

### [Paper](https://openaccess.thecvf.com/content/WACV2021/papers/Ragusa_The_MECCANO_Dataset_Understanding_Human-Object_Interactions_From_Egocentric_Videos_in_WACV_2021_paper.pdf) | [Dataset](https://iplab.dmi.unict.it/MECCANO/) | [github](https://github.com/fpv-iplab/MECCANO)


MECCANO is related to an assembly operation but collected with wearable cameras. The target task is to build a toy motorbike given all the components and the booklet, and the whole assembly process is precisely divided into 61 action step.

## Download and preprocessing

### 1. Download videos

- The dataset is officially released:

    [RGB Videos](https://iplab.dmi.unict.it/sharing/MECCANO/MECCANO_RGB_Videos.zip)<br>
    [Action Temporal Annotations](https://iplab.dmi.unict.it/sharing/MECCANO/MECCANO_action_annotations.zip)

- Put all the files under:  `./data/meccano/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_meccano.sh
    ```