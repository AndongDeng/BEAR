import os
import sys
# import cv2
from tqdm import tqdm
from moviepy.editor import VideoFileClip

mode = sys.argv[1]

frame_dir = './frames/{}/'.format(mode)
video_dir = './videos/{}/'.format(mode)

label_file = '{}_label_file.txt'.format(mode)
label_f = open(label_file, 'w')

video_class_list_dir = os.listdir(video_dir)  # list of class ids
for class_id in video_class_list_dir:
    class_video_dir = os.path.join(video_dir, class_id)
    for i, video_name in enumerate(os.listdir(class_video_dir)):
        video_path = os.path.join(class_video_dir, video_name)
        video_index = int(class_id) * 100 + i
        frame_path = os.path.join(frame_dir, str(video_index).zfill(5))
        if not os.path.exists(frame_path):
            os.mkdir(frame_path)
        if len(os.listdir(frame_path)) == 0:
            print('saving frames for video {}'.format(video_index))

        # label_f.write(str(video_index).zfill(5) + ' ' + class_id + '\n')
            # # opencv extract frames
            # cap = cv2.VideoCapture(video_path)
            # length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # take 300 frames in total, evenly sampling
            # # if length > 300:
            # #     freq = length // 300
            # # else:
            # #     print('less than 300 frames')
            # #     freq = 1

            # i = 0
            # count = 0
            # while (cap.isOpened()):
            #     ret, frame = cap.read()
            #     if ret == False:
            #         print('no frame!')
            #         print(video_path)
            #         break
            #     else:
            #         if count % 10 == 0:
            #             save_path = os.path.join(frame_path, str(i).zfill(5) + '.jpg')
            #             # if os.path.exists(save_path):
            #             #     pass
            #             cv2.imwrite(save_path, frame)
            #             if not os.path.exists(save_path):
            #                 print('failed to save frame !')
            #             i += 1
            #             if i > 90000:
            #                 break
            #         count += 1
            # cap.release()

            # moviepy backup
            clip = VideoFileClip(video_path)
            clip.write_images_sequence(os.path.join(frame_path, '%05d.jpg'), fps=3, verbose=False, logger=None)
            print('saved {} frames !'.format(len(os.listdir(frame_path))))





    
        
        







