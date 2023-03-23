# MISAW

### [Paper](https://arxiv.org/pdf/2103.13111v1.pdf) | [Dataset](https://www.synapse.org/#!Synapse:syn21776936/wiki/601700) 

To cover scenarios as much as possible, we add two medical instructional datasets MISAW [28] (Micro-Surgical Anastomose Workflow) and PETRAW [27] (PEg TRAnsfer Workflow). Both two datasets are collected in simulated environments. The whole process is constructed by step-wise professional clinical operations, such as ’suturing’ and ’knot tying’. Both two datasets provide frame-wise annotation in terms of phase, step, and action labels for the left hand and right hand and MISAW additionally provides the target and tool annotations. To generate segment-level action annotation, for MISAW, we view the action label of the left hand and the corresponding target as a whole, when any of them changes, we change the segment annotation. For instance, if the annotation of the action and the target for the current frame are ’Hold’ and ’Left artificial vessel’, we annotate the segment where it belongs as ’Hold Left artificial vessel’; if the annotation changes in the next frame into ’Catch’ and ’Needle’, we start a new segment and annotate it as ’Catch Needle’ until the next change. Similarly, we segment PETRAW videos based on the change of the left-hand action.

## Download and preprocessing

### 1. Download videos

- The dataset is released [here](https://www.synapse.org/#!Synapse:syn21776936/files/).

- Put all the files under:  `./data/misaw/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    python decode.py
    ```