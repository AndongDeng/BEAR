import os
import csv

import cv2


data_root = 'videos/'
train_frame_root = 'frames/train/'
test_frame_root = 'frames/test/'

train_csv = open('annotations/hacs_train.csv', 'w')
test_csv = open('annotations/hacs_test.csv', 'w')
label_csv = open('annotations/labels.csv', 'w')

train_writer = csv.writer(train_csv)
test_writer = csv.writer(test_csv)
label_writer = csv.writer(label_csv)

label_dict = dict()
label_set = set()

file_clips = './HACS_v1.1.1/HACS_clips_v1.1.1.csv'
with open(file_clips, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        classname, vid, subset, start, end, label = row
        vid = 'v_' + vid
        label_dict[vid] = dict()
        label_dict[vid]['start'] = float(start)
        label_dict[vid]['end'] = float(end)
        label_dict[vid]['label'] = classname

failure = []

class_listdir = os.listdir(data_root)
for class_name in class_listdir:
    class_path = os.path.join(data_root, class_name)
    label_set.add(class_name)

    video_listdir = os.listdir(class_path)
    for i, video_name_mp4 in enumerate(video_listdir):
        video_path = os.path.join(class_path, video_name_mp4)
        video_name = video_name_mp4.split('.mp4')[0]

        if i <= 39:
            frame_save_path = os.path.join(train_frame_root, video_name)
            train_writer.writerow([video_name + ';' + class_name])
        elif i >= 40:
            frame_save_path = os.path.join(test_frame_root, video_name)
            test_writer.writerow([video_name + ';' + class_name])
        # if not os.path.exists(frame_save_path):
        #     os.mkdir(frame_save_path)

        # cap = cv2.VideoCapture(video_path)
        # FPS = cap.get(5)

        # start, end = label_dict[video_name].values()
        # start_index, end_index = int(start * FPS), int(end * FPS)

        # frame_index = 0
        # while True:
        #     ret, frame = cap.read()
        #     if not ret:
        #         failure.append(video_name)
        #     break

        #     if frame_index >= start_index and frame_index <= end_index:
        #         cv2.imwrite(os.path.join(frame_save_path, str(frame_index).zfill(3) + '.jpg'), frame)
        #     frame_index += 1
        #     if frame_index > end_index:
        #         break
        # print('saved {} frames at {}!'.format(len(os.listdir(frame_save_path)), frame_save_path))

# print(len(failure))
# print(failure)
for cn in label_set:
    label_writer.writerow([cn])