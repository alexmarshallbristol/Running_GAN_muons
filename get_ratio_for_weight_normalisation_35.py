import numpy as np
import matplotlib as mpl
mpl.use('TkAgg') 
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
from matplotlib.colors import LogNorm
import random
import glob 

ratio = np.load('GAN_KDE_ratio.npy')
x_values_bins_limits = np.load('x_values_bins_limits_35.npy')
y_values_bins_limits = np.load('y_values_bins_limits_35.npy')

total_muons_seen = 0
total_weight_of_muons_seen = 0

counter = -1 

files = glob.glob('/eos/experiment/ship/user/amarshal/HUGE_GAN_random_id/*')

# for x in range(0, 100):
for file in files:
	counter += 1
	if counter == 100:
		quit()

	current = np.load(file)

	# total_mom = buffer_mom[0][1]+buffer_mom[0][2]+buffer_mom[0][3]
	# trans_mom = math.sqrt(buffer_mom[0][1]**2+buffer_mom[0][2]**2)
	p = np.add(current[:,4], current[:,5])
	p = np.add(p, current[:,6])
	p_t = np.sqrt(np.add(current[:,4]**2,current[:,5]**2))


	# start_momentum_data_gan = np.append(start_momentum_data_gan,[[total_mom,trans_mom]],axis=0)
	
	p_index = np.digitize(p, x_values_bins_limits)
	pt_index = np.digitize(p_t, y_values_bins_limits)


	# p_index = np.digitize(total_mom, x_values_bins_limits)
	# pt_index = np.digitize(math.sqrt(buffer_mom[0][1]**2+buffer_mom[0][2]**2), y_values_bins_limits)

	# weight = 1/np.flip(ratio.T,axis=1)[p_index,pt_index]
	weight = 1/np.fliplr(ratio.T)[p_index-1,pt_index-1]

	# print(weight)

	total_weight_of_muons_seen += np.sum(weight)
	total_muons_seen += np.shape(current)[0]
 
	print('after',counter,'constant:',1/(total_weight_of_muons_seen/total_muons_seen))




