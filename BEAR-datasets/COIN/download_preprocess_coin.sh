# download coin raw videos with officially provided python script
python download_videos.py

# segment clips of interests according to the temporal annotations and save them under ./videos
python segment_coin.py

# delete the original coin videos
rm -rf raw_coin_videos/