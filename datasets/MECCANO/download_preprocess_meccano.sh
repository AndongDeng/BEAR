# download the RGB videos
wget https://iplab.dmi.unict.it/sharing/MECCANO/MECCANO_RGB_Videos.zip

# unzip .zip file
unzip MECCANO_RGB_Videos.zip

# rename files
mv MECCANO_RGB_Videos/ raw_meccano_videos/

# segment videos according to the temporal annotations
python segment_meccano.py

# delete the raw videos if neccessay
rm -rf raw_meccano_videos/