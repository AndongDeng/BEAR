# download raw videos to ./raw_finegym_videos/
python download.py

# segment videos according to the temporal annotation and save them to ./videos/
python segment_finegym.py

# you can delete the raw videos if you need
rm -rf raw_finegym_videos/

