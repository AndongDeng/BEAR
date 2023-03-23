import os
import json
import cv2


def video_to_frames(video_path, frame_save_path, size=None):
    """
    video_path -> str, path to video.
    size -> (int, int), width, height.
    """

    cap = cv2.VideoCapture(video_path)

    i = 1
    while True:
        ret, frame = cap.read()
    
        if ret:
            if size:
                frame = cv2.resize(frame, size)
            cv2.imwrite(os.path.join(frame_save_path, str(i).zfill(5) + '.jpg'), frame)
        else:
            break
        i += 1

    cap.release()


if __name__ == '__main__':

    root = os.getcwd()
    frame_dir = os.path.join(root, 'frames/')
    video_dir = os.path.join(root, 'videos/')

    video_list_dir = os.listdir(video_dir)

    for video_id in video_list_dir:
        video_path = os.path.join(video_dir, video_id)
        frame_save_path = os.path.join(frame_dir, video_id.split('.')[0])
        if not os.path.exists(frame_save_path):
            os.mkdir(frame_save_path)
        video_to_frames(video_path, frame_save_path)
        print('Video {} has been extracted to frames.'.format(video_id.split('.')[0]))
        




