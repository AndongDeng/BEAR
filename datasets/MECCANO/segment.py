import os
import csv


def segment_frames(csv_reader, split, csv_writer):
    for content in csv_reader:
        video_id = content[0]
        action_name = content[2]
        start_index = int(content[3].split('.jpg')[0])
        end_index = int(content[4].split('.jpg')[0])

        target_video_name = video_id + '_' + str(start_index).zfill(5) + '_' + str(end_index).zfill(5)

        if split == 'train':
            frame_save_path = 'frames/train/'
        elif split == 'val':
            frame_save_path = 'frames/val/'
        elif split == 'test':
            frame_save_path = 'frames/test/'
        if not os.path.exists(frame_save_path):
            os.mkdir(frame_save_path)
        
        csv_writer.writerow([target_video_name + ';' + action_name])


        pre_frame_root = 'pre_frames/'
        pre_frame_path = os.path.join(pre_frame_root, video_id)

        target_frame_path = os.path.join(frame_save_path, target_video_name)
        if not os.path.exists(target_frame_path):
            os.mkdir(target_frame_path)

        for index in range(start_index, end_index + 1):
            cmd = 'cp ' + pre_frame_path + '/' + str(index).zfill(5) + '.jpg' + ' ' + target_frame_path + '/'
            os.system(cmd)
        print('copy {} frames from {} to {}'.format(end_index - start_index + 1, pre_frame_path, target_frame_path))


if __name__ == '__main__':
    raw_train_csv = open('MECCANO_action_temporal_annotations/train.csv', 'r')
    raw_test_csv = open('MECCANO_action_temporal_annotations/test.csv', 'r')
    raw_val_csv = open('MECCANO_action_temporal_annotations/val.csv', 'r')

    train_reader = csv.reader(raw_train_csv)
    test_reader = csv.reader(raw_test_csv)
    val_reader = csv.reader(raw_val_csv)

    train_csv = open('annotations/meccano_train.csv', 'w')
    test_csv = open('annotations/meccano_test.csv', 'w')
    val_csv = open('annotations/meccano_val.csv', 'w')

    train_writer = csv.writer(train_csv)
    test_writer = csv.writer(test_csv)
    val_writer = csv.writer(val_csv)

    segment_frames(train_reader, 'train', train_writer)
    segment_frames(test_reader, 'test', test_writer)
    segment_frames(val_reader, 'val', val_writer)




