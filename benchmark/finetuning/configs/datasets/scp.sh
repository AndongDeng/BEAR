for DATA in coin xd_violence wlasl mod20 meccano inhard petraw misaw uav_human mini_hacs mini_sports1m mpii_cooking toyota_smarthome fine_gym charades_ego muvim ucf_crime jester
do
	scp -r ubuntu@3.250.24.239:/home/ubuntu/andong/code/Video-Swin-Transformer/config/benchmark/datasets/$DATA/* $DATA/
done
