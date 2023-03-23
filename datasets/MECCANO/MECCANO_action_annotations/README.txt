This README is related to the following scientific paper:
    
F. Ragusa, A. Furnari, G. M. Farinella. MECCANO: A Multimodal Egocentric Dataset for Humans Behavior Understanding in the Industrial-like Domain. 2022.

More information is available at our web page: http://iplab.dmi.unict.it/MECCANO 

In the folder there are the temporal annotations of the 61 action classes related to the MECCANO Dataset.
You will find 3 .csv files one for each subset of the MECCANO (Training, Validation and Test).

Each instance of the .csv file is composed of 5 fields as explained in the PySlowfast framework:

	- video_id which represents the video of the MECCANO Dataset (from 0001 to 0020) where the specific clip has been extracted;
	- action_id which represents the ID of the action class related to the clip;
	- action_name which represents the action label associated to the verb ID;
	- start_frame which is the name of the frame where the action starts;
	- end_frame which is the name of the frame where the action ends. 