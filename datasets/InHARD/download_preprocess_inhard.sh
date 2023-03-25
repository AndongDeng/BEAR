# download all .7z.* files
wget -O 01-InHARD.7z.001 "https://zenodo.org/record/4003541/files/01-InHARD.7z.001?download=1"
wget -O 01-InHARD.7z.002 "https://zenodo.org/record/4003541/files/01-InHARD.7z.002?download=1"
wget -O 01-InHARD.7z.003 "https://zenodo.org/record/4003541/files/01-InHARD.7z.003?download=1"
wget -O 01-InHARD.7z.004 "https://zenodo.org/record/4003541/files/01-InHARD.7z.004?download=1"
wget -O 01-InHARD.7z.005 "https://zenodo.org/record/4003541/files/01-InHARD.7z.005?download=1"
wget -O 01-InHARD.7z.006 "https://zenodo.org/record/4003541/files/01-InHARD.7z.006?download=1"
wget -O 01-InHARD.7z.007 "https://zenodo.org/record/4003541/files/01-InHARD.7z.007?download=1"
wget -O 01-InHARD.7z.008 "https://zenodo.org/record/4003541/files/01-InHARD.7z.008?download=1"
wget -O 01-InHARD.7z.009 "https://zenodo.org/record/4003541/files/01-InHARD.7z.009?download=1"
wget -O 01-InHARD.7z.000 "https://zenodo.org/record/4003541/files/01-InHARD.7z.010?download=1"
wget -O 01-InHARD.7z.011 "https://zenodo.org/record/4003541/files/01-InHARD.7z.011?download=1"
wget -O 01-InHARD.7z.012 "https://zenodo.org/record/4003541/files/01-InHARD.7z.012?download=1"

# extract the raw videos from 12 .7z files
7za x 01-InHARD.7z.001

# only keep ./Segmented/RGBSegmented/ which contains all the segmented RGB videos
mv ./Segmented/RGBSegmented/ ./videos

# delete other files if you do not need them
rm -rf ./Online/
rm -rf ./Segmented/
rm 01-Inhard.7z.*