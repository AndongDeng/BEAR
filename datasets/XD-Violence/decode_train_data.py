from genericpath import exists
import os
import cv2
# from moviepy.editor import VideoFileClip

data_roots_list = ['1-1004/', '1005-2004/', '2005-2804/', '2805-3319/', '3320-3954/']

frame_root = './frames/train/'
if not os.path.exists(frame_root):
    os.mkdir(frame_root)

for data_root in data_roots_list:
    video_listdir = os.listdir(data_root)
    for video_name in video_listdir:
        video_path = os.path.join(data_root, video_name)
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(5)
        frame_freq = fps // 3

        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_path = os.path.join(frame_root, video_name.split('.mp4')[0])
            if not os.path.exists(frame_path):
                os.mkdir(frame_path)
            if frame_index % frame_freq == 0:
                cv2.imwrite(os.path.join(frame_path, str(frame_index).zfill(4) + '.jpg'), frame)
            frame_index += 1
        # frame_path = os.path.join(frame_root, video_name.split('.mp4')[0])
        # if not os.path.exists(frame_path):
        #     os.mkdir(frame_path)
        # clip = VideoFileClip(video_path)
        # clip.write_images_sequence(os.path.join(frame_path, '%05d.jpg'), fps=3, verbose=False, logger=None)
        print('saved {} frames at {} !!! '.format(len(os.listdir(frame_path)), frame_path))