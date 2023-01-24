import os
import csv


def gen_anno(csv_reader):
    label_csv = open('annotations/labels.csv', 'w')
    label_writer  = csv.writer(label_csv)

    action_set = set()
    for content in csv_reader:
        video_id = content[0]
        action_name = content[2]
        start_index = int(content[3].split('.jpg')[0])
        end_index = int(content[4].split('.jpg')[0])

        action_set.add(action_name)
    
    action_list = list(action_set)
    print(action_list)
    for action in action_list:
        label_writer.writerow([action])




if __name__ == '__main__':
    raw_train_csv = open('MECCANO_action_temporal_annotations/train.csv', 'r')
    train_reader = csv.reader(raw_train_csv)
    gen_anno(train_reader)



