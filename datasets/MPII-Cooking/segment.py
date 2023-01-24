import os
import csv

import cv2
from tqdm import tqdm

video_root = 'videos/'
raw_frame_root = 'raw_frames/'
if not os.path.exists(raw_frame_root):
    os.mkdir(raw_frame_root)
frame_root = 'frames'

raw_annotation_csv = open('annotations/detectionGroundtruth-1-0.csv', 'r')
raw_csv_reader = csv.reader(raw_annotation_csv)

label_csv = open('labels.csv', 'w')
label_writer = csv.writer(label_csv)
label_set = set()

annotation_csv = open('mpi_cooking.csv', 'w')
annotation_writer = csv.writer(annotation_csv)


# # save whole frames
# video_listdir = os.listdir(video_root)
# for video_name in video_listdir:
#     video_path = os.path.join(video_root, video_name)

#     cap = cv2.VideoCapture(video_path)

#     frame_index = 0
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame_path = os.path.join(raw_frame_root, video_name.split('.avi')[0])
#         if not os.path.exists(frame_path):
#             os.mkdir(frame_path)
#         cv2.imwrite(os.path.join(frame_path, str(frame_index).zfill(5) + '.jpg'), frame)

#         frame_index += 1
#     print('saved {} frames in {}!'.format(len(os.listdir(frame_path)), frame_path))



# save segment frame
for line in tqdm(raw_csv_reader):
    subject, file_name, start, end, category_id, activity_category = line
    label_set.add(activity_category)

    start = int(start)
    end = int(end)
    raw_frame_path = os.path.join(raw_frame_root, file_name)

    clip_name = file_name + '_' + str(start).zfill(5) + '_' + str(end).zfill(5)
    target_file_path = os.path.join(frame_root, clip_name)

    annotation_writer.writerow([clip_name + ';' + activity_category])
    # if not os.path.exists(target_file_path):
    #     os.mkdir(target_file_path)

    # for index in range(start, end + 1):
    #     frame_saved_path = os.path.join(raw_frame_path, str(index).zfill(5) + '.jpg')

    #     cmd = 'cp ' + frame_saved_path +  ' ' + target_file_path + '/'
    #     os.system(cmd)


label_list = list(label_set)
for label in label_list:
    label_writer.writerow([label])





