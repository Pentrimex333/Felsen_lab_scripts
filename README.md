# Felsen_lab_scripts
Python scripts made for use in processing/automation/analysis of behavioral and neural data

## dlc_matlab_sync.py
Takes DeepLabCut .csv files, targets frames when LED light comes on, and extracts these to be converted into timestamps that relate to the video. These timestamps are then exported as MATLAB array files that can be synced with other data stored in MATLAB for comprehensive analysis of behavioral experiments by trial.

## bpod_mix2afc.py
Recreates a previous MATLAB code used by the lab to run a mixed 2AFC odor discrimination task for mice. The task has not only been converted from MATLAB to Python, but also now uses a Bpod system rather than Linux to run the RTLSM. Key note: Uses state machine to ensure accurate timing between states.
