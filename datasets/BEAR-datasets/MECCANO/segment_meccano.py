import os
import csv
from tqdm import tqdm

def segment_frames(csv_reader, split):
    
    print('Segmenting {} ... '.format(split))

    for content in tqdm(csv_reader):
        video_id = content[0]
        # action_name = content[2]
        start_index = int(content[3].split('.jpg')[0])  # frame index
        end_index = int(content[4].split('.jpg')[0])

        FPS = 12

        start = start_index // FPS
        end = end_index // FPS
        duration = str(end - start)

        ss_hour = start // 3600
        ss_minute = (start - ss_hour * 3600) // 60
        ss_second = start - ss_hour * 3600 - ss_minute * 60
        ss = str(ss_hour).zfill(2) + ':' + str(ss_minute).zfill(2) + ':' + str(ss_second).zfill(2)

        target_video_name = video_id + '_' + str(start_index).zfill(5) + '_' + str(end_index).zfill(5)

        if split == 'train':
            segment_video_path = 'videos/train/'
        elif split == 'val':
            segment_video_path = 'videos/train/'
        elif split == 'test':
            segment_video_path = 'videos/test/'
        if not os.path.exists(segment_video_path):
            os.mkdir(segment_video_path)
        
        raw_vide_root = 'MECCANO_RGB_Videos/'
        raw_video_path = os.path.join(raw_vide_root, video_id)

        target_video_path = os.path.join(segment_video_path, target_video_name)
        if not os.path.exists(target_video_path):
            os.mkdir(target_video_path)

        cmd = 'ffmpeg -ss ' + ss + ' -i ' + raw_video_path + ' -t ' + duration + ' ' + target_video_path
        os.system(cmd)
        # print('Successfully segment {} to {} !'.format(raw_video_path, target_video_path))


if __name__ == '__main__':
    raw_train_csv = open('MECCANO_action_annotations/MECCANO_train_actions.csv', 'r')
    raw_test_csv = open('MECCANO_action_annotations/MECCANO_test_actions.csv', 'r')
    raw_val_csv = open('MECCANO_action_annotations/MECCANO_val_actions.csv', 'r')

    train_reader = csv.reader(raw_train_csv)
    test_reader = csv.reader(raw_test_csv)
    val_reader = csv.reader(raw_val_csv)

    segment_frames(train_reader, 'train')
    segment_frames(test_reader, 'test')
    segment_frames(val_reader, 'val')




