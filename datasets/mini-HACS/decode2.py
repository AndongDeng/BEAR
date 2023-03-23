import os
import csv

import cv2
# from moviepy.editor import VideoFileClip


data_root = 'segments_2sec/'
train_frame_root = 'frames/train/'
test_frame_root = 'frames/test/'

train_csv = open('annotations/hacs_train1.csv', 'w')
test_csv = open('annotations/hacs_test1.csv', 'w')
label_csv = open('annotations/labels1.csv', 'w')

train_writer = csv.writer(train_csv)
test_writer = csv.writer(test_csv)
label_writer = csv.writer(label_csv)

train_anno_file = open('train_download_pos_file.csv', 'r')
test_anno_file = open('test_download_pos_file.csv', 'r')

train_anno_reader = csv.reader(train_anno_file)
test_anno_reader = csv.reader(test_anno_file)

train_failure = []
test_failure = []

for row in train_anno_reader:
    classname, video_id, start, _ = row[0].split(',')
    class_name = classname.replace(' ', '_')
    start_int = int(float(start))
    video_id_start = video_id + '_' + str(start_int).zfill(5)
    video_path = os.path.join(data_root, class_name, video_id_start + '.mp4')

    if os.path.exists(video_path):

        frame_save_path = os.path.join(train_frame_root, video_id_start)
        if not os.path.exists(frame_save_path):
            os.mkdir(frame_save_path)

        # if len(os.listdir(frame_save_path)) == 0:
        #     try:
        #         # clip = VideoFileClip(video_path)
        #         # clip.write_images_sequence(os.path.join(frame_save_path, 'img_%05d.jpg'), verbose=False, logger=None)

        #         cap = cv2.VideoCapture(video_path)
        #         frame_index = 0
        #         while True:
        #             ret, frame = cap.read()
        #             if not ret:
        #                 train_failure.append(row[0])
        #                 break

        #             cv2.imwrite(os.path.join(frame_save_path, 'img_' + str(frame_index).zfill(5) + '.jpg'), frame)
        #             frame_index += 1

        #     except KeyError:
        #         print('*** Video Reading Failure !!! ***')
        #         train_failure.append(row[0])
        #     except OSError:
        #         print('*** Video Reading Failure !!! ***')
        #         train_failure.append(row[0])

        #     if len(os.listdir(frame_save_path)) == 0:
        #             train_failure.append(row[0])

        #     print('Training Part: saved {} frames at {}!'.format(len(os.listdir(frame_save_path)), frame_save_path))
        if len(os.listdir(frame_save_path)) != 0:
            train_writer.writerow([frame_save_path + ';' + class_name])


for row in test_anno_reader:
    classname, video_id, start, _ = row[0].split(',')
    class_name = classname.replace(' ', '_')
    start_int = int(float(start))
    video_id_start = video_id + '_' + str(start_int).zfill(5)
    video_path = os.path.join(data_root, class_name, video_id_start + '.mp4')

    if os.path.exists(video_path):

        frame_save_path = os.path.join(test_frame_root, video_id_start)
        if not os.path.exists(frame_save_path):
            os.mkdir(frame_save_path)


        # if len(os.listdir(frame_save_path)) == 0:
        #     try:
        #         # clip = VideoFileClip(video_path)
        #         # clip.write_images_sequence(os.path.join(frame_save_path, 'img_%05d.jpg'), verbose=False, logger=None)

        #         cap = cv2.VideoCapture(video_path)
        #         frame_index = 0
        #         while True:
        #             ret, frame = cap.read()
        #             if not ret:
        #                 test_failure.append(row[0])
        #                 break

        #             cv2.imwrite(os.path.join(frame_save_path, 'img_' + str(frame_index).zfill(5) + '.jpg'), frame)
        #             frame_index += 1

        #     except KeyError:
        #         print('*** Video Reading Failure !!! ***')
        #         test_failure.append(row[0])
        #     except OSError:
        #         print('*** Video Reading Failure !!! ***')
        #         test_failure.append(row[0])

        #     if len(os.listdir(frame_save_path)) == 0:
        #             test_failure.append(row[0])

        #     print('Test Part: saved {} frames at {}!'.format(len(os.listdir(frame_save_path)), frame_save_path))
        if len(os.listdir(frame_save_path)) != 0:   
            test_writer.writerow([frame_save_path + ';' + class_name])



train_fail = open('train_fail.txt', 'w')
test_fail = open('test_fail.txt', 'w')

for fail in train_failure:
    train_fail.write(fail + '\n')

for fail in test_failure:
    test_fail.write(fail + '\n')
