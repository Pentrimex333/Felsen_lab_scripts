#!/usr/bin/env python
# coding: utf-8

# In[9]:


# this is the final function for the code used to count frames when trials start using an LED light
##################################################################################
# BELOW: Import desired modules, and load csv file as an array called "dlc_data" #       

import os
import numpy as np
import scipy.io as spio

DEF_IMPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"
# You may need to change this default directory if putting csv files in new folder
DEF_EXPORT_DIR = r"C:\Users\Felsenlab\python_work\DeepLabCut_projects\led_csv_files"

print('Welcome to DeepLabCut_Sync! Currently your default import and export directories are:\n\nDEF_IMPORT_DIR = ', DEF_IMPORT_DIR)
print('DEF_EXPORT_DIR = ', DEF_EXPORT_DIR)
print('\nIf you wish to change these directories, please assign a new path (format = r"path") to these variables (excluding file name).')
print('\nThis script contains the following functions: trial_start_frames, convert_frames, and export_mat')
print('\n\nx = dlc_sync.trial_start_frames(file_name) \n\tEnter name of DLC csv file you need for trial start frames as string (include .csv)')
print('\ny = dlc_sync.convert_frames(timestamp_file_name, x) \n\tEnter name of timestamps csv file (include .csv) as string and output(x) of trial_start_frames function')
print('\ndlc_sync.export_mat(export_file_name, MATLAB_name, y) \n\tEnter desired name of MATLAB file (include .mat) as string, desired MATLAB variable name as string,')
print('\tand output(y) from convert_frames function')

def trial_start_frames(file_name, data_dir=None):  #input new file name within folder to start function.
    
    if data_dir is None:     #allows for input of new file name, but stays in path of folder
        data_dir = DEF_IMPORT_DIR
    
    fp = os.path.join(data_dir,file_name)
    try:
        dlc_data = np.loadtxt(fp, delimiter=',',skiprows=3)
    except SyntaxError:
        print('Please supply a raw string of the form r"data_dir"')
        
##############################################################        
# BELOW: Isolate LED likelihood values, turn into a new list #       

    
    led_likelihood_array = dlc_data[:,3:4]    #Need to set to corresponding column in csv file
    
    led_likelihood = []
    for value in np.nditer(led_likelihood_array):
        led_likelihood.append(float(value))
    
#######################################################################################
# BELOW: For loop through led_likelihood and append trial_start_frame list w/ indices # 

    trial_start_frame = []
    cutoff_value = 0.9
    last_value = 0

    for i, value in enumerate(led_likelihood):
        if value > cutoff_value and last_value < cutoff_value:
            trial_start_frame.append(i)
        last_value = value
    
    del trial_start_frame[-1]
        
    return trial_start_frame

##################################################################################################################
# convert_frames = take timestamp.csv and create an array that holds global time of each trial_start_frame value #
##################################################################################################################

def convert_frames(timestamp_fn, trial_start_frame, data_dir=None):   #You have to save trial_start_frames output into variable, then use variable

    #First open timestamp file and convert to array
    if data_dir is None:     #allows for input of new file name, but stays in path of folder
        data_dir = DEF_IMPORT_DIR
    
    fp = os.path.join(data_dir,timestamp_fn)
    try:
        timestamp_array = np.loadtxt(fp, delimiter=',')
    except SyntaxError:
        print('Please supply a raw string of the form r"data_dir"')
        
        
    #Finally, use trial_start_frame output to index timestamp_array and create final array
    trial_start_timestamps = timestamp_array[trial_start_frame]
    
    return trial_start_timestamps    #This is still an array


########################################################################################
# export_mat = take final timestamps array and export to local file as a .mat file #
########################################################################################    

def export_mat(export_fn, mat_name, timestamp_array, export_dir=None): 
    # Need to name MAT file with .mat included (str), within-MATLAB name (str), and variable holding timestamp_array
    
    if export_dir is None:
        export_dir = DEF_EXPORT_DIR
    
    export_fp = os.path.join(export_dir, export_fn)
    spio.savemat(export_fp, mdict={mat_name: timestamp_array})
    
    
    


# In[ ]:




