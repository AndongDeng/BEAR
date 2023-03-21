# Jester

### [Paper](https://openaccess.thecvf.com/content_ICCVW_2019/papers/HANDS/Materzynska_The_Jester_Dataset_A_Large-Scale_Video_Dataset_of_Human_Gestures_ICCVW_2019_paper.pdf) | [Dataset](https://developer.qualcomm.com/software/ai-datasets/jester)


Jester is collected from 1,376 actors based on 27 gesture classes. The categories contained in Jester include gestures that usually appear in interactions between humans and some smart devices, such as “Zoom in with two fingers”.

## Download and preprocessing

### 1. Download videos

- The dataset is officially released [here](https://developer.qualcomm.com/software/ai-datasets/jester).

- Put all the files under:  `./data/jester/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_jester.sh
    ```