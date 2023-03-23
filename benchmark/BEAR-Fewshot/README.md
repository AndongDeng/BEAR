# BEAR-FewShot

Compared with standard finetuning where abundant annotations can be utilized, few-shot learning is of more practical significance since annotating massive amounts of videos is notoriously expensive. To extend the investigation mentioned, we thoroughly investigate the capability of the selected 6 models on BEAR under few-shot setting given both supervised and self-supervised pre-trained weights. Specifically, we consider (2,4,8,16)-shot settings, and for each setting, we randomly generate 3 splits and report the mean and standard deviation. Due to space constraints, we only select TSM, 3D NonLocal, and Video Swin to represent each model type for illustration as they perform generally better. 


## Introduction

The training pipeline of few-shot learning is the same as the standard finetuning. You only need to replace the full annotations as the train_${SHOT}.csv [here](../finetuning/data/). We provide an example of VideoSwin training here.

```
CKPT=$1
MODE=$2

for DATA in mini_sports1m mini_hacs coin xd_violence wlasl mod20 meccano inhard petraw misaw uav_human mpii_cooking toyota_smarthome fine_gym charades_ego muvim jester ucf_crime
do
	for SHOT in 2 4 8 16
	do
		bash tools/dist_train.sh configs/datasets/$DATA/swin_base_patch244_window877_8x16_$DATA.py 8  \ 
        --validate \ 
        --cfg-options load_from=$CKPT \ 
                      data_root=data/$DATA/frames/ \ 
                      data_root_val=data/$DATA/frames/ \  
                      data.train.ann_file=data/${DATA}/annotations/train_${SHOT}.csv  \ 
                      data.train.data_prefix=data/$DATA/frames/  \ 
                      data.val.data_prefix=data/$DATA/frames/  \ 
                      data.test.data_prefix=data/$DATA/frames/  \ 
                      work_dir=/home/ubuntu/data16T/ssl_fewshot_work_dirs/swin/${SHOT}shot/${DATA}_8frame/  \ 
                      log_config.interval=2 \ 
                      checkpoint_config.interval=5 \ 
	done
done
```