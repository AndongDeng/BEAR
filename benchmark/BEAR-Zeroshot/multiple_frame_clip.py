import os
import csv
import glob
import numpy as np
import torch
from tqdm import tqdm
import argparse

from PIL import Image
from torchvision.transforms import *

import clip

from dataloader import VideoFolder, default_loader
from utils.utils import accuracy, extract_text_features, get_templates


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Action Video Benchmark: Multiple-clip CLIP Zero-shot Evaluation')
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--num_clip', default=3, type=int)
    parser.add_argument('--backbone', default='ViT-B/32')
    parser.add_argument('--batch_size', default=32)
    parser.add_argument('--num_workers', default=8)
    args = parser.parse_args()

    transform = Compose([
                        Resize(224, interpolation=3),
                        CenterCrop((224, 224)),
                        ToTensor(),
                        Normalize(
                            mean=[0.48145466, 0.4578275, 0.40821073],
                            std=[0.26862954, 0.26130258, 0.27577711])
                        ])
    if args.dataset in ['ucf101', 'ucf_crime', 'wlasl', 'jester', 'uav_human', 'toyota_smarthome', 'mpii_cooking', 'muvim', 'charades_ego']:
        loader = VideoFolder(root="/home/ubuntu/andong/code/CLIP/data/{}/frames/".format(args.dataset),
                            csv_file_input="/home/ubuntu/andong/code/CLIP/data/{}/annotations/{}_test.csv".format(args.dataset, args.dataset),
                            csv_file_labels="/home/ubuntu/andong/code/CLIP/data/{}/annotations/labels.csv".format(args.dataset),
                            nclips=args.num_clip,
                            transform=transform,
                            loader=default_loader)
    else:
        loader = VideoFolder(root="/home/ubuntu/andong/code/CLIP/data/{}/frames/test/".format(args.dataset),
                            csv_file_input="/home/ubuntu/andong/code/CLIP/data/{}/annotations/{}_test.csv".format(args.dataset, args.dataset),
                            csv_file_labels="/home/ubuntu/andong/code/CLIP/data/{}/annotations/labels.csv".format(args.dataset),
                            nclips=args.num_clip,
                            transform=transform,
                            loader=default_loader)


    train_loader = torch.utils.data.DataLoader(
        loader,
        batch_size=args.batch_size, shuffle=True,
        num_workers=args.num_workers, pin_memory=True)

    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load(args.backbone, device)

    labels_file = open("/home/ubuntu/andong/code/CLIP/data/{}/annotations/labels.csv".format(args.dataset), 'r')
    labels_reader = csv.reader(labels_file)
    labels_list = []
    for label in labels_reader:
        labels_list.append(label)

    templates = get_templates(args.dataset)

    with torch.no_grad():
        top1_num = 0
        top5_num = 0        

        text_features = extract_text_features(model, labels_list, templates, device)

        for images, labels in tqdm(train_loader):
            images = images.to(device) # [batch_size, C, N, H, W] e.g., [32, 3, 5, 224, 224]
            sim_list = []
            for i in range(args.num_clip):
                images_i = images[:, :, i, :, :] # [bs*N, C, 224, 224]

                labels = labels.to(device)
                image_features = model.encode_image(images_i)  # [bs*N, dim]
                image_features /= image_features.norm()

                similarity = (100.0 * (image_features @ text_features).squeeze()).softmax(dim=-1)  # [batch*N, num_class]
                sim_list.append(similarity)
            similarity = torch.stack(sim_list, 0).mean(0)

            if args.dataset == 'muvim':
                acc1_num = accuracy(similarity, labels, (1, ))[0]
                top1_num += acc1_num
            else:
                acc1_num, acc5_num = accuracy(similarity, labels, (1, 5))
                top1_num += acc1_num
                top5_num += acc5_num
        
        print('Top1 Acc: {}%'.format(top1_num * 100 / len(loader)))
        if args.dataset != 'muvim':
            print('Top5 Acc: {}%'.format(top5_num * 100 / len(loader)))