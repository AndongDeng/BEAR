import os
import csv


def convert_float_to_str(x):
    """
    input_float: xx.xx or xx.x or xx.0 or x.x or x.0
    return '00xx.xx'
    """
    x = format(float(x), '.2f')
    x = str(x).zfill(7)
    return x


if __name__ == '__main__':

    raw_root = 'RGBSegmented/'
    train_root = 'videos/train/'
    test_root = 'videos/test/'


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

            start = int(start_str)
            end = int(end_str)

            duration = str(int(end) - int(start))

            ss_hour = start // 3600
            ss_minute = (start - ss_hour * 3600) // 60
            ss_second = start - ss_hour * 3600 - ss_minute * 60
            ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)

            # video_name = File + '_' + str(Action_start_rgb_sec).zfill(7) + '_' + str(Action_end_rgb_sec).zfill(7)
            video_name = File + '_' + start_str + '_' + end_str

            raw_video_path = os.path.join(raw_root, Meta_action_label, video_name  + '.mp4')

            if File in S_train:
                target_segment_file_name = os.path.join(train_root, video_name + '.mp4')
            elif File in S_test:
                target_segment_file_name = os.path.join(test_root, video_name + '.mp4')

            cmd = 'ffmpeg -ss ' + ss + ' -i ' + raw_video_path + ' -t ' + duration + ' ' + target_segment_file_name
            os.system(cmd)

            print('Successfully segment {} to {} !'.format(raw_video_path, target_segment_file_name))
