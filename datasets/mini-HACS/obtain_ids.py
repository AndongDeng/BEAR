import csv

train_reader = csv.reader(open('train.csv', 'r'))
test_reader = csv.reader(open('test.csv', 'r'))

ids = []

i = 0
for row in train_reader:
    video_id = row[0].split(' ')[0][6: 17]
    ids.append(video_id)
    i += 1

for row in test_reader:
    video_id = row[0].split(' ')[0][5: 16]
    ids.append(video_id)
    i += 1

print(i)
print(len(ids))
yid_file_writer = csv.writer(open('mini_hacs_vid.csv', 'w'))
for k, id in enumerate(ids):
    print(k)
    yid_file_writer.writerow([id])
