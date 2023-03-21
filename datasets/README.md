# Datasets Download and Pre-processing in BEAR

- The general folder structure for BEAR datasets should be as follows:
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
  ```

## Anomaly Action Datasets
We include XD-Violence, UCF-Crime and MUVIM as the three anomaly video datasets in BEAR.

### XD-Violence
1. Download: 

    The raw videos of XD-Violence can be downloaded [here](https://roc-ng.github.io/XD-Violence/), and put it at `./XD-Violence/`

2. Pre-processing: 
    
    We first decode the origin videos into frames as follows:

    `python ./XD-Violence/decode_train_data.py`

    In BEAR, we only consider single-label action recognition. Thus, we first need to segment each video in XD-Violence according to the temporal annotations provided as follows:

    `python ./XD-Violence/seg_test_data.py`

3. MMAction2-format annotation files generation: Then, generate annoatation files as follows:
    
    `python ./XD-Violence/gen_annotation_csv.py`


### UCF-Crime

### MUVIM

## Daily Action Datasets

## Sports Action Datasets

## Gesture Action Datasets

## Instructional Action Datasets
