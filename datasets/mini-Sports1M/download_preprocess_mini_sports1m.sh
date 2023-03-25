# download mini-sports1m from dropbox link
wget https://www.dropbox.com/s/7k3it4nblrbtty5/mini_sports1m_videos.tar.gz.part.00?dl=0
wget https://www.dropbox.com/s/0882psclzia96g8/mini_sports1m_videos.tar.gz.part.01?dl=0
wget https://www.dropbox.com/s/5v4ogrfmq7v4vyd/mini_sports1m_videos.tar.gz.part.02?dl=0
wget https://www.dropbox.com/s/n9owzrrbcs7mma2/mini_sports1m_videos.tar.gz.part.03?dl=0
wget https://www.dropbox.com/s/zoaqy79n2axaqtk/mini_sports1m_videos.tar.gz.part.04?dl=0
wget https://www.dropbox.com/s/zzs5jwpxc5xypdz/mini_sports1m_videos.tar.gz.part.05?dl=0
wget https://www.dropbox.com/s/r56zyp6o1m5v43c/mini_sports1m_videos.tar.gz.part.06?dl=0
wget https://www.dropbox.com/s/9l9w6xidg0x9ox5/mini_sports1m_videos.tar.gz.part.07?dl=0
wget https://www.dropbox.com/s/dfu9x5tnbnmycps/mini_sports1m_videos.tar.gz.part.08?dl=0
wget https://www.dropbox.com/s/o5rr7i5eg7skld9/mini_sports1m_videos.tar.gz.part.09?dl=0
wget https://www.dropbox.com/s/f1nynzy7az5oxoo/mini_sports1m_videos.tar.gz.part.10?dl=0
wget https://www.dropbox.com/s/mb0ax1d8kua875d/mini_sports1m_videos.tar.gz.part.11?dl=0
wget https://www.dropbox.com/s/lu4pbxorpvuejbb/mini_sports1m_videos.tar.gz.part.12?dl=0
wget https://www.dropbox.com/s/d3jool60zkjl5n5/mini_sports1m_videos.tar.gz.part.13?dl=0
wget https://www.dropbox.com/s/s18cinmshu0yytf/mini_sports1m_videos.tar.gz.part.14?dl=0

# merge the tar.gz.* file
cat mini_sports1m_videos.tar.gz.part.* | tar -xzvf -

# rename all the videos as xxxxx.mp4
python rename_videos.py
