import os
import glob
import csv
import numpy as np
import torch
from collections import namedtuple

from PIL import Image
from torchvision.transforms import *


IMG_EXTENSIONS = ['.jpg', '.JPG', '.jpeg', '.JPEG']
ListDataJpeg = namedtuple('ListDataJpeg', ['id', 'label', 'path'])


class JpegDataset(object):

    def __init__(self, 
                 csv_path_input, 
                 csv_path_labels, 
                 data_root):

        self.classes = self.read_csv_labels(csv_path_labels)
        self.classes_dict = self.get_two_way_dict(self.classes)
        self.csv_data = self.read_csv_input(csv_path_input, data_root)

    def read_csv_input(self, csv_path, data_root):
        csv_data = []
        with open(csv_path) as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=';')
            for row in csv_reader:
                item = ListDataJpeg(row[0],
                                    row[1],
                                    os.path.join(data_root, row[0])
                                    )
                if row[1] in self.classes:
                    csv_data.append(item)
        return csv_data

    def read_csv_labels(self, csv_path):
        classes = []
        with open(csv_path) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                classes.append(row[0])
        return classes

    def get_two_way_dict(self, classes):
        classes_dict = {}
        for i, item in enumerate(classes):
            classes_dict[item] = i
            classes_dict[i] = item
        return classes_dict


def default_loader(path):
    return Image.open(path).convert('RGB')


class VideoFolder(torch.utils.data.Dataset):

    def __init__(self, 
                 root, 
                 csv_file_input, 
                 csv_file_labels,
                 nclips, 
                 transform=None,
                 loader=default_loader):
        self.dataset_object = JpegDataset(csv_file_input, csv_file_labels, root)

        self.csv_data = self.dataset_object.csv_data
        self.classes = self.dataset_object.classes
        self.classes_dict = self.dataset_object.classes_dict
        self.root = root
        self.transform = transform
        self.loader = loader

        self.nclips = nclips

    def __getitem__(self, index):
        item = self.csv_data[index]
        img_paths = self.get_frame_names(item.path)

        imgs = []
        for img_path in img_paths:
            img = self.loader(img_path)
            img = self.transform(img)
            imgs.append(torch.unsqueeze(img, 0))

        target_idx = self.classes_dict[item.label]

        # format data to torch
        data = torch.cat(imgs)
        data = data.permute(1, 0, 2, 3)
        return (data, target_idx)

    def __len__(self):
        return len(self.csv_data)

    def get_frame_names(self, path):
        frame_names = []
        for ext in IMG_EXTENSIONS:
            frame_names.extend(glob.glob(os.path.join(path, "*" + ext)))
        frame_names = list(sorted(frame_names))
        num_frames = len(frame_names)  # total frames number
        num_frames_necessary = self.nclips

        # pick frames
        if num_frames_necessary > num_frames:
            # pad last frame if video is shorter than necessary
            frame_names += [frame_names[-1]] * (num_frames_necessary - num_frames)
        step_size = len(frame_names) // (num_frames_necessary + 1)
        frame_names = frame_names[step_size: len(frame_names): step_size]
        frame_names = frame_names[: self.nclips]
        return frame_names
