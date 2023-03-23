import os
import csv
# import cv2
from moviepy.editor import VideoFileClip

anomaly_data_root = '/home/ubuntu/data16T/UCF-Crime/Anomaly_Videos/'
normal_data_root = '/home/ubuntu/data16T/UCF-Crime/Normal_Videos_for_Event_Recognition/'
frame_root = './frames/'

content = open('Action_Recognition_splits/test_001.txt', 'r').readlines()

for line in content:
    if line.startswith('Normal'):
        video_name = line.split('/')[1].split('.mp4')[0]
        video_path = os.path.join(normal_data_root, video_name + '.mp4')
        pass
    else:
        class_name = line.split('/')[0]
        video_name = line.split('/')[1].split('.mp4')[0]
        video_path = os.path.join(anomaly_data_root, class_name, video_name + '.mp4')

    frame_path = os.path.join(frame_root, video_name)
    if not os.path.exists(frame_path):
        os.mkdir(frame_path)
    assert os.path.exists(video_path), '{} does not exists!'.format(video_path)

    if len(os.listdir(frame_path)) == 0:
        clip = VideoFileClip(video_path)
        clip.write_images_sequence(os.path.join(frame_path, '%05d.jpg'), fps=3, verbose=False, logger=None)
        print('saved {} frames !'.format(len(os.listdir(frame_path))))
    else:
        print('Already decoded!')
