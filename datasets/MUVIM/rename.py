import os

data_root = 'frames/'
video_name_list = os.listdir(data_root)
for video in video_name_list:
    video_path = os.path.join(data_root, video)
    for i, frame_name in enumerate(os.listdir(video_path)):
        old_path = os.path.join(video_path, frame_name)
        new_path = os.path.join(video_path, str(i).zfill(5) + '.jpg')
        os.rename(old_path, new_path)