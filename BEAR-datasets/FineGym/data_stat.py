import os
import json
from statistics import mean

data_info = json.load(open('finegym_annotation_info_v1.0.json', 'r'))
num_videos = len(data_info.keys())

print('Number of Videos: ', num_videos)

train_split_file = open('gym99_train_element_v1.0.txt', 'r')
test_split_file = open('gym99_val_element.txt', 'r')

train_content = train_split_file.readlines()
num_train_clips = len(train_content)
print('Number of Train Clips: ', num_train_clips)

test_content = test_split_file.readlines()
num_test_clips = len(test_content)
print('Number of Train Clips: ', num_test_clips)

train_sample_dict =  dict()
test_sample_dict = dict()

duration = 0
for sample in train_content:
    sample_id, class_id = sample.split(' ')
    url, E, start, end, A, sub_start, sub_end = sample_id.split('_')
    if class_id not in train_sample_dict.keys():
        train_sample_dict[class_id] = 1
    else:
        train_sample_dict[class_id] += 1
    duration += int(sub_end) - int(sub_start)


for sample in test_content:
    sample_id, class_id = sample.split(' ')
    class_id = class_id.split('\n')[0]
    url, E, start, end, A, sub_start, sub_end = sample_id.split('_')
    if class_id not in train_sample_dict.keys():
        test_sample_dict[class_id] = 1
    else:
        test_sample_dict[class_id] += 1
    duration += int(sub_end) - int(sub_start)


video_hour = duration / 3600
avg_len = duration / (num_train_clips + num_test_clips)

min_num = min(train_sample_dict.values())
max_num = max(train_sample_dict.values())
avg_num = mean(train_sample_dict.values())

print('video hour: ', video_hour)
print('avg length: ', avg_len)

print(min_num, max_num, avg_num)
