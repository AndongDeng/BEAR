import os
import sys
import csv

fall_video_root = 'Fall/'
fall_seg_frame_root = 'frames/'
if not os.path.exists(fall_seg_frame_root):
    os.mkdir(fall_seg_frame_root)

fall_annotations = open('Labels.csv', 'r')
fall_reader = csv.reader(fall_annotations)

for i, content in enumerate(fall_reader):
    if i >= 1:
        _, _, video, start, end, _, duration = content
        taregt_path = os.path.join(fall_seg_frame_root, 'Fall' + video + '_' + start + '_' + end + '/')
        if not os.path.exists(taregt_path):
            os.mkdir(taregt_path)
        # print(content)
        video_path = os.path.join(fall_video_root, 'Fall' + video + '/')
        if os.path.exists(video_path):
            for index in range(int(start), int(end) + 1):
                frame_path = os.path.join(video_path, 'left' + str(index).zfill(6) + '.png')
                cmd = 'cp ' + frame_path + ' ' + taregt_path
                os.system(cmd)
        print('copy {} frames to {}'.format(len(os.listdir(taregt_path)), taregt_path))
