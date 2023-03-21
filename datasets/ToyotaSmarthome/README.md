# Toyota Smarthome

### [Paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Das_Toyota_Smarthome_Real-World_Activities_of_Daily_Living_ICCV_2019_paper.pdf) | [Dataset](https://project.inria.fr/toyotasmarthome/) 

Toyota Smarthome is a 3rd view dataset containing videos from different cameras deployed in an apartment, whose subjects are 18 senior people. The videos are collected from 7 cameras in the dining room, kitchen, and living room. We use the cross-subject train-test split in our evaluation, i.e., the training data are from 11 subjects and the rest are utilized for testing.

## Download and preprocessing

### 1. Download videos

- The dataset is released but you have to first sign the form at the bottm of its project page [here](https://project.inria.fr/toyotasmarthome/).


- Put all the files under:  `./data/ToyotaSmarthome/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_toyota_smarthome.sh
    ```