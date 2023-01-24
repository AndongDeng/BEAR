import os
import csv
import sys

mode = sys.argv[1]

labels_dict = {'B1': 'Fighting', 'B2': 'Shooting', 'B4': 'Riot', 'B5': 'Abuse', 'B6': 'Car accident', 'G': 'Explosion', 'A': 'Non-violen'}

csv_file = open('xd_violence_{}.csv'.format(mode), 'w')
csv_writer = csv.writer(csv_file)

frame_root = './frames/{}'.format(mode)

video_listdir = os.listdir(frame_root)

for video_name in video_listdir:
    raw_labels = video_name.split('label_')[1].split('_')[0]
    assert raw_labels in labels_dict.keys(), 'wrong labels {}'.format(raw_labels)
    csv_writer.writerow([video_name + ';' + labels_dict[raw_labels]])



