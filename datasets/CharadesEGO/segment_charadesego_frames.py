import os
import csv

import sys

mode = sys.argv[1]

frame_root = 'frames/'
if not os.path.exists(frame_root):
    os.mkdir(frame_root)
video_root = 'CharadesEgo_v1/'

test_anno_file = open('CharadesEgoAnno/CharadesEgo/CharadesEgo_v1_{}_only1st.csv'.format(mode), 'r')
# test_anno_file = open('datasets/CharadesEgo/CharadesEgo_v1_test_only1st.csv', 'r')
test_anno_reader = csv.DictReader(test_anno_file)

label_anno_file = open('CharadesEgoAnno/CharadesEgo/Charades_v1_classes.txt', 'r')
# label_anno_file = open('datasets/CharadesEgo/Charades_v1_classes.txt', 'r')
label_file = open('annotations/labels.csv', 'w')
label_writer = csv.writer(label_file)

label_content = label_anno_file.readlines()
label_dict = dict()
for content in label_content:
    label_code = content[: 4]
    class_name = content[5: ].split('\n')[0]
    label_dict[label_code] = class_name
    label_writer.writerow([class_name])

test_file = open('annotations/charades_ego_{}.csv'.format(mode), 'w')
test_writer = csv.writer(test_file)



for row in test_anno_reader:

    actions = row['actions']
    video_id = row['id']

    video_path = os.path.join(video_root, video_id + '.mp4')

    if actions == '':
        actions = []
    else:
        action_split_list = actions.split(';')  # ['c00 0 4', 'c02 9 18', 'c09 10 19']

        for sub_action in action_split_list:
            action_cls, start, end = sub_action.split(' ')
            target_frame_path_name = video_id + '_' + action_cls + str(start) + '_' + str(end)
            target_frame_path = os.path.join(frame_root, target_frame_path_name)

            if not os.path.exists(target_frame_path):
                os.mkdir(target_frame_path)

            start = int(float(start))
            end = int(float(end))
            duration = str(end - start)

            ss_hour = start // 3600
            ss_minute = (start - ss_hour * 3600) // 60
            ss_second = start - ss_hour * 3600 - ss_minute * 60
            ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)
            cmd = 'ffmpeg -ss ' + ss + ' -i ' + video_path + ' -t ' + duration + ' ' + target_frame_path + '/%4d.jpg'
            os.system(cmd)
            print('decoded {} frames in {}'.format(len(os.listdir(target_frame_path)), target_frame_path))
            if len(os.listdir(target_frame_path)) > 0:
                test_writer.writerow([target_frame_path_name + ';' + label_dict[action_cls]])
