# BEAR: A BEnchmark on video Action Recognition

## Introduction
BEAR consists of 18 datasets covering five data domain: daily life, sports, gesture, anomaly actions and instructional actions. Besides, BEAR includes several evaluation paradigms: standard finetuning, few-shot finetuning, zero-shot and domain adaptation. In this work, we provide evaluation results of 6 popular video models on BEAR. We hope BEAR can serve as a fair and challenging evaluation benchmark to gain insights on building next-generation spatiotemporal learners.

The evaluation is **extremely simple** since we provide all scripts in this codebase. The users only need to download datasets and run the scripts provided.


## Datasets Download and Pre-processing
We provide downloading and pre-processing pipeline [here](https://github.com/BEAR-CVPR2023/BEAR/tree/main/datasets) for each dataset.


## Benchmark
Based on pre-trained models on Kinetics400, we provide 4 types of down stream tasks for evaluation: standard finetuning, few-shot finetuning, zero-shot evaluation and domain adaptation.

The pre-trained models can be downloaded [here]().

### Standard Finetuning
We build our stanard finetuning based on a popular video understanding toolbox [MMAction2](https://github.com/open-mmlab/mmaction2).

We provide specific training steps [here](https://github.com/BEAR-CVPR2023/BEAR/tree/main/benchmark/finetuning).

The finetuning results of supervised pre-training are shown below: 

| **Dataset**           | TSN   | TSM   | I3D   | NL    | TimeSformer | VideoSwin |
|------------------|-------|-------|-------|-------|-------------|-----------|
| **XD-Violence** | **85.54** | 82.96 | 79.93 | 79.91 | 82.51 | 82.40 | 75.11 | 80.49 | **81.73** | 80.38 | 80.94 | 77.47 | 77.91 |
| **UCF-Crime**    | 35.42     | **42.36** | 31.94 | 34.03 | 36.11  | 34.72  | 25.69  | **37.50** | 35.42     | 34.03  | 34.72  | 36.11  | 34.03  |
| **MUVIM**        | 79.30     | **100** | 97.80 | 98.68 | 94.71  | **100** | 99.56  | 99.12  | **100**    | 66.96  | 66.96  | 99.12  | **100** |
| **WLASL**        | 29.63     | 43.98 | 49.07 | **52.31** | 37.96  | 45.37  | 44.91  | 27.01  | 27.78     | 29.17  | **30.56** | 25.56  | 28.24  |
| **Jester**       | 86.31     | **95.21** | 92.99 | 93.49 | 93.42  | 94.27  | 92.24  | 83.22  | **95.32**  | 87.23  | 93.89  | 90.33  | 90.18  |
| **UAV-Human**    | 27.89     | **38.84** | 33.49 | 33.03 | 28.93  | 38.66  | 36.07  | 15.70  | 30.75     | 31.95  | 26.28   | 21.02       | 35.12     |
| **CharadesEGO** | 8.26 | 8.11 | 6.13 | 6.42 | **8.58** | 8.55 | 5.69 | 6.29 | 6.59 | 6.24 | 6.31 | 7.59 | **7.65** |
| **Toyota Smarthome** | 74.73 | **82.22** | 79.51 | 76.86 | 69.21 | 79.88 | 79.09 | 68.71 | **81.34** | 77.82 | 76.16 | 61.64 | 80.18 |
| **Mini-HACS** | 84.69 | 80.87 | 77.74 | 79.51 | 79.81 | **84.94** | 60.57 | 64.60 | 63.24 | 70.24 | 60.57 | 73.92 | **75.58** |
| **MPII Cooking** | 38.39 | 46.74 | **48.71** | 42.19 | 40.97 | 46.59 | 42.19 | 34.45 | **50.08** | 42.79 | 40.36 | 35.81 | 47.19 |
| **Mini-Sports1M** | 54.11 | 50.06 | 46.90 | 46.16 | 51.79 | **55.34** | 41.91 | 43.02 | 43.59 | 46.28 | 45.56 | 44.60 | **47.60** |
| **FineGym** | 63.73 | **80.95** | 72.00 | 71.21 | 63.92 | 65.02 | 68.49 | 54.62 | **75.87** | 69.62 | 68.79 | 47.60 | 58.94 |
| **MOD20** | **98.30** | 96.75 | 96.61 | 96.18 | 94.06 | 92.64 | 92.08 | 91.23 | 92.08 | 91.94 | 92.08 | 90.81 | **92.36** |
| **COIN** | 81.15 | 78.49 | 73.79 | 74.30 | **82.99** | 76.27 | 61.29 | 61.48 | 64.53 | 71.57 | **72.78** | 67.64 | 68.78 |
| **MECCANO** | **41.06** | 39.28 | 36.88 | 36.13 | 40.95 | 38.89 | 30.78 | 32.34 | 35.10 | 34.86 | 33.62 | 33.30 | **37.80** |
| **InHARD** | 84.39 | **88.08** | 82.06 | 86.31 | 85.16 | 87.60 | 84.86 | 75.63 | **87.66** | 82.54 | 80.81 | 71.28 | 80.10 |
| **PETRAW** | 94.30 | 95.72 | 94.84 | 94.54 | 94.30 | **96.43** | 95.46 | 93.18 | **95.51** | 95.02 | 94.38 | 85.56 | 91.46 |
| **MISAW** | 61.44 | **75.16** | 68.19 | 64.27 | 71.46 | 69.06 | 69.06 | 59.04 | **73.64** | 70.37 | 64.27 | 60.78 | 68.85 |

The finetuning results of self-supervised pre-training are shown below: 

| **Dataset**           | TSN   | TSM   | I3D   | NL    | TimeSformer | VideoSwin |
|-------------------|-------|-------|-------|-------|-------------|-----------|
| **XD-Violence**  | 80.49 | **81.73** | 80.38 | 80.94 | 77.47 | 77.91 |
| **UCF-Crime**    | **37.50** | 35.42     | 34.03  | 34.72  | 36.11  | 34.03  |
| **MUVIM**        | 99.12  | **100**    | 66.96  | 66.96  | 99.12  | **100** |
| **WLASL**        | 27.01  | 27.78     | 29.17  | **30.56** | 25.56  | 28.24  |
| **Jester**       | 83.22  | **95.32**  | 87.23  | 93.89  | 90.33  | 90.18  |
| **UAV-Human**    | 15.70  | **30.75**     | 31.95  | 26.28   | 21.02       | 35.12     |
| **CharadesEGO** | 6.29 | 6.59 | 6.24 | 6.31 | 7.59 | **7.65** |
| **Toyota Smarthome** | 68.71 | **81.34** | 77.82 | 76.16 | 61.64 | 80.18 |
| **Mini-HACS** | 64.60 | 63.24 | 70.24 | 60.57 | 73.92 | **75.58** |
| **MPII Cooking** | 34.45 | **50.08** | 42.79 | 40.36 | 35.81 | 47.19 |
| **Mini-Sports1M** | 43.02 | 43.59 | 46.28 | 45.56 | 44.60 | **47.60** |
| **FineGym** | 54.62 | **75.87** | 69.62 | 68.79 | 47.60 | 58.94 |
| **MOD20** | 91.23 | 92.08 | 91.94 | 92.08 | 90.81 | **92.36** |
| **COIN** | 61.48 | 64.53 | 71.57 | **72.78** | 67.64 | 68.78 |
| **MECCANO** | 32.34 | 35.10 | 34.86 | 33.62 | 33.30 | **37.80** |
| **InHARD** | 75.63 | **87.66** | 82.54 | 80.81 | 71.28 | 80.10 |
| **PETRAW** | 93.18 | **95.51** | 95.02 | 94.38 | 85.56 | 91.46 |
| **MISAW** | 59.04 | **73.64** | 70.37 | 64.27 | 60.78 | 68.85 |


### Few-shot Finetuning
| epoch | N=1         | N=2         | N=5         | N=10        | N=20        | 100-class acc |
|-------|-------------|-------------|-------------|-------------|-------------|---------------|
| 90    | 52.11/75.32 | 57.34/80.43 | 61.49/85.88 | 64.83/88.49 | 67.17/89.33 | 82.47         |
| 80    | 52.36/75.51 | 56.44/81.00 | 61.77/86.59 | 64.58/89.09 | 66.66/89.87 | 82.68         |
| 70    | 52.92/76.48 | 57.44/81.03 | 62.20/86.78 | 65.08/89.14 | 67.05/89.90 | 82.82         |
| 60    | 51.28/74.77 | 55.68/80.07 | 61.11/86.35 | 63.86/88.76 | 65.95/89.49 | 82.16         |
| 50    | 52.07/74.94 | 55.64/80.20 | 60.77/86.24 | 63.95/88.33 | 65.64/89.23 | 81.28         |
### Zero-shot Evaluation

### Domain Adaptation








