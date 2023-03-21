import os
import csv

import sys

split = sys.argv[1]  # 'train' or 'test'

segmented_video_root = 'videos/'
if not os.path.exists(segmented_video_root):
    os.mkdir(segmented_video_root)

original_video_root = 'CharadesEgo_v1/'
anno_csv_file = open('annotations/CharadesEgo_v1_{}_only1st.csv'.format(split), 'r')
anno_csv_reader = csv.DictReader(anno_csv_file)
label_anno_file = open('annotations/Charades_v1_classes.txt', 'r')

for row in anno_csv_reader:

    actions = row['actions']
    video_id = row['id']

    video_path = os.path.join(original_video_root, video_id + '.mp4')

    if actions == '':
        actions = []
    else:
        action_split_list = actions.split(';')  # ['c00 0 4', 'c02 9 18', 'c09 10 19']

        for sub_action in action_split_list:
            action_cls, start, end = sub_action.split(' ')
            target_segment_file_name = video_id + '_' + action_cls + str(start) + '_' + str(end) + '.mp4'

            start = int(float(start))
            end = int(float(end))
            duration = str(end - start)

            ss_hour = start // 3600
            ss_minute = (start - ss_hour * 3600) // 60
            ss_second = start - ss_hour * 3600 - ss_minute * 60
            ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)
            cmd = 'ffmpeg -ss ' + ss + ' -i ' + video_path + ' -t ' + duration + ' ' + target_segment_file_name
            os.system(cmd)
            print('Successfully segment {} to {} !'.format(video_path, target_segment_file_name))
