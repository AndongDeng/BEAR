#########################################################################
     ________                         __                ______          
    / ____/ /_  ____ __________ _____/ /__  _____      / ____/___ _____ 
   / /   / __ \/ __ `/ ___/ __ `/ __  / _ \/ ___/_____/ __/ / __ `/ __ \
  / /___/ / / / /_/ / /  / /_/ / /_/ /  __(__  )_____/ /___/ /_/ / /_/ /
  \____/_/ /_/\__,_/_/   \__,_/\__,_/\___/____/     /_____/\__, /\____/ 
                                                          /____/        
#########################################################################

Charades-Ego Dataset - Version 1.0
https://github.com/gsig/actor-observer
allenai.org/plato/charades/
Initial Release, April 2018

Gunnar A. Sigurdsson
Abhinav Gupta
Cordelia Schmid
Ali Farhadi
Karteek Alahari

If this work helps your research, please cite:
@inproceedings{actorobserver,
author = {Gunnar A. Sigurdsson and Abhinav Gupta and Cordelia Schmid and Ali Farhadi and Karteek Alahari},
title={Actor and Observer: Joint Modeling of First and Third-Person Videos},
booktitle={CVPR},
year={2018},
}

Relevant files:
README.txt (this file)
license.txt (the license file, this must be included)
CharadesEgo_v1.tar:
  CharadesEgo_v1_train.csv (the training annotations)
  CharadesEgo_v1_test.csv (the validation annotations)
  Charades_v1_classes.txt (the classes)
  Charades_v1_objectclasses.txt (the primary object classes)
  Charades_v1_verbclasses.txt (the primary verb classes)
  Charades_v1_mapping.txt (mapping from activity to object and verb)
  Charades_v1_classify.m (evaluation code for video-level classification)
  Charades_v1_localize.m (evaluation code for temporal action detection)
CharadesEgo_v1.tar (the videos)
CharadesEgo_v1_480.tar (the videos in 480p)
Charades_caption.zip (contains evaluation code for caption generation)
CharadesEgo_v1_rgb.tar (the videos stored as jpg frames at 24 fps)
Please refer to the website to download any missing files.


###########################################################
Charades_v1.tar
###########################################################
The zipfile contains videos for training and validation sets encoded in H.264/MPEG-4 AVC (mp4) using ffmpeg:
ffmpeg -i input.ext -vcodec libx264 -crf 23 -c:a aac -strict -2 -pix_fmt yuv420p output.mp4
The videos, originally in various formats, maintain their original resolutions and framerates.


###########################################################
Charades_v1_classes.txt 
###########################################################
Contains each class label (starting at c000) followed by a human-readable description of the action, such as "c008 Opening a door"


###########################################################
CharadesEgo_v1_train.csv and CharadesEgo_v1_test.csv
###########################################################
A comma-seperated csv, where a field may be enclosed by double quotation marks (") in case it contains a comma. If a field has multiple values, such as multiple actions, those are seperated by semicolon (;). The file contains the following fields:

- id:
Unique identifier for each video. This id contains 'EGO' at the end for first person videos. That is, if a third-person video has the id ABCDE then the corresponding egocentric video is ABCDEEGO
- subject:
Unique identifier for each subject in the dataset
- scene:
One of 15 indoor scenes in the dataset, such as Kitchen
- quality:
The quality of the video judged by an annotator (7-point scale, 7=high quality)
- relevance: 
The relevance of the video to the script judged by an annotated (7-point scale, 7=very relevant)
- verified:
'Yes' if an annotator successfully verified that the video matches the script, else 'No'
- script:
The human-generated script used to generate the video
- descriptions:
Semicolon-separated list of descriptions by annotators watching the video
- actions:  
Semicolon-separated list of "class start end" triplets for each actions in the video, such as c092 11.90 21.20;c147 0.00 12.60
- length:
The length of the video in seconds
- egocentric:
'Yes' if the video is in first-person, else 'No'
- charades_video:
Identifier of the video in the Charades training set that has the same script to this video.


This can be loaded into MATLAB as follows:

f = fopen('CharadesEgo_v1_train.csv');
header = textscan(f,repmat('%s ',[1 12]),1,'Delimiter',',');
csv = textscan(f,repmat('%q ',[1 12]),'Delimiter',',');
actions = csv{9};
actions_in_first_video = regexp(actions{1},';','split');


This can be loaded into python as:

import csv
with open('CharadesEgo_v1_train.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        actions = row['actions'].split(';')

Please refer to the evaluation code for usage examples.


###########################################################
Charades_v1_classify.m
###########################################################
Evaluation code for video-level classification. Each video has zero or more actions. This script takes in a "submission file" which is a csv file of the form:

id vector

where 'id' is a video id for a given video, and 'vector' is a whitespace delimited list of 157 floating point numbers representing the scores for each action in a video. An example submission file is provided in test_submission_classify.txt

The evaluation script calculates the mean average precision (mAP) for the videos. That is, the average of the average precision (AP) for a single activity in all the videos.


###########################################################
Charades_v1_localize.m
###########################################################
Evaluation code for frame-level classification (localization). Each frame in a video has zero or more actions. This script takes in a "submission file" which is a csv file of the form:

id framenumber vector

where 'id' is a video id for a given video, 'framenumber' is the number of frame described below, and 'vector' is a whitespace delimited list of 157 floating point numbers representing the scores of each action in a frame. An example submission file is provided in test_submission_localize.txt (download this file with get_test_submission_localize.sh).

To avoid extremely large submission files, the evaluation script evaluates mAP on 25 equally spaced frames throughout each video. The frames are chosen as follows

for j=1:frames_per_video
    timepoint(j) = (j-1)*time/frames_per_video;

That is: 0, time/25, 2*time/25, ..., 24*time/25.

The baseline performance was generated by calculating the action scores at 75 equally spaced frames in the video (our batchsize) and picking every third prediction.

For more information about localization, please refer to the following publication:
@article{sigurdsson2016asynchronous,
author = {Gunnar A. Sigurdsson and Santosh Divvala and Ali Farhadi and Abhinav Gupta},
title = {Asynchronous Temporal Fields for Action Recognition},
journal={arXiv preprint arXiv:1612.06371},
year={2016},
pdf = {http://arxiv.org/pdf/1612.06371.pdf},
code = {https://github.com/gsig/temporal-fields},
}


###########################################################
CharadesEgo_v1_rgb.tar
###########################################################
These frames were extracted at 24fps using the following ffmpeg call for each video in the dataset:

line=pathToVideo
MAXW=320
MAXH=320
filename=$(basename $line)
ffmpeg -i "$line" -qscale:v 3 -filter:v "scale='if(gt(a,$MAXW/$MAXH),$MAXW,-1)':'if(gt(a,$MAXW/$MAXH),-1,$MAXH)',fps=fps=24" "/somepath/${filename%.*}/${filename%.*}_%0d.jpg";

The files are stored as CharadesEgo_v1_rgb/id/id-000000.jpg where id is the video id and 000000 is the number of the frame at 24fps.


###########################################################
Baseline algorithms on Charades 
###########################################################
Code for multiple activity recognition algorithms are provided at:
https://github.com/gsig/charades-algorithms
https://github.com/gsig/actor-observer


###########################################################
CHANGELOG
###########################################################

4/1/18
Initial release

###########################################################
