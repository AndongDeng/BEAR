# Charades-EGO

### [Paper](https://arxiv.org/pdf/1804.09627.pdf) | [Dataset](https://prior.allenai.org/projects/charades-ego)

Charades-Ego is a large-scale dataset with paired first- and third-person videos to facilitate the investigation of the intrinsic correspondence between different views for the same action. In our benchmark, we choose to only carry out the evaluation using its 1st person part, since we do not focus on the correlations between two different views. Based on its official temporal annotations, we manage to segment the original videos into 43,594 short clips.

## Download and preprocessing

### 1. Download videos

- The videos are officially provided in Dropbox with the following link:

    [Data(scaled to 480p, 11GB)](https://ai2-public-datasets.s3-us-west-2.amazonaws.com/charades/CharadesEgo_v1_480.tar)<br>
    [Annotations](https://ai2-public-datasets.s3-us-west-2.amazonaws.com/charades/CharadesEgo.zip)


- Put all the zip files under:  `./data/CharadesEGO/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_charadesego.sh
    ```
