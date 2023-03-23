import os
import csv

train_csv = open('annotations/train.csv', 'w')
train_writer = csv.writer(train_csv)


frame_root = 'frames/'
video_listdir = os.listdir(frame_root)
for video_name in video_listdir:
    if video_name.startswith('Fall'):
        train_writer.writerow([video_name + ';' + 'fall'])
        pass
    elif video_name.startswith('NonFall'):
        train_writer.writerow([video_name + ';' + 'nonfall'])
        pass
