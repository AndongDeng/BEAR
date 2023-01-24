import os 
import csv

train_Pid_list = [0, 2, 5, 6, 7, 8, 10, 11, 12, 13, 
                 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 
                 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 
                 49, 50, 51, 52, 53, 55, 56, 57, 59, 61, 
                 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 
                 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 
                 86, 87, 88, 89, 90, 98, 100, 102, 103, 
                 105, 106, 110, 111, 112, 114, 115, 116, 117, 118]

test_Pid_list = []
for i in range(119):
    if i not in train_Pid_list:
        test_Pid_list.append(i)

label_f = open('annotations/labels.csv', 'r')
label_content = csv.reader(label_f)
label_dict = dict()
for i, l in enumerate(label_content):
    label_dict[i] = l[0]

train_anno_f = open('annotations/uav_human_cs1_train.csv', 'w')
test_anno_f = open('annotations/uav_human_cs1_test.csv', 'w')

train_writer = csv.writer(train_anno_f)
test_writer = csv.writer(test_anno_f)

data_root = 'frames/'
data_listdir = os.listdir(data_root)

for video_name in data_listdir:
    # P078S06G10B40H20UC072000LC031000A141R0_09171105
    person_id = int(video_name.split('P')[1][0: 3])
    action_id = int(video_name.split('A')[1][0: 3])

    if person_id in train_Pid_list:
        train_writer.writerow([video_name + ';' + label_dict[action_id]])
    else:
        test_writer.writerow([video_name + ';' + label_dict[action_id]])




