# download the avi videos
wget http://datasets.d2.mpi-inf.mpg.de/MPIICookingActivities/videos.zip

# segment videos according to the temporal annotations
python segment.py
