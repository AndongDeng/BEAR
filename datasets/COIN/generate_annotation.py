import os
import json
import csv
import cv2

video_root = 'videos/'
data_info = json.load(open('annotations/COIN.json', 'r'))['database']

train_csv = open('annotations/coin_train.csv', 'w')
test_csv = open('annotations/coin_test.csv', 'w')

train_writer = csv.writer(train_csv)
test_writer = csv.writer(test_csv)

for url in data_info.keys():

        video_info = data_info[url]

        recipe_type = video_info['recipe_type']  # class_id
        # start = float(video_info['start'])
        # end = float(video_info['end'])
        class_name = video_info['class']
        split = video_info['subset']

        video_path = os.path.join(video_root, str(recipe_type), url + '.mp4')
        cap = cv2.VideoCapture(video_path)

        FPS = cap.get(5)
        if FPS != 0:
            num_frames = cap.get(7)
            if split == 'training':
                train_writer.writerow([url + ' ' + num_frames + ' ' + class_name])
            elif split == 'testing':
                test_writer.writerow([url + ' ' + num_frames + ' '  + class_name])
            else:
                raise NotImplementedError('Only train or test !!!')
