# MUVIM

### [Paper](https://arxiv.org/pdf/2206.12740.pdf)

MUVIM  (Multi Visual Modality Fall Detection Dataset) is a recently released fall detection dataset, which consists of visual data from multiple sensors: infrared, depth, RGB, and thermal cameras. Considering the data consistency, we only utilize their RGB version. The original data is used for detection; we use it for a binary classification task.

## Download and preprocessing

### 1. Download videos

- The dataset has not officially released yet. To obtain the dataset, contact the author bing.ye@utoronto.ca for the access. Usually, you can obtain the download instruction in three days. 

- The instructions can be as follows:

    Before you do anything, install and connect to the Cisco AnyConnect VPN:  https://isea.utoronto.ca/services/vpn/utorvpn/users/.  This link includes installation and configuration instructions.  In brief, you’ll be installing Cisco AnyConnect, and connecting to general.vpn.utoronto.ca.  Note that you’ll use your personal UTORid and password to connect to the VPN. 

    (UTORid: xxxx    Password: xxxx)

    You’ll need to connect using Cisco AnyConnect each time before connecting to the server – it makes it look like you’re on UofT campus.
    
    Once you’re connected to the VPN, you can connect to the server on a Mac machine (similar procedure on a Linux system):
    
    • Go to Finder and click on Go – Connect to Server
    • In that box, type smb://142.1.143.130/iatsl/FallDetection_36744/Data2Share and click Connect
    • When prompted, use the username xxxx and the password:  xxxx (This is different from UTORid)

- Then you can see all the content in the shown folder, and you only need to obtain `ZED_RGB/`

    <div align="center">
        <img src="download.jpeg">
    </div>

- Put all data under:  `./data/MUVIM/videos`

- Run the following command: 
    ```
    bash prerpocess_muvim.sh
    ```
