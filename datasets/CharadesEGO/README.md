# Charades-EGO

### [Paper](https://arxiv.org/pdf/1804.09627.pdf) | [Dataset](https://prior.allenai.org/projects/charades-ego)

Charades-Ego is a large-scale dataset with paired first- and third-person videos to facilitate the investigation of the intrinsic correspondence between different views for the same action. In our benchmark, we choose to only carry out the evaluation using its 1st person part, since we do not focus on the correlations between two different views. Based on its official temporal annotations, we manage to segment the original videos into 43,594 short clips.

## Download and preprocessing

- Run the following command for downloading and preprocessing: 
    ```
    bash download_prerpocess_charadesego.sh
    ```

- Note1: There are two kinds of videos in CharagesEGO, one is with name xxxxx.mp4, which are the normal 3rd view videos, and another is with name xxxxxEGO.mp4, which are the 1st view videos. As aforementioned, we only keep the latter in our BEAR. Besides, to know more about the details of the aormat of annotations, please refer to the [official README](annotations/README.txt), which includes all the original annotations, but we only keep 'only1st' version in BEAR.

- Note2: Ensure the folder structure after excute the command is as follows:

  ```
  ./CharadesEGO/
  |
  |───videos/
  │    └───D3TR8EGO_c1563.90_12.00.mp4
  │    └───D3TR8EGO_c0618.20_12.50.mp4
  │    └───...
  └───annotations/
  │    └───Charades_v1_classes.txt
  │    └───CharadesEgo_v1_test_only1st.csv
  │    └───CharadesEgo_v1_train_only1st.csv
  ```