import numpy as np
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math


GAN_KDE_ratio = np.load('GAN_KDE_ratio.npy')
x_values_bins_limits = np.load('x_values_bins_limits_35.npy')
y_values_bins_limits = np.load('y_values_bins_limits_35.npy')

# print(x_values_bins_limits, np.shape(y_values_bins_limits))
# quit()

p_limit = 350
pt_limit = 6

data = np.empty((0, 3))

for i in range(0, 100):

	for j in range(0 ,100):

		p = (i/100.)*p_limit

		pt = (j/100.)*pt_limit

		# print(p, pt)

		p_index = np.digitize(p, x_values_bins_limits)
		pt_index = np.digitize(pt, y_values_bins_limits)

		# print(p_index-1, pt_index)
		# quit()
		weight = (1/np.fliplr(GAN_KDE_ratio.T)[p_index-1,pt_index-1])*0.97505166029109325 # correction factor obtained with /afs/cern.ch/user/a/amarshal/What_breaks_shield/get_ratio_for_weight_normalisation_35.py script. 
		print(weight)
		data = np.append(data,[[p, pt, weight]],axis=0)


print(np.shape(data))


# cmap = plt.get_cmap('viridis')
# cmap.set_under(color='white')  

plt.scatter(data[:,0], data[:,1],c=data[:,2],norm=LogNorm())
plt.colorbar()
plt.xlabel('pz')
plt.ylabel('p')
# plt.hist(data[:,2],bins=100)
plt.savefig('test_KDE_ratio')




















