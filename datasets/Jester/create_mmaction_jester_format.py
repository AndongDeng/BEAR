import os
import sys
import csv

mode = sys.argv[1]
root = sys.argv[2]

labels_file = 'labels/labels.csv'

if mode == 'train':
    original_ann_file = 'labels/train.csv'
    new_format_ann_file = 'labels/train_mmformat.txt'
elif mode == 'validation':
    original_ann_file = 'labels/validation.csv'
    new_format_ann_file = 'labels/validation_mmformat.txt'
elif mode == 'test':
    original_ann_file = 'labels/test-answers.csv'
    new_format_ann_file = 'labels/test_mmformat.txt'
else:
    raise NotImplementedError

labels = open(labels_file, 'r')
labels_reader = csv.reader(labels)
labels_dict = dict()
i = 1
for label in labels_reader:
    labels_dict[label[0]] = i
    i += 1
labels.close()
# print(labels_dict)


"""
convert the original to the following format:

some/directory-1 163 1
some/directory-2 122 1
some/directory-3 258 2
some/directory-4 234 2
some/directory-5 295 3
some/directory-6 121 3

""" 

csv_file = open(os.path.join(root, original_ann_file), 'r')
new_format_file = open(os.path.join(root, new_format_ann_file), 'w')

reader = csv.reader(csv_file)
for line in reader:
    video_id, category = line[0].split(';')
    frame_number = os.listdir(os.path.join(root, video_id))
    category_id = labels_dict[category]
    content = video_id + ' ' + str(frame_number) + ' ' + str(category_id)
    new_format_file.write(content)

csv_file.close()
new_format_file.close()


