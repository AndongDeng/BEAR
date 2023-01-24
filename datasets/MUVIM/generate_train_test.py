from doctest import testfile
import os
import csv

from sklearn.preprocessing import OrdinalEncoder

train_split = 0.8

num_fall = 371
num_nonfall = 1127 - num_fall

train_fall = int(train_split * num_fall)
test_fall = num_fall - train_fall
train_nonfall = int(train_split * num_nonfall)
test_nonfall = num_nonfall - train_nonfall

print('train fall: {}; test fall: {}'.format(train_fall, test_fall))
print('train nonfall: {}; test nonfall: {}'.format(train_nonfall, test_nonfall))

origianal_file = open('annotations/train.csv', 'r')
ori_reader = csv.reader(origianal_file)

train_file = open('annotations/muvim_train.csv', 'w')
test_file = open('annotations/muvim_test.csv', 'w')

train_writer = csv.writer(train_file)
test_writer = csv.writer(test_file)

for i, row in enumerate(ori_reader):
    if i < train_fall:
        train_writer.writerow(row)
    elif train_fall <= i < num_fall:
        test_writer.writerow(row)
    elif num_fall <= i < num_fall + train_nonfall:
        train_writer.writerow(row)
    else:
        test_writer.writerow(row)
    



