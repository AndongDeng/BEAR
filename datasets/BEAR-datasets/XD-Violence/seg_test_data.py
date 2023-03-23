import os
import cv2


data_root = '/home/ubuntu/data16T/xd_violence/videos/'
frame_root = '/home/ubuntu/data16T/xd_violence/frames/test/'
if not os.path.exists(frame_root):
    os.mkdir(frame_root)

labels_list = ['B1', 'B2', 'B4', 'B5', 'B6', 'G']

annotations = open('annotations_multiclasses.txt', 'r')
video_content = annotations.readlines()
video_content_dict = dict()

for line in video_content:

    video_name = line.split(' ')[0].split('.mp4')[0]
    video_path = os.path.join(data_root, video_name + '.mp4')
    raw_labels = video_name.split('label_')[1].split('-')
    timestamps = line.split('\n')[0].split(' ')[1: ]
    num_clip = len(timestamps) // 3

    start_list = []
    end_list = []

    for i in range(num_clip):

        label = timestamps[i * 3]
        start = int(timestamps[i * 3 + 1])
        end = int(timestamps[i * 3 + 2])
        start_list.append(start)
        end_list.append(end)

    cap = cv2.VideoCapture(video_path)

    frame_index = 0
    clip_index = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break
        
        if clip_index < num_clip:
            if frame_index >= start_list[clip_index] and frame_index <= end_list[clip_index]:
                frame_save_path = os.path.join(frame_root, video_name.split('label_')[0] + 'label_' + label + '_' + str(start_list[clip_index]).zfill(5) + '_' + str(end_list[clip_index]).zfill(5))
                if not os.path.exists(frame_save_path):
                    os.mkdir(frame_save_path)
                cv2.imwrite(os.path.join(frame_save_path, str(frame_index).zfill(5)) + '.jpg', frame)
            elif frame_index > end_list[clip_index]:
                clip_index += 1
                print('save {} frames in {}'.format(len(os.listdir(frame_save_path)), frame_save_path))
            else:
                pass
            frame_index += 1






        
        

