import os
import csv
import sys

mode = sys.argv[1]

# generate label txt
label_f = open('label.csv', 'w')
label_writer = csv.writer(label_f)
label_set = set()

# generate test csv file, video_name;class_name
test_csv = open('toyota_smarthome_cs_{}.csv'.format(mode), 'w')
test_writer = csv.writer(test_csv)

test_CS = open('splits/{}_CS.txt'.format(mode), 'r')
test_content = test_CS.readlines()
for line in test_content:
    class_name = line.split('_p')[0]
    label_set.add(class_name)
    video_name = line.split('.mp4')[0]

    test_writer.writerow([video_name + ';' + class_name])

label_list = list(label_set)
print(label_list)
for label in label_list:
    label_writer.writerow([label])



