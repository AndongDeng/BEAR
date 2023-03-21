# download the original CharadesEGO videos to ./data/CharadesEGO/
wget https://ai2-public-datasets.s3-us-west-2.amazonaws.com/charades/CharadesEgo_v1.tar

# extract videos from .tar file
tar -xvf CharadesEgo_v1.tar

# delete the .tar file
rm CharadesEgo_v1.tar

# segment original videos according to the temporal annotation and save the processed videos to ./data/ChradesEGO/videos/
python segment_charadesego.py train
python segment_charadesego.py test

# delete the original videos if needed
rm -rf CharadesEgo_v1/