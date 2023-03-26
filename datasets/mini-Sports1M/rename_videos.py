import os


def rename(video_root):
    class_id_list = os.listdir(video_root)
    for class_id in class_id_list:
        video_name_list = os.listdir(os.path.join(video_root, class_id))
        for video_name in video_name_list:
            video_id = video_name.split('_')[0]
            new_name = video_id + '.mp4'
            old_path = os.path.join(video_root, class_id, video_name)
            new_path = os.path.join(video_root, class_id, new_name)
            os.rename(old_path, new_path)


if __name__ == '__main__':

    train_root = 'videos/train/'
    test_root = 'videos/test'

    rename(train_root)
    rename(test_root)

