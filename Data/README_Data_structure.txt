This file contains documentation for how the data for the publication SEEING NATURAL IMAGES THROUGH THE 
EYE OF A FLY WITH REMOTE FOCUSING TWO-PHOTON MICROSCOPY (2020) is structured. 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++ White noise experiments +++++++++++++++++++++++++++++
+++++++++++++++++++++++ Figure 3, Figure S3 and Figure S4 ++++++++++++++++++++++++


#################### RFdata_L2.pkl and RFdata_Mi1.pkl ############################

open with: 
>> pandas.read_pickle('RFdata_L2.pkl')

Each row contains data from an individual cell. 
The relevant columns are:
- "zscore"  			The z-score of the RF center pixel 
- "centers_i_fitted [deg]"	The coordinates of the RF center location in azimuth in degrees
- "centers_j_fitted [deg]"	The coordinates of the RF center location in elevation in degrees
- "sigmas_i [deg]"
- "sigmas_j [deg]"

################# centeredRFs_L2.npy and centeredRFs_Mi1.npy ####################

open with: 
>> RFs = numpy.load('centeredRFs_L2.npy')

A numpy array of the size (azimuth x elevation x cell_number x time) or (11x11xcell_numberx150)
All RFs have been centered and cropped such that the center of each cells RF is located at: RFs[5,5,:,30]

To obtain the average spatial RF over all cells:
>> numpy.mean(RFs[:,:,:,30],axis = 2)

To obtain the average temporal RF over all cells:
>> numpy.mean(RFs[5,5,:,:], axis = 0)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ Static natural scene experiments +++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++ Figure 4 +++++++++++++++++++++++++++++++++++++++++++


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ Dynamic natural scene experiments ++++++++++++++++++++++++++
++++++++++++++++++++++++++++ Figure 5 and Figure S5 ++++++++++++++++++++++++++++++++