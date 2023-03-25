# <img src="../figs/bear.png" width="25"/>BEAR Datasets 

## Introduction
Despite new datasets being introduced every year, the most widely adopted benchmarks in the video action recognition community are Kinetics-400/600/700, Something-something-v1/v2, UCF-101 and HMDB-51. 
However, these datasets share a high similarity in that they are mostly composed of daily and sports actions. Models that achieve good performance on these datasets may not generalize well to the challenging real-world scenarios due to dramatic domain shifts. 
For example, anomaly videos are often captured from surveillance cameras, which look quite different from daily videos due to viewpoint change. Ideally, a video model is expected to cope with diverse real-world applications.
To comprehensively evaluate the generalization capability of video models, we present <img src="../figs/bear.png" width="14"/>**BEAR**, a new **BE**nchmark for human **A**ction **R**ecognition, which is carefully designed towards *practical use*, *data diversity*, and *task diversity*.

## Data domain

The 18 datasets cover 5 data domains: 

- Daily videos
  - [Charades-EGO](CharadesEGO/)
  - [Toyota Smarthome](ToyotaSmarthome/)
  - [Mini-HACS](mini-HACS/)
  - [MPII-Cooking](MPII-Cooking/)
- Sports videos
  - [Mini-Sports1M](mini-Sports1M/)
  - [FineGym99](FineGym/)
  - [MOD20](MOD20/)
- Gesture videos
  - [WLASL100](WLASL/)
  - [Jester](Jester/)
  - [UAV Human](UAV-Human/)
- Anomaly videos
  - [XD-Violence](XD-Violence/)
  - [UCF Crime](UCF-Crime/)
  - [MUVIM](MUVIM/)
- Instructional videos
  - [COIN](COIN/)
  - [MECCANO](MECCANO/)
  - [InHARD](InHARD/)
  - [MISAW](MISAW/)
  - [PETRAW](PETRAW/)

## Download and Preprocessing

We provide download and pre-processing approaches for all 18 datasets here. It should be noted that for [UAV-Human](UAV-Human/README.md), [ToyotaSmarthome](ToyotaSmarthome/README.md) and [MUVIM](MUVIM/README.md), there are no direct downloading scripts, since the data access must be requested from the owners of the datasets and there shall be no redistribution of these datasets. Besides, MISAW, PETRAW require sign-in for Synapse and XD-Violence and MOD20 provide Onedrive and Google drive link, respectively.


- You can doanload and preprocess the rest 11 datasets via one command:

  ```
  bash download_preprocess_most.sh
  ```


- The general folder structure for <img src="../figs/bear.png" width="14"/>**BEAR** datasets should be as follows:
  ```
  ./data/
  |
  |───dataset1/
  │    └───videos/
  │    └───annotations/
  └───dataset2
  │    └───videos/
  │    └───annotations/
  └───dataset3/
  │    └───videos/
  │    └───annotations/
  └───...
  ```

- You can refer to [MMAction2 Data Preparation](https://github.com/open-mmlab/mmaction2/blob/master/docs/en/data_preparation.md) for more details.