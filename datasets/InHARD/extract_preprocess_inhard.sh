# extract the raw videos from 12 .7z files
7za x 01-InHARD.7z.001

# only keep ./Segmented/RGBSegmented/ which contains all the segmented RGB videos
mv ./Segmented/RGBSegmented/ ./videos

# delete other files if you do not need them
rm -rf ./Online/
rm -rf ./Segmented/