import os
import json
import csv

import cv2


video_root = 'raw_coin_videos/'

segmented_video_root = 'videos/'

if not os.path.exists(segmented_video_root):
    os.mkdir(segmented_video_root)


data_info = json.load(open('annotations/COIN.json', 'r'))['database']
for url in data_info.keys():

        video_info = data_info[url]

        recipe_type = video_info['recipe_type']  # class_id
        start = float(video_info['start'])
        end = float(video_info['end'])
        class_name = video_info['class']
        split = video_info['subset']

        target_segment_file_name = os.path.join(segmented_video_root, url + '.mp4')

        duration = str(int(end - start))

        ss_hour = start // 3600
        ss_minute = (start - ss_hour * 3600) // 60
        ss_second = start - ss_hour * 3600 - ss_minute * 60
        ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)

        video_path = os.path.join(video_root, str(recipe_type), url + '.mp4')

        cmd = 'ffmpeg -ss ' + ss + ' -i ' + video_path + ' -t ' + duration + ' ' + target_segment_file_name
        os.system(cmd)
        print('Successfully segment {} to {} !'.format(video_path, target_segment_file_name))