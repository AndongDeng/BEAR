import os
import csv

annotations = open('detectionGroundtruth-1-0.csv', 'r')
reader = csv.reader(annotations)

action_dict = dict()

durations = 0

for line in reader:
    subject, video_name, start, end, action_id, action_name = line
    if action_name not in action_dict.keys():
        action_dict[action_name] = 1
    else:
        action_dict[action_name] += 1
    
    durations += (int(end) - int(start))


total = sum(action_dict.values())
video_hour = durations / 3600
avg_len = durations / total
num_class = len(action_dict.values())

min_num = min(action_dict.values())
max_num = max(action_dict.values())
mean_num = total / num_class
print(total)

print(video_hour, avg_len, min_num, max_num, mean_num, len(action_dict.values()))



