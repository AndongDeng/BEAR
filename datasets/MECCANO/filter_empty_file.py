from fileinput import filename
import os
import csv
import sys


mode = sys.argv[1]

csv_file = open('annotations/meccano_{}.csv'.format(mode), 'r')
csv_reader = csv.reader(csv_file)

frame_root = 'frames/{}'.format(mode)

for content in csv_reader:
    file_name = content[0].split(';')[0]
    frame_path = os.path.join(frame_root, )
