import enum
import os
import csv

video_root = 'NonFall/'
fall_seg_frame_root = 'frames/'
if not os.path.exists(fall_seg_frame_root):
    os.mkdir(fall_seg_frame_root)


nonfall_video_listdir = os.listdir(video_root)
for video_name in nonfall_video_listdir:
    video_path = os.path.join(video_root, video_name)
    video_frame_listdir = os.listdir(video_path)
    for i, frame in enumerate(video_frame_listdir):
        start = i // 300 * 300 + 1
        end = (i // 300 + 1) * 300
        target_path = os.path.join(fall_seg_frame_root, video_name + '_' + str(start) + '_' + str(end) + '/')
        if not os.path.exists(target_path):
            os.mkdir(target_path)
        frame_path = os.path.join(video_path, frame)
        cmd = 'cp ' + frame_path + ' ' + target_path
        os.system(cmd)
        if (i + 1) % 300 == 0:
             print('copy {} frames to {}'.format(len(os.listdir(target_path)), target_path))
