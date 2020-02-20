#!/usr/bin/env python
# coding: utf-8

# In[6]:


# this is the final function for the code used to count frames when trials start using an LED light
##################################################################################
# BELOW: Import desired modules, and load csv file as an array called "dlc_data" #       

import os
import numpy as np
import scipy.io as spio

DEF_IMPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"
# You may need to change this default directory if putting csv files in new folder
DEF_EXPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"

def trial_start_frames(dlc_fn, data_dir=None):  #input new file name within folder to start function.
    
    if data_dir is None:     #allows for input of new file name, but stays in path of folder
        data_dir = DEF_IMPORT_DIR
    
    fp = os.path.join(data_dir, dlc_fn)
    try:
        dlc_data = np.loadtxt(fp, delimiter=',',skiprows=3)
    except SyntaxError:
        print('Please supply a raw string of the form r"data_dir"')
        
        
# BELOW: Isolate LED likelihood values, turn into a new list        

    
    led_likelihood_array = dlc_data[:,3:4]    #Need to set to corresponding column in csv file
    
    led_likelihood = []
    for value in np.nditer(led_likelihood_array):
        led_likelihood.append(float(value))
    

# BELOW: For loop through led_likelihood and append trial_start_frame list w/ indices 

    trial_start_frame = []
    cutoff_value = 0.9
    last_value = 0

    for i, value in enumerate(led_likelihood):
        if value > cutoff_value and last_value < cutoff_value:
            trial_start_frame.append(i)
        last_value = value
    
    del trial_start_frame[-1]
        
    return trial_start_frame


# In[7]:


##################################################################################################################
# convert_frames = take timestamp.csv and create an array that holds global time of each trial_start_frame value #
##################################################################################################################

def convert_frames(dlc_fn, timestamp_fn, data_dir=None):   #You have to save trial_start_frames output into variable, then use variable
    
    tsf_output = trial_start_frames(dlc_fn)    # Run trial_start_frames function through convert_frames to get output
    
    #Open timestamp file and convert to array
    if data_dir is None:     #allows for input of new file name, but stays in path of folder
        data_dir = DEF_IMPORT_DIR
    
    fp = os.path.join(data_dir,timestamp_fn)
    try:
        timestamp_array = np.loadtxt(fp, delimiter=',')
    except SyntaxError:
        print('Please supply a raw string of the form r"data_dir"')
        
        
    #Finally, use trial_start_frames output to index timestamp_array and create final array
    trial_start_timestamps = timestamp_array[tsf_output]
    
    return trial_start_timestamps    #This is still an array


# In[8]:


####################################################################################
# export_mat = take final timestamps array and export to local file as a .mat file #
####################################################################################    

def export_mat(dlc_fn, timestamp_fn, export_fn, mat_name, export_dir=None): 
    # Need to name MAT file with .mat included (str), within-MATLAB name (str), and variable holding timestamp_array
    
    timestamp_output = convert_frames(dlc_fn, timestamp_fn)
    if export_dir is None:
        export_dir = DEF_EXPORT_DIR
    
    export_fp = os.path.join(export_dir, export_fn)
    spio.savemat(export_fp, mdict={mat_name: timestamp_output})


# In[10]:


###############################################################
# main = combine all functions above into one function #    
###############################################################

def main():
    import os
    import numpy as np
    import scipy.io as spio

    DEF_IMPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"
    # You may need to change this default directory if putting csv files in new folder
    DEF_EXPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"

    print('Welcome to DeepLabCut_Sync! Currently your default import and export directories are:\n\nDEF_IMPORT_DIR = ', DEF_IMPORT_DIR)
    print('DEF_EXPORT_DIR = ', DEF_EXPORT_DIR)
    print('\nIf you wish to change these directories, please assign a new path (format = r"path") to these variables (excluding file name).')
    
    
    just_dlc_fn = input('Enter DLC csv file name: ')
    dlc_fn = just_dlc_fn + '.csv'
    just_timestamp_fn = input('Enter timestamps csv file name: ')
    timestamp_fn = just_timestamp_fn + '.csv'
    just_export_fn = input('Enter the desired name of MATLAB file: ')
    export_fn = just_export_fn + '.mat'
    mat_name = input('Enter variable name of array in your MATLAB file: ')
    
    export_mat(dlc_fn, timestamp_fn, export_fn, mat_name)
    
    
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




