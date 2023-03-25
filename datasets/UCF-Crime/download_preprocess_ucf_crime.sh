# download files from Dropbox
wget -O Anomaly-Videos-Part-1.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABJtkTnNc8LcVTfH1gE_uFoa/Anomaly-Videos-Part-1.zip?dl=0"
wget -O Anomaly-Videos-Part-2.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABJtkTnNc8LcVTfH1gE_uFoa/Anomaly-Videos-Part-1.zip?dl=0"
wget -O Anomaly-Videos-Part-3.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABJtkTnNc8LcVTfH1gE_uFoa/Anomaly-Videos-Part-1.zip?dl=0"
wget -O Anomaly-Videos-Part-4.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AABJtkTnNc8LcVTfH1gE_uFoa/Anomaly-Videos-Part-1.zip?dl=0"
# wget -O Normal_Videos_for_Event_Recognition.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AACyDI-0oRqqiqUcAulw_x5wa/Normal_Videos_for_Event_Recognition.zip?dl=0"

wget -O Test_Normal_Videos.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AACeDPUxpB6sY2jKgLGzaEdra/Testing_Normal_Videos.zip?dl=0"
wget -O Training-Normal-Videos-Part-1.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AADEUCsLOCN_jHmmx7uFcUhHa/Training-Normal-Videos-Part-1.zip?dl=0"
wget -O Training-Normal-Videos-Part-2.zip "https://www.dropbox.com/sh/75v5ehq4cdg5g5g/AAAHZByMMGCVms4hhHZU2pMBa/Training-Normal-Videos-Part-2.zip?dl=0"

# extract files and delete .zip files
unzip *.zip
rm *.zip

# move all the videos in ./videos/
find . -type f -name "*.mp4" -exec mv {} videos/ \;