# merge the tar.gz.* file
cat mini_sports1m_videos.tar.gz.part.* | tar -xzvf -

# rename all the videos as xxxxx.mp4
python rename_videos.py
