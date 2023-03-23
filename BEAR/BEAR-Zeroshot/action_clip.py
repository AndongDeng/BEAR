# Code for "ActionCLIP: ActionCLIP: A New Paradigm for Action Recognition"
# arXiv:
# Mengmeng Wang, Jiazheng Xing, Yong Liu

import os
import csv
import action_clip
from tqdm import tqdm
import argparse
from modules.visual_promp import VisualPrompt
import torch
import torch.nn as nn
from dataloader import VideoFolder, default_loader
from torchvision.transforms import *
from utils.utils import accuracy, extract_text_features, get_templates


def validate(val_loader, classes, device, model, fusion_model, num_text_aug):
    model.eval()
    fusion_model.eval()
    num = 0
    corr_1 = 0
    corr_5 = 0

    with torch.no_grad():
        text_inputs = classes.to(device)
        for iii, (image, class_id) in enumerate(tqdm(val_loader)):
            image = image.view((-1, 1, 3) + image.size()[-2:])
            b, t, c, h, w = image.size()
            class_id = class_id.to(device)
            image_input = image.to(device).view(-1, c, h, w)
            image_features = model.encode_image(image_input).view(b, t, -1)
            image_features = fusion_model(image_features)
            image_features /= image_features.norm(dim=-1, keepdim=True)
            text_features /= text_features.norm(dim=-1, keepdim=True)
            similarity = (100.0 * image_features @ text_features.T)
            similarity = similarity.view(b, num_text_aug, -1).softmax(dim=-1)
            similarity = similarity.mean(dim=1, keepdim=False)
            values_1, indices_1 = similarity.topk(1, dim=-1)
            values_5, indices_5 = similarity.topk(5, dim=-1)
            num += b
            for i in range(b):
                if indices_1[i] == class_id[i]:
                    corr_1 += 1
                if class_id[i] in indices_5[i]:
                    corr_5 += 1
    top1 = float(corr_1) / num * 100
    top5 = float(corr_5) / num * 100
    print('Top1: {}, Top5: {}'.format(top1, top5))
    return top1

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Action Video Benchmark: Single-clip CLIP Zero-shot Evaluation')
    parser.add_argument('--dataset', required=True)
    parser.add_argument('--backbone', default='ViT-B/32')
    parser.add_argument('--pretrain', default='checkpoint/vit-32-8f.pt')
    parser.add_argument('--batch_size', default=32)
    parser.add_argument('--num_frame', default=8, type=int)
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
                            nclips=args.num_frame,
                            transform=transform,
                            loader=default_loader)
    else:
        loader = VideoFolder(root="/home/ubuntu/andong/code/CLIP/data/{}/frames/test/".format(args.dataset),
                            csv_file_input="/home/ubuntu/andong/code/CLIP/data/{}/annotations/{}_test.csv".format(args.dataset, args.dataset),
                            csv_file_labels="/home/ubuntu/andong/code/CLIP/data/{}/annotations/labels.csv".format(args.dataset),
                            nclips=args.num_frame,
                            transform=transform,
                            loader=default_loader)
                            
    train_loader = torch.utils.data.DataLoader(
        loader,
        batch_size=args.batch_size, shuffle=False,
        num_workers=args.num_workers, pin_memory=True)

    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, clip_state_dict = action_clip.load(args.backbone, device=device, jit=False, tsm=False, T=1, 
                                       dropout=0., emb_dropout=0.)  # Must set jit=False for training  ViT-B/32
    fusion_model = VisualPrompt('Transf', clip_state_dict, 8)
    fusion_model = nn.DataParallel(fusion_model).to(device)

    if args.pretrain:
        if os.path.isfile(args.pretrain):
            print(("=> loading checkpoint '{}'".format(args.pretrain)))
            checkpoint = torch.load(args.pretrain)
            model.load_state_dict(checkpoint['model_state_dict'])
            fusion_model.load_state_dict(checkpoint['fusion_model_state_dict'])
            del checkpoint
        else:
            print(("=> no checkpoint found at '{}'".format(args.pretrain)))

    labels_file = open("/home/ubuntu/andong/code/CLIP/data/{}/annotations/labels.csv".format(args.dataset), 'r')
    labels_reader = csv.reader(labels_file)
    labels_list = []
    for label in labels_reader:
        labels_list.append(label)

    templates = get_templates(args.dataset)


    with torch.no_grad():
        top1_num = 0
        top5_num = 0
        num = 0
        text_features = extract_text_features(model, labels_list, templates, device)

        for images, labels in tqdm(train_loader):
            images = images.view((-1, args.num_frame, 3) + images.size()[-2:])
            b, t, c, h, w = images.size()
            labels = labels.to(device)
            image_input = images.to(device).view(-1, c, h, w)

            image_features = model.encode_image(image_input).view(b, t, -1)

            image_features = fusion_model(image_features)

            image_features /= image_features.norm(dim=-1, keepdim=True)

            similarity = (100.0 * (image_features @ text_features).squeeze()).softmax(dim=-1)  # [batch, num_class]
            # similarity = similarity.view(-1, args.num_frame, len(labels_list)).mean(1)

    #         values_1, indices_1 = similarity.topk(1, dim=-1)
    #         values_5, indices_5 = similarity.topk(5, dim=-1)
    #         num += b
    #         for i in range(b):
    #             print(indices_1.size(), labels.size())
    #             if indices_1[i] == labels[i]:
    #                 top1_num += 1
    #             if labels[i] in indices_5[i]:
    #                 top5_num += 1
    # top1 = float(top1_num) / num * 100
    # top5 = float(top5_num) / num * 100
    # print('Top1: {}, Top5: {}'.format(top1, top5))

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



