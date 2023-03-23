import os
import json
import csv
# from moviepy.editor import VideoFileClip

import cv2


video_root = 'videos/'
train_frame_root = 'frames/train/'
test_frame_root = 'frames/test/'

train_csv = open('annotations/coin_train.csv', 'w')
test_csv = open('annotations/coin_test.csv', 'w')

train_writer = csv.writer(train_csv)
test_writer = csv.writer(test_csv)

if not os.path.exists(train_frame_root):
    os.mkdir(train_frame_root)
if not os.path.exists(test_frame_root):
    os.mkdir(test_frame_root)

data_info = json.load(open('annotations/COIN.json', 'r'))['database']
for url in data_info.keys():

        video_info = data_info[url]

        recipe_type = video_info['recipe_type']  # class_id
        start = float(video_info['start'])
        end = float(video_info['end'])
        class_name = video_info['class']
        split = video_info['subset']

        video_path = os.path.join(video_root, str(recipe_type), url + '.mp4')
        cap = cv2.VideoCapture(video_path)

        FPS = cap.get(5)
        if FPS != 0:
            if split == 'training':
                frame_save_path = os.path.join(train_frame_root, url)
                train_writer.writerow([url + ';' + class_name])
            elif split == 'testing':
                frame_save_path = os.path.join(test_frame_root, url)
                test_writer.writerow([url + ';' + class_name])
            else:
                raise NotImplementedError('Only train or test !!!')
            if not os.path.exists(frame_save_path):
                os.mkdir(frame_save_path)
            
            # FPS = cap.get(5)
            # start_index = int(FPS * start)
            # end_index = int(FPS * end)

            # frame_freq = FPS // 3

            # frame_index = 0
            # while True:
            #     ret, frame = cap.read()
            #     if not ret:
            #         break
            #     if frame_index >= start_index and frame_index <= end_index:
            #         if frame_index % frame_freq == 0:
            #             cv2.imwrite(os.path.join(frame_save_path, str(frame_index).zfill(5) + '.jpg'), frame)
            #     elif frame_index > end_index:
            #         break
            #     frame_index += 1
            # print('FPS: {}. Staring from {} to {}. Saved {} frames at {}.'.format(FPS, start_index, end_index, len(os.listdir(frame_save_path)), frame_save_path))



