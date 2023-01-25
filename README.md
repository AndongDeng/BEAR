# BEAR: A BEnchmark on video Action Recognition

## Introduction
BEAR consists of 18 datasets covering five data domain: daily life, sports, gesture, anomaly actions and instructional actions. Besides, BEAR includes several evaluation paradigms: standard finetuning, few-shot finetuning, zero-shot and domain adaptation. In this work, we provide evaluation results of 6 popular video models on BEAR. We hope BEAR can serve as a fair and challenging evaluation benchmark to gain insights on building next-generation spatiotemporal learners.

The evaluation is extremely simple since we provide all scripts in this codebase. The users only need to download datasets and run the scripts provided.


## Datasets Download and Pre-processing
We provide downloading and pre-processing pipeline [here](https://github.com/BEAR-CVPR2023/BEAR/tree/main/datasets) for each dataset.


## Benchmark
Based on pre-trained models on Kinetics400, we provide 4 types of down stream tasks for evaluation: standard finetuning, few-shot finetuning, zero-shot evaluation and domain adaptation.

The pre-trained models can be downloaded [here]().

### Standard Finetuning
We build our stanard finetuning based on a popular video understanding toolbox [MMAction2](https://github.com/open-mmlab/mmaction2).

We provide specific training steps [here](https://github.com/BEAR-CVPR2023/BEAR/tree/main/benchmark/finetuning).

### Few-shot Finetuning

### Zero-shot Evaluation

### Domain Adaptation








