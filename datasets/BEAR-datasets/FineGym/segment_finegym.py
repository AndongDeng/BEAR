import os
import cv2
import json

data_info = json.load(open('finegym_annotation_info_v1.0.json', 'r'))
data_root = './raw_finegym_videos/'
video_root = './videos/'
if not os.path.exists(video_root):
    os.mkdir(video_root)

data_listdir = os.listdir(data_root)
for video_name in data_listdir:
    video_path = os.path.join(data_root, video_name)
    url = video_name.split('.')[0]
    raw_info = data_info[url]

    for event_key in raw_info.keys():

        event_info = raw_info[event_key]

        start = int(event_key.split('E_')[1].split('_')[0])
        end = int(event_key.split('E_')[1].split('_')[1]) + 1

        seg_info = event_info['segments']

        if seg_info:
            for clip_key in seg_info.keys():
                sub_start = int(clip_key.split('A_')[1].split('_')[0])
                sub_end = int(clip_key.split('A_')[1].split('_')[1]) + 1
                duration = str(int(sub_end - sub_start))
                ss_tmp = start + sub_start
                ss_hour = ss_tmp // 3600
                ss_minute = (ss_tmp - ss_hour * 3600) // 60
                ss_second = ss_tmp - ss_hour * 3600 - ss_minute * 60
                ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)
                destination = os.path.join(video_root, url + '_' + event_key + '_' + clip_key + '.mp4')
                os.system('ffmpeg -ss ' + ss + ' -i ' + video_path + ' -t ' + duration + ' ' + destination)
                if os.path.exists(destination):
                    print('Successfully obtain video clips at {}!'.format(destination))



    