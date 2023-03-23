import os
import cv2


mp4_root = './mp4/'
frame_root = './frames/'

video_list_dir = os.listdir(mp4_root)
for video_name in video_list_dir:
    video_path = os.path.join(mp4_root, video_name)
    cap = cv2.VideoCapture(video_path)

    video_name_new = video_name.split('.mp4')[0]
    print('saving frames of video {} ...'.format(video_name_new))

    i = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break
        
        frame_save_dir = os.path.join(frame_root, video_name_new)
        if not os.path.exists(frame_save_dir):
            os.mkdir(frame_save_dir)

        cv2.imwrite(os.path.join(frame_save_dir, str(i).zfill(5) + '.jpg'), frame)
        i += 1
