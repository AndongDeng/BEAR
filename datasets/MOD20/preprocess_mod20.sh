# extract file
unzip data.zip

# You only need data/dataset which contains all the videos categorized according to its class labels
mv data/dataset/ videos/
mv videos/*/* videos/
rmdir *

# delete other files
rm -rf data/