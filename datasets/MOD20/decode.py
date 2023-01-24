import csv
import os
from moviepy.editor import VideoFileClip


data_root = 'dataset/'
frame_root = 'frames/'
if not os.path.exists(frame_root):
    os.mkdir(frame_root)

label_csv = open('annotations/labels.csv', 'w')
label_writer = csv.writer(label_csv)

test_csv = open('annotations/mod20_test.csv', 'w')
train_csv = open('annotations/mod20_train.csv', 'w')

test_writer = csv.writer(test_csv)
train_writer = csv.writer(train_csv)

class_name_listdir = sorted(os.listdir(data_root))
for class_name in class_name_listdir:
    label_writer.writerow([class_name])
    video_listdir = sorted(os.listdir(os.path.join(data_root, class_name)))
    num_clips = len(video_listdir)
    num_test_clips = int(num_clips * 0.3)

    for i, video_name_mp4 in enumerate(video_listdir):
        video_name = video_name_mp4.split('.mp4')[0]
        video_path = os.path.join(data_root, class_name, video_name_mp4)
        clip = VideoFileClip(video_path)
        if i <= num_test_clips:
            frame_path = os.path.join(frame_root, 'test/', video_name)
            test_writer.writerow([video_name + ';' + class_name])
        else:
            frame_path = os.path.join(frame_root, 'train/', video_name)
            train_writer.writerow([video_name + ';' + class_name])

        if not os.path.exists(frame_path):
            os.mkdir(frame_path)
        if len(os.listdir(frame_path)) == 0:
            clip.write_images_sequence(os.path.join(frame_path, '%05d.jpg'), verbose=False, logger=None)
            print('saved {} frames in {}!'.format(len(os.listdir(frame_path)), frame_path))
        else:
            print('already saved!')

