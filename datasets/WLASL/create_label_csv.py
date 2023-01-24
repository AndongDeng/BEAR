from cgi import test
import os
import json
import csv

data_root = 'frames/'
file_path = 'WLASL_v0.3.json'

train_label_file = 'train.csv'
validation_label_file = 'validation.csv'
test_label_file = 'test.csv'
label_file = 'label.csv'


train_csv = open(train_label_file, 'w')
validation_csv = open(validation_label_file, 'w')
test_csv = open(test_label_file, 'w')
label_csv = open(label_file, 'w')

train_writer = csv.writer(train_csv)
validation_writer = csv.writer(validation_csv)
test_writer = csv.writer(test_csv)
label_writer = csv.writer(label_csv)

with open(file_path) as ipf:
    content = json.load(ipf)

cnt_train = 0
cnt_val = 0
cnt_test = 0

for category_id, ent in enumerate(content):
    if category_id <= 99:

        gloss = ent['gloss']
        label_writer.writerow([gloss])

        for inst in ent['instances']:

            split = inst['split']
            video_id = inst['video_id']
            frame_path = os.path.join(data_root, video_id)
            
            if os.path.exists(frame_path):
                frame_number = len(os.listdir(frame_path))

                to_write = [video_id + ';' + gloss]

                if split == 'train':
                    train_writer.writerow(to_write)
                    cnt_train += 1
                elif split == 'val':
                    validation_writer.writerow(to_write)
                    cnt_val += 1
                elif split == 'test':
                    test_writer.writerow(to_write)            
                    cnt_test += 1
                else:
                    raise ValueError("Invalid split.")

print('train samples: {}'.format(cnt_train))
print('validation samples: {}'.format(cnt_val))
print('test samples: {}'.format(cnt_test))
