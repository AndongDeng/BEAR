import os
import csv
import cv2


data_root = './MISAW-Training-data/Video/'
annotations_root = './MISAW-Training-data/Procedural decription/'
frame_root = './frames/test/'
if not os.path.exists(frame_root):
    os.mkdir(frame_root)

# test_anno_file_csv = open('misaw_test.csv', 'w')
# test_writer = csv.writer(test_anno_file_csv)

label_csv = open('labels1.csv', 'w')
label_writer = csv.writer(label_csv)

video_list_dir = os.listdir(data_root)

action_set = set()
state_shift = 0  # num of clips
pre_action = ''
clip_path = ''

for video_name in video_list_dir:
    video_path = os.path.join(data_root, video_name)
    video_id = video_name.split('.mp4')[0]
    print('processing video: {}'.format(video_id))
    annotations_path = os.path.join(annotations_root, video_id + '_annotation.txt')
    annotation_content = open(annotations_path, 'r').readlines()[1:]

    cap = cv2.VideoCapture(video_path)

    frame_index = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 1. find action labels for current frame
        line = annotation_content[frame_index]
        v_left = line.split('\t')[2]
        t_left = line.split('\t')[3]

        action = v_left + t_left
        action_set.add(action)

        if action != pre_action:
            print('change action to: {}'.format(action))
            state_shift += 1
            clip_name = str(state_shift).zfill(4)
            # test_writer.writerow([clip_name + ';' + action])
            pre_action = action
            
#             if os.path.exists(clip_path):
#                 print('saving {} frames !'.format(len(os.listdir(clip_path))))

#             clip_path = os.path.join(frame_root, clip_name)
#             if not os.path.exists(clip_path):
#                 os.mkdir(clip_path)

#         frame_save_path = os.path.join(clip_path, str(frame_index).zfill(3) + '.jpg')
#         cv2.imwrite(frame_save_path, frame)
        frame_index += 1

action_list = list(action_set)
for a in action_list:
    label_writer.writerow([a])





