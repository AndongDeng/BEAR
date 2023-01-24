import os
import csv


csv_file = open('ucf_crime_train.csv', 'w')
csv_writer = csv.writer(csv_file)

txt_file = open('Action_Recognition_splits/train_001.txt', 'r')
for i, line in enumerate(txt_file.readlines()):
    class_name, video_name = line.split('/')
    frame_name = video_name.split('.mp4')[0]
    csv_writer.writerow([frame_name + ';' + class_name])
    print(i)
