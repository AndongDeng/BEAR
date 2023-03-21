# UCF-Crime

### [Paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Sultani_Real-World_Anomaly_Detection_CVPR_2018_paper.pdf) | [Dataset](https://www.crcv.ucf.edu/projects/real-world/) | [Github](https://github.com/WaqasSultani/AnomalyDetectionCVPR2018)

UCF-Crime is a challenging anomaly video dataset collected from surveillance cameras. We select 12 human-related crime categories from its original 14-class recognition version as we only focus on human actions.

## Download and preprocessing

### 1. Download videos

- The videos are officially provided in Dropbox with the following link:

    [Dropbox](https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABvnJSwZI7zXb8_myBA0CLHa?dl=0)

    **Note**: Each zip file can be unzip separately. (*TODO*)


- Put all the zip files under:  `./data/UCF-Crime/videos`


### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_ucf_crime.sh
    ```

