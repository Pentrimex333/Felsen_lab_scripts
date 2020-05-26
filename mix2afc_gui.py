from tkinter import *

# Create a base GUI that can edit values in bpod_mix2afc.py

main_window = Tk()
main_window.title("Bpod Mix2AFC Program")

#Create Entry boxes for each parameter that should be changeable.
### Trial Parameters ###
trialParameterFrame = LabelFrame(main_window, text="Trial Parameters",
                                   padx=5, pady=5)
trialParameterFrame.grid(row=0, column=0, padx=10, pady=10)

itiMean_input = Entry(trialParameterFrame)
itiMean_label = Label(trialParameterFrame, text="ITI Mean:")
itiMean_input.insert(0, "1")
itiMean_label.grid(row=0, column=0)
itiMean_input.grid(row=0, column=1)

itiStdDev_input = Entry(trialParameterFrame)
itiStdDev_label = Label(trialParameterFrame, text="ITI Std Dev:")
itiStdDev_input.insert(0, "0.1")
itiStdDev_label.grid(row=1, column=0)
itiStdDev_input.grid(row=1, column=1)

errorPenalty_input = Entry(trialParameterFrame)
errorPenalty_label = Label(trialParameterFrame, text="Error Penalty:")
errorPenalty_input.insert(0, "2")
errorPenalty_label.grid(row=2, column=0)
errorPenalty_input.grid(row=2, column=1)

inEarlyPenalty_input = Entry(trialParameterFrame)
inEarlyPenalty_label = Label(trialParameterFrame, text="In Early Penalty:")
inEarlyPenalty_input.insert(0, "0.5")
inEarlyPenalty_label.grid(row=3, column=0)
inEarlyPenalty_input.grid(row=3, column=1)

outEarlyPenalty_input = Entry(trialParameterFrame)
outEarlyPenalty_label = Label(trialParameterFrame, text="Out Early Penalty:")
outEarlyPenalty_input.insert(0, "2")
outEarlyPenalty_label.grid(row=4, column=0)
outEarlyPenalty_input.grid(row=4, column=1)

trialLength_input = Entry(trialParameterFrame)
trialLength_label = Label(trialParameterFrame, text="Trial Length:")
trialLength_input.insert(0, "45")
trialLength_label.grid(row=5, column=0)
trialLength_input.grid(row=5, column=1)

totalNumtrials_input = Entry(trialParameterFrame)
totalNumtrials_label = Label(trialParameterFrame, text="Number of Trials:")
totalNumtrials_input.insert(0, "1000")
totalNumtrials_label.grid(row=6, column=0)
totalNumtrials_input.grid(row=6, column=1)

### Odor Parameters ###
odorParameterFrame = LabelFrame(main_window, text="Odor Parameters",
                                   padx=5, pady=5)
odorParameterFrame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

minOdorDelay_input = Entry(odorParameterFrame)
minOdorDelay_label = Label(odorParameterFrame, text="Min Odor Delay:")
minOdorDelay_input.insert(0, "0.2")
minOdorDelay_label.grid(row=0, column=0)
minOdorDelay_input.grid(row=0, column=1)

maxOdorDelay_input = Entry(odorParameterFrame)
maxOdorDelay_label = Label(odorParameterFrame, text="Max Odor Delay:")
maxOdorDelay_input.insert(0, "0.4")
maxOdorDelay_label.grid(row=1, column=0)
maxOdorDelay_input.grid(row=1, column=1)

odor_delay_input = Entry(odorParameterFrame)
odor_delay_label = Label(odorParameterFrame, text="Odor Delay:")
odor_delay_input.insert(0, "1")
odor_delay_label.grid(row=2, column=0)
odor_delay_input.grid(row=2, column=1)

odor_sampletime_input = Entry(odorParameterFrame)
odor_sampletime_label = Label(odorParameterFrame, text="Odor Sample Time:")
odor_sampletime_input.insert(0, "0.55")
odor_sampletime_label.grid(row=3, column=0)
odor_sampletime_input.grid(row=3, column=1)

odor_sampletimerange_input = Entry(odorParameterFrame)
odor_sampletimerange_label = Label(odorParameterFrame, text="Sample Time Range:")
odor_sampletimerange_input.insert(0, "0.055")
odor_sampletimerange_label.grid(row=4, column=0)
odor_sampletimerange_input.grid(row=4, column=1)

# Odor Weights Section #
odorWeights_label = Label(odorParameterFrame, text="Current Odor Weights")
odorWeights_label.grid(row=5, column=0, columnspan=2, pady=10)

input_95left = Entry(odorParameterFrame)
label_95left = Label(odorParameterFrame, text="95/5 Left:")
input_95left.insert(0, "0.5")
label_95left.grid(row=6, column=0)
input_95left.grid(row=6, column=1)

input_80left = Entry(odorParameterFrame)
label_80left = Label(odorParameterFrame, text="80/20 Left:")
input_80left.insert(0, "1")
label_80left.grid(row=7, column=0)
input_80left.grid(row=7, column=1)

input_60left = Entry(odorParameterFrame)
label_60left = Label(odorParameterFrame, text="60/40 Left:")
input_60left.insert(0, "2")
label_60left.grid(row=8, column=0)
input_60left.grid(row=8, column=1)

input_5050 = Entry(odorParameterFrame)
label_5050 = Label(odorParameterFrame, text="50/50 Mix:")
input_5050.insert(0, "2")
label_5050.grid(row=9, column=0)
input_5050.grid(row=9, column=1)

input_40right = Entry(odorParameterFrame)
label_40right = Label(odorParameterFrame, text="40/60 Right:")
input_40right.insert(0, "2")
label_40right.grid(row=10, column=0)
input_40right.grid(row=10, column=1)

input_20right = Entry(odorParameterFrame)
label_20right = Label(odorParameterFrame, text="20/80 Right:")
input_20right.insert(0, "1")
label_20right.grid(row=11, column=0)
input_20right.grid(row=11, column=1)

input_05right = Entry(odorParameterFrame)
label_05right = Label(odorParameterFrame, text="5/95 Right:")
input_05right.insert(0, "0.5")
label_05right.grid(row=12, column=0)
input_05right.grid(row=12, column=1)

### Reward Parameters ###
rewardParameterFrame = LabelFrame(main_window, text="Reward Parameters",
                                   padx=5, pady=5)
rewardParameterFrame.grid(row=1, column=0, padx=10, pady=10)

minRewardDelay_input = Entry(rewardParameterFrame)
minRewardDelay_label = Label(rewardParameterFrame, text="Min Reward Delay:")
minRewardDelay_input.insert(0, "0.1")
minRewardDelay_label.grid(row=0, column=0)
minRewardDelay_input.grid(row=0, column=1)

maxRewardDelay_input = Entry(rewardParameterFrame)
maxRewardDelay_label = Label(rewardParameterFrame, text="Max Reward Delay:")
maxRewardDelay_input.insert(0, "0.1")
maxRewardDelay_label.grid(row=1, column=0)
maxRewardDelay_input.grid(row=1, column=1)

rewardDelay_input = Entry(rewardParameterFrame)
rewardDelay_label = Label(rewardParameterFrame, text="Reward Delay:")
rewardDelay_input.insert(0, "1")
rewardDelay_label.grid(row=2, column=0)
rewardDelay_input.grid(row=2, column=1)

rewardAvailability_input = Entry(rewardParameterFrame)
rewardAvailability_label = Label(rewardParameterFrame, text="Reward Availability:")
rewardAvailability_input.insert(0, "5")
rewardAvailability_label.grid(row=3, column=0)
rewardAvailability_input.grid(row=3, column=1)

leftRewardAmt_uL_input = Entry(rewardParameterFrame)
leftRewardAmt_label = Label(rewardParameterFrame, text="Left Reward (uL):")
leftRewardAmt_uL_input.insert(0, "5")
leftRewardAmt_label.grid(row=4, column=0)
leftRewardAmt_uL_input.grid(row=4, column=1)

rightRewardAmt_uL_input = Entry(rewardParameterFrame)
rightRewardAmt_label = Label(rewardParameterFrame, text="Right Reward (uL):")
rightRewardAmt_uL_input.insert(0, "5")
rightRewardAmt_label.grid(row=5, column=0)
rightRewardAmt_uL_input.grid(row=5, column=1)

#Will also require a display that shows correct choice for each trial,
#whether previous choices were correct, and also updates future trials
#(but also keeps old trial info) if odor parameters are changed.





