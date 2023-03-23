import csv
import os
import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--root', default='', type=str)
parser.add_argument('--protocol', default='CS', type=str)

args = parser.parse_args()


f = open('./splits/test_'+args.protocol+'.txt', "r")
dir1 = args.root
outfile = open('./labels/test_Labels_CV2.csv', "w")
outf = csv.writer(outfile, delimiter=',')
outf.writerow(['name', 'start', 'end'])

for i in f.readlines():
    n_frames = len(os.listdir(dir1 + os.path.splitext(i.strip())[0]))
    div = int(math.ceil(n_frames//128))

    if div>0:
        for j in range(0, div):
            t = 128
            outf.writerow([os.path.splitext(i.strip())[0], j*t, (j+1)*t])
    else:
        outf.writerow([os.path.splitext(i.strip())[0], '0', int(n_frames)])


