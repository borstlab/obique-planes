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
All RFs have been centered and cropped such that the center of each cells RF is located at: RFs[5,5,:,120]
The time axis extends from -2 seconds (stimulus history) to +0.5 seconds.
The space axes are in pixels on the area. In elevation, 54 pixels spanned 105 degrees of elevation / 13 cm. 
In azimuth, 64 pixels spanned 180 degrees. 

To obtain the average spatial RF over all cells:
>> numpy.mean(RFs[:,:,:,30],axis = 2)

To obtain the average temporal RF over all cells:
>> numpy.mean(RFs[5,5,:,:], axis = 0)




++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ Dynamic natural scene experiments ++++++++++++++++++++++++++
++++++++++++++++++++++++++++ Figure 5 and Figure S5 ++++++++++++++++++++++++++++++++


#################### translimgs_L2.pkl and translimgs_Mi1.pkl ############################

open with: 
>> pandas.read_pickle('translimgs_L2.pkl')

A pandas hierachical dataframe. 

First level: 	'cells': 	'0', '1', '2', ... n
Second level: 	'imgs': 	'0', '1', '2', ... '9'
Third level: 	'data': 	'mean', 'error', 'trial0', 'trial1', 'trial2'

Index: Time axis. Time point 0 indicates the beginning of the image movement. 

To obtain the mean response of cell 53 to image 5: 
>> df[53][5]['mean']


################### locations_L2.pkl and locations_Mi1.pkl ######################

open with: 
>> pandas.read_pickle('locations_L2.pkl')

A pandas dataframe. 
Columns: 'phi', 'z' # the receptive field locations of each cell in azimuth (phi) and elevation (z)
Rows: Individual cells.

The cell numbers in the index correspond to the cell numbers in the hierachical index of the data (translimgs_L2.pkl ) 
as well as the predictions. 

To retrieve the receptive field location of cell number 53:
>> df[53]


################## predictions_L2.pkl and predictions_Mi1.pkl ###########################

open with: 
>> pandas.read_pickle('predictions_L2.pkl')

A pandas hierachical dataframe analogous to the dataframes containing the data (translimgs_L2.pkl)

First level: 	'cells': 	'0', '1', '2', ... n
Second level: 	'imgs': 	'0', '1', '2', ... '9'
Third level: 	'predictions': 	'Luminance prediction', 'RF prediction'

Index: Time axis. Index 0 is the timepoint of the beginning of the image movement (Time = 0). Index 106 is 
the timepoint of the end of the movement in one direction (Time = 7). 

To retrieve the RF prediction for cell 53 to image 5:
>> df[53][5]['RF prediction']


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++ Static natural scene experiments +++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++ Figure 4 +++++++++++++++++++++++++++++++++++++++++++
