# XD-Violence

### [Paper](https://roc-ng.github.io/XD-Violence/images/paper.pdf) | [Dataset](https://roc-ng.github.io/XD-Violence/) | [Github](https://github.com/Roc-Ng/XDVioDet)


XD-violence is a video anomaly dataset that includes data from various sources such as action movies, sports videos, and CCTV cameras. This results in a more extensive collection of video samples, enriching our anomaly datasets track. Specifically, the **original XD-violence has a multi-label text set** with temporal annotation, according to which we segment the test videos into **single-label clips**.


## Download and preprocessing

### 1. Download videos

- The videos are officially provided in OneDrive with the following link:

    [Training Videos_0001-1004](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/ERiQQLUAex1CnwuBIEOK9YgBtcqU3hR_ZDtahCwLtVVkew?e=QHJ3bz)<br>
    [Training Videos_1005-2004](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/EU-CqR-yYmVEqlFR1qHs3ZwB_Xfmi9d2augzSoOgDM66ug?e=gNNLIR)<br>
    [Training Videos_2005-2804](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/EVcHk8zeeQJGhoDrsj1I-RsBXwGgOwrr_qU_8Yvx1KVnEw?e=84ftkC)<br>
    [Training Videos_2805-3319](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/EV9x2SOsTWNFjAAukYmTVIEBKTFz2rc_lkJ4N-8Y7AbIvA?e=fOZU2d)<br>
    [Training Videos_3320-3954](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/ERGkxZqFDJlGs4GM1CvhOY4B5ASIKQIS4elt3VWZqjR65g?e=jdbmcO)<br>
    [Test Videos](https://stuxidianeducn-my.sharepoint.com/:u:/g/personal/pengwu_stu_xidian_edu_cn/EdewYQSko-BHpew03RBfGLQBIAOUdF7jt1rC71rK5iBGag?e=v4Enay)<br>


- Put all the zip files under:  `./data/XD-Violence/videos`


### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_xd_violence.sh
    ```








