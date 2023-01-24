import os
import sys
import json


data_info = json.load(open('finegym_annotation_info_v1.0.json', 'r'))
raw_video_root = './raw/'
if not os.path.exists(raw_video_root):
    os.mkdir(raw_video_root)

for url, annotations in data_info.items():
    # download the raw videos
    destination = os.path.join(raw_video_root, url)
    youtube_dl_cmd = 'yt-dlp ' + url + ' -o ' + destination
    os.system(youtube_dl_cmd)
    if os.path.exists(destination):
        print('Succesfully download video {} !!!'.format(url))


    # for event_name, event_content in annotations.items():
    #     event_id = event_content['event']
    #     seg_infos = event_content['segments']
    #     abs_timestamps = event_content['timestamps'][0]

    #     if seg_infos:
    #         for sub_action_id, sub_content in seg_infos.items():
    #             stage = sub_content['stages']
    #             rel_timestamps = sub_content['timestamps']
    #             e = rel_timestamps[0][-1]
    #             for i, t in enumerate(rel_timestamps):
    #                 if i == 1:
    #                     s = t[0]
    #                     if s != e:
    #                         print(event_name, sub_action_id)
                # print(rel_timestamps)

