import os
import sys
import csv

import cv2

mode = sys.argv[1]
assert mode == 'train' or mode == 'test'

data_root = './videos/'
frame_root = './frames/{}/'.format(mode)

split_file = open('raw_annotations/gym99_{}_element_v1.0.txt'.format(mode), 'r')

class_file = open('raw_annotations/gym99_categories.txt', 'r')
class_csv = open('labels.csv', 'w')
class_writer = csv.writer(class_csv)
class_content = class_file.readlines()
class_dict = dict()
for i, line in enumerate(class_content):
    category_name = line[40: ].split('\n')[0].rstrip()
    class_writer.writerow([category_name])
    class_dict[i] = category_name

print(class_dict)

csv_file = open('fine_gym_{}.csv'.format(mode), 'w')

split_content = split_file.readlines()
csv_writer = csv.writer(csv_file)

for line in split_content:
    video_name = line.split(' ')[0]
    class_id = int(line.split(' ')[1].split('\n')[0])

    video_path = os.path.join(data_root, video_name + '.mp4')
    if os.path.exists(video_path):
        csv_writer.writerow([video_name + ';' + class_dict[class_id]])
        # cap = cv2.VideoCapture(video_path)

        # frame_index = 0
        # while True:
        #     ret, frame = cap.read()

        #     if not ret:
        #         break

        #     frame_path = os.path.join(frame_root, video_name)
        #     if not os.path.exists(frame_path):
        #         os.mkdir(frame_path)
            
        #     cv2.imwrite(os.path.join(frame_path, str(frame_index).zfill(4) + '.jpg'), frame)
        #     frame_index += 1
        # print('saved {} frames at {}!'.format(len(os.listdir(frame_path)), frame_path))