import os
import csv
from re import X

# import cv2
# from moviepy.editor import VideoFileClip


def convert_float_to_str(x):
    """
    input_float: xx.xx or xx.x or xx.0 or x.x or x.0
    return '00xx.xx'
    """
    x = format(float(x), '.2f')
    x = str(x).zfill(7)
    return x


if __name__ == '__main__':

    video_root = 'RGBSegmented/'
    train_frame_root = 'frames/train/'
    test_frame_root = 'frames/test/'

    # train_csv = open('inhard_train.csv', 'w')
    test_csv = open('inhard_test.csv', 'w')

    label_csv = open('labels.csv', 'w')
    label_writer = csv.writer(label_csv)

    # train_writer = csv.writer(train_csv)
    test_writer = csv.writer(test_csv)


    S_train = ['P01_R01', 'P01_R03', 'P03_R01', 'P03_R03', 'P03_R04', 
            'P04_R02', 'P05_R03', 'P05_R04', 'P06_R01', 'P07_R01', 
            'P07_R02', 'P08_R02', 'P08_R04', 'P09_R01', 'P09_R03', 
            'P10_R01', 'P10_R02', 'P10_R03', 'P11_R02', 'P12_R01', 
            'P12_R02', 'P13_R02', 'P14_R01', 'P15_R01', 'P15_R02', 'P16_R02']

    S_test = ['P01_R02', 'P02_R01', 'P02_R02', 'P04_R01', 'P05_R01', 'P05_R02', 
            'P08_R01', 'P08_R03', 'P09_R02', 'P11_R01', 'P14_R02', 'P16_R01']

    annotation_csv = open('InHARD.csv', 'r')
    annotation_content = csv.reader(annotation_csv)
    label_set = set()
    for i, line in enumerate(annotation_content):
        if i >= 1:
            Action_end_rgb_sec = line[3]  # decide video file name
            Action_start_rgb_sec = line[7]
            File = line[9]  # decide train/test split
            Meta_action_label = line[11]  # decide video directory
            label_set.add(Meta_action_label)

            start_str = convert_float_to_str(Action_start_rgb_sec)
            end_str = convert_float_to_str(Action_end_rgb_sec)

            # video_name = File + '_' + str(Action_start_rgb_sec).zfill(7) + '_' + str(Action_end_rgb_sec).zfill(7)
            video_name = File + '_' + start_str + '_' + end_str

            video_path = os.path.join(video_root, Meta_action_label, video_name  + '.mp4')

            # cap = cv2.VideoCapture(video_path)
            if File in S_train:
                frame_save_path = os.path.join(train_frame_root, video_name)
                # train_writer.writerow([video_name + ';' + Meta_action_label])
            elif File in S_test:
                frame_save_path = os.path.join(test_frame_root, video_name)
                test_writer.writerow([video_name + ';' + Meta_action_label])
            if not os.path.exists(frame_save_path):
                os.mkdir(frame_save_path)

            # clip = VideoFileClip(video_path)
            # clip.write_images_sequence(os.path.join(frame_save_path, '%05d.jpg'), verbose=False, logger=None)
            # print('saved {} frames in {}'.format(len(os.listdir(frame_save_path)), frame_save_path))
    label_list = list(label_set)
    print(label_list)
    for label in label_list:
        label_writer.writerow([label])
    
    # x1 = '9'
    # x2 = '9.1'
    # x3 = '9.45999999'
    # x4 = '9.0'
    # x5 = '9.1000001'

    # y1 = convert_float_to_str(x1)
    # y2 = convert_float_to_str(x2)
    # y3 = convert_float_to_str(x3)
    # y4 = convert_float_to_str(x4)
    # y5 = convert_float_to_str(x5)

    # print(y1, y2, y3, y4, y5)
        





