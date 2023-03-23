import os
import cv2


data_root = 'videos/'
frame_root = 'pre_frames/'

video_listdir = os.listdir(data_root)
for video in video_listdir:
    video_path = os.path.join(data_root, video)
    cap = cv2.VideoCapture(video_path)

    frame_save_path = os.path.join(frame_root, video.split('.mp4')[0])
    if not os.path.exists(frame_save_path):
        os.mkdir(frame_save_path)
    
    frame_index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imwrite(os.path.join(frame_save_path, str(frame_index).zfill(5) + '.jpg'), frame)
        frame_index += 1
    print('saved {} frames in {}'.format(len(os.listdir(frame_save_path)), frame_save_path))

