import glob
import numpy as np

list_of_files = glob.glob('/eos/experiment/ship/user/amarshal/HUGE_GAN_random_id/*')

list_of_files = [element[76:85] for element in list_of_files]

print(list_of_files, np.shape(list_of_files))

np.save('list_of_file_ID',list_of_files)