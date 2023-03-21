# InHARD

### [Paper](https://www.researchgate.net/profile/Mejdi-Dallel/publication/344252122_InHARD_-_Industrial_Human_Action_Recognition_Dataset_in_the_Context_of_Industrial_Collaborative_Robotics/links/5f60cdb692851c078967e929/InHARD-Industrial-Human-Action-Recognition-Dataset-in-the-Context-of-Industrial-Collaborative-Robotics.pdf) | [Dataset](https://lineact.cesi.fr/inhard-industrial-human-action-recognition-dataset/) | [Github](https://github.com/vhavard/InHARD)


InHARD [8], Industrial Human Action Recognition Dataset,is collected in a human-robot collaboration scenario. 16 distinct subjects are invited to finish an assembly task with the guidance of a robotic arm. The classes contain the specific actions during this operation, such as ’put down measuring rod’ and ’put down component’.

## Download and preprocessing

### 1. Download videos

- The dataset is officially released [here](https://zenodo.org/record/4003541#.ZBkotuzMJhE).

- Put all the files under:  `./data/inhard/videos`

### 2. Preprocessing

- Run the following command: 
    ```
    bash prerpocess_inhard.sh
    ```