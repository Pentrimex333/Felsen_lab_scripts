# First draft outline of Python BPOD-mix2afc module

#Call Bpod and StateMachine from pybpodapi.protocol
from pybpodapi.protocol import Bpod, StateMachine
from random import choices, randint, triangular, gauss

# set the serial port from which the Bpod runs,
# then set Bpod to variable my_bpod
serial_port='' #add serial port location when ready
my_bpod = Bpod(serial_port)

###########################################################################
      # Set Default Parameters for use in states and main function #
###########################################################################

# Trial Parameters #
itiMean = 1
itiStdDev = 0.1
errorPenalty = 2
inEarlyPenalty = 0.5
outEarlyPenalty = 2
#trialLength = 45    #Not currently in use
totalNumtrials = 1000

# Odor Parameters #
minOdorDelay = 0.2
maxOdorDelay = 0.4
odor_delay = 1
odor_sample_time = 0.55
odor_sample_time_range = 0.055

# Reward Parameters #
minRewardDelay = 0.1
maxRewardDelay = 0.1
rewardDelay = 1
rewardAvailability = 5
leftRewardAmt_uL = 5
leftValveTime_sec = 1 #value will change with calibration
rightRewardAmt_uL = 5
rightValveTime_sec = 1 #value will change with calibration

# Current Values #
ITI_Value = 1
TrialNumber = 1
GoMode = 5 #look into
CurrentBlock = 1
PortOutRegDelay = 0.5 #NOT CURRENTLY USED  #How long mouse must remain
                      #out of port before returning
reward_delay = 1
lite = 'On'
timeBeforeCenterPoke = 40

# Odor Fractions #
odor95_fraction = 1
odor05_fraction = 1
odor80_fraction = 0
odor20_fraction = 0
odor60_fraction = 0
odor40_fraction = 0
odor50_fraction = 1
##GUI materials might need to be attached to these values later on##

CurrentBlock = 1
PortOutRegDelay = 0.5
timeBeforeCenterPoke = 40

###########################################################################
                         # Define Trials #
###########################################################################

# Define trial type for each possible behavioral response, and create
# a list of future trial types for a session.

# NOTE: Left_choice = 1, Right_choice = 2

valveNumbers = [1,2,3,4,5,6,7] #Valve 0 is pure oil mix (empty odor)
odorFractions = [
    odor95_fraction,
    odor05_fraction,
    odor80_fraction,
    odor20_fraction,
    odor60_fraction,
    odor40_fraction,
    odor50_fraction] #Odors aligned to valveNumbers in manner similar to
# the freely-moving boxes

odorFractionsPrev = odorFractions #Copy of odorFractions for GUI changes
# May not need this initially until adding GUI

# odorTypes is the list created that decides what odors will be delivered
# on which trials (based on valve number)
odorTypes = choices(valveNumbers, odorFractions, k = totalNumtrials)

#TrialTypes is the list of correct answers (1 or 2) for each trial
TrialTypes = [0] * totalNumtrials #List of zeros

# This for loop produces the completed TrialTypes list based on odorTypes
for i, valve in enumerate(odorTypes):
    if valve in (1,3,5):
        TrialTypes[i] = 1
    elif valve in (2,4,6):
        TrialTypes[i] = 2
    elif valve == 7:
        TrialTypes[i] = randint(0,4)

# iti_times and delay_times can also be randomized and filled into a list 
delay_times = [0] * totalNumtrials
iti_times = [0] * totalNumtrials
reward_delay_times = [0] * totalNumtrials
odor_sample_times = [0] * totalNumtrials

#delay_times use minOdorDelay * factor between 1-2 randomized by triangular
for i, time in enumerate(delay_times):
    r_num = triangular(1.0, 2.0)    #Factor to multiply minimum odor delay time
    delay_times[i] = r_num * minOdorDelay

#iti_times simply use function 'gauss' and apply iti_mean and iti_StdDev
for i, time in enumerate(iti_times):
    gauss_num = gauss(itiMean, itiStdDev)
    iti_times[i] = gauss_num

#reward_delay_times (Not as vital since we don't fluctuate reward time at moment)
for i, time in enumerate(reward_delay_times):
    reward_time = triangular(minRewardDelay,maxRewardDelay)
    reward_delay_times[i] = reward_time

#odor_sample_times (replaces req_time)
for i, time in enumerate(odor_sample_times):
    time_range = triangular((-1*odor_sample_time_range), odor_sample_time_range)
    odor_sample_times[i] = odor_sample_time + time_range

###########################################################################
                          # MAIN TRIAL LOOP #
###########################################################################

#Start a for loop that runs for each trial, prints current trial number
for trial in range(0, totalNumtrials):
    trial_num = trial+1
    print("Starting Trial Number",trial_num)

    # For each trial, collect the necessary values from each list per trial
    trial_iti_time = iti_times[trial]
    trial_odor_delay = delay_times[trial]
    trial_odor_sample = odor_sample_times[trial]
    trial_reward_time = reward_delay_times[trial]

    #Will need to remake to allow for adjustments of reward based on calibration
    #and GUI interface, but for now just use standard values

    #Checking for odor updates since last trial (Need GUI again)
    #if odorFractions != odorFractionsPrev:
        #update the current trial, then update OdorFractionsPrev
    
    #Now begin state machine
    sma = StateMachine(my_bpod)
    #May also need to set a global timer (learn this later)

    #Now build parameters for each trialtype based on TrialType value for current trial
    thisTrialType = TrialTypes[trial]

    if thisTrialType == 0:   #Null trial; both sides won't reward mouse
        leftPokeTimer = 10
        leftPoke_SCCs = {'Port1Out': 'completed_state'}
        leftRewardTimer = 0
        leftReward_SCCs = {}
        leftRewardOutput = {}

        rightPokeTimer = 10
        rightPoke_SCCs = {'Port3Out': 'completed_state'}
        rightRewardTimer = 0
        rightReward_SCCs = {}
        rightRewardOutput = {}

        valveNumber = 1

    elif thisTrialType == 1:    #Left poke is correct
        leftPokeTimer = trial_reward_time
        leftPoke_SCCs = {'Port1Out': 'omission_state', 'Tup': 'l_reward'}
        leftRewardTimer = leftValveTime_sec
        leftReward_SCCs = {'Port1Out': 'final_state', 'Tup': 'final_state'}
        leftRewardOutput = {'ValveState': 1}

        rightPokeTimer = -0.01
        rightPoke_SCCs = {'Port3Out': 'l_error_state', 'Tup': 'l_error_state'}
        rightRewardTimer = 10    #Check on this? Seems wrong
        rightReward_SCCs = {}
        rightRewardOutput = {}

        valveNumber = 2

    elif thisTrialType == 2:    #Right poke is correct
        leftPokeTimer = -0.01
        leftPoke_SCCs = {'Port1Out': 'r_error_state', 'Tup': 'r_error_state'}
        leftRewardTimer = 10    #Check on this? Seems wrong
        leftReward_SCCs = {}
        leftRewardOutput = {}

        rightPokeTimer = trial_reward_time
        rightPoke_SCCs = {'Port3Out': 'omission_state', 'Tup': 'r_reward'}
        rightRewardTimer = rightValveTime_sec
        rightReward_SCCs = {'Port3Out': 'final_state', 'Tup': 'final_state'}
        rightRewardOutput = {'ValveState': 4}

        valveNumber = 3

    elif thisTrialType == 3:    #Either side is correct
        leftPokeTimer = trial_reward_time
        leftPoke_SCCs = {'Port1Out': 'omission_state', 'Tup': 'l_reward'}
        leftRewardTimer = leftValveTime_sec
        leftReward_SCCs = {'Port1Out': 'final_state', 'Tup': 'final_state'}
        leftRewardOutput = {'ValveState': 1}

        rightPokeTimer = trial_reward_time
        rightPoke_SCCs = {'Port3Out': 'omission_state', 'Tup': 'r_reward'}
        rightRewardTimer = rightValveTime_sec
        rightReward_SCCs = {'Port3Out': 'final_state', 'Tup': 'final_state'}
        rightRewardOutput = {'ValveState': 4}

        valveNumber = 4

    else:
        print('Invalid trial type selected; look into the code')
        break

###########################################################################
                          # Matrix Setup #
###########################################################################
# These states are actually built into the for loop, so you can use for loop
# variables to carry settings and times for current trial.

#Special states for LED lite being on: light_delay and light_penalty
    if lite == 'On' or lite == 'On - Rx Time' or lite == 'beep & light':
        sma.add_state(
            state_name = 'light_delay',
            state_timer= trial_iti_time,
            state_change_conditions = {'Port2In':'light_penalty',
                                       'Port3Out':'light_penalty',
                                       'Tup':'port_entry'},
            output_actions = [])
        sma.add_state(
            state_name = 'light_penalty',
            state_timer = inEarlyPenalty,
            state_change_conditions = {'Tup':'light_delay'},
            output_actions = [])

#Now the starting state machines that begin the trial
    sma.add_state(
        state_name = 'port_entry',
        state_timer = timeBeforeCenterPoke,
        state_change_conditions = {'Port2In':'c_poke',
                                   'Tup':'omission_state'},
        output_actions = [(Bpod.OutputChannels.PWM2, 126)])
    sma.add_state(
        state_name = 'c_poke',
        state_timer = trial_odor_delay,
        state_change_conditions = {'Port2Out':'flash_state',
                                   'Tup':'odor_del1'},
        output_actions = [(Bpod.OutputChannels.PWM2, 255)])

###########################################################################
                      # Odor Delivery Section #
###########################################################################

#Still in the for loop
#Odor Delivery state machines depend on lite being on or off
    if lite == 'On' or lite == 'light flash' or lite == 'beep & light' or lite == 'beep':
        sma.add_state(
            state_name = 'odor_del1',
            state_timer = trial_odor_sample,  #Needs to be adjusted to include odor_del2
            state_change_conditions = {'Port2Out':'flash_state',
                                       'Tup':'odor_del2'},
            output_actions = [(Bpod.OutputChannels.PWM1, 255),(Bpod.OutputChannels.GlobalTimerTrig, 1)])
    elif lite == 'Off - Rx Time' or lite == 'On - Rx Time':
        sma.add_state(
            state_name = 'odor_del1',
            state_timer = trial_odor_sample,
            state_change_conditions = {'Port2Out':'lr_poke',
                                       'Tup':'odor_del2'},
            output_actions = [(Bpod.OutputChannels.PWM1, 255),(Bpod.OutputChannels.GlobalTimerTrig, 1)])
    elif lite == '':
        sma.add_state(
            state_name = 'odor_del1',
            state_timer = trial_odor_sample,  #Needs to be adjusted to include odor_del2
            state_change_conditions = {'Port2Out':'flash_state',
                                       'Tup':'odor_del2'},
            output_actions = [(Bpod.OutputChannels.PWM1, 255),(Bpod.OutputChannels.GlobalTimerTrig, 1)])
    else:
        print('Error: No valid option specified for Lite GUI')

    sma.add_state(
        state_name = 'odor_del2',
        state_timer = 1 - trial_odor_sample,
        #Needs to be adjusted so both odor_del = odor_sample_times[trial]
        state_change_conditions = {'Port2Out':'lr_poke',
                                       'Tup':'lr_poke'},
        output_actions = [(Bpod.OutputChannels.PWM3, 255)])

###########################################################################
                    # Choice/Reward/Penalty Section #
###########################################################################

    sma.add_state(
        state_name = 'lr_poke',
        state_timer = rewardAvailability,
        state_change_conditions = {'Port1In':'l_poke',
                                   'Port3In':'r_poke',
                                   'Tup':'omission_state'},
        output_actions = [])
    
    sma.add_state(
        state_name = 'l_poke',
        state_timer = leftPokeTimer,
        state_change_conditions = leftPoke_SCCs,
        output_actions = [])

    sma.add_state(
        state_name = 'r_poke',
        state_timer = rightPokeTimer,
        state_change_conditions = rightPoke_SCCs,
        output_actions = [])

    sma.add_state(
        state_name = 'l_reward',
        state_timer = leftRewardTimer,
        state_change_conditions = leftReward_SCCs,
        output_actions = leftRewardOutput)

    sma.add_state(
        state_name = 'r_reward',
        state_timer = rightRewardTimer,
        state_change_conditions = rightReward_SCCs,
        output_actions = rightRewardOutput)

###########################################################################
                        # Flash Penalty State #
###########################################################################

    sma.add_state(
        state_name = 'flash_state',
        state_timer = -0.01,
        state_change_conditions = {'Tup':'flash_on'},
        output_actions = [(Bpod.OutputChannels.GlobalTimerTrig, 2)])

    sma.add_state(
        state_name = 'flash_on',
        state_timer = 0.1,
        state_change_conditions = {'Tup':'flash_off',
                                   'Port2In':'oe_pen',
                                   'GlobalTimer1_End':'oe_pen'},
        output_actions = [(Bpod.OutputChannels.PWM2, 255)])
    
    sma.add_state(
        state_name = 'flash_off',
        state_timer = 0.1,
        state_change_conditions = {'Tup':'flash_on',
                                   'Port2In':'oe_pen',
                                   'GlobalTimer2_End':'oe_pen'},
        output_actions = [])

    sma.add_state(
        state_name = 'oe_pen',
        state_timer = outEarlyPenalty,
        state_change_conditions = {'Tup':'final_state'},
        output_actions = [])

###########################################################################
                          # Omission State #
###########################################################################

    sma.add_state(
        state_name = 'omission_state',
        state_timer = -0.01,
        state_change_conditions = {'Tup':'final_state'},
        output_actions = [])

###########################################################################
                          # Completed State #
###########################################################################

    sma.add_state(
        state_name = 'completed_state',
        state_timer = -0.01,
        state_change_conditions = {'Tup':'final_state'},
        output_actions = [])

###########################################################################
                            # Error State #
###########################################################################

    sma.add_state(
        state_name = 'r_error_state',
        state_timer = errorPenalty,
        state_change_conditions = {'Tup':'final_state'},
        output_actions = [])

    sma.add_state(
        state_name = 'l_error_state',
        state_timer = errorPenalty,
        state_change_conditions = {'Tup':'final_state'},
        output_actions = [])

###########################################################################
                             # Final State #
###########################################################################

    if lite == 'On' or lite == 'On - Rx Time' or lite == 'beep & light':
        sma.add_state(
            state_name = 'final_state',
            state_timer = -0.01,
            state_change_conditions = {'Tup':'exit'},
            output_actions = [])
    else:
        sma.add_state(
            state_name = 'final_state',
            state_timer = trial_iti_time,
            state_change_conditions = {'Tup':'exit'},
            output_actions = [])

###########################################################################

#Send state machine descriptions to Bpod, then run state machine
    my_bpod.send_state_machine(sma)
    my_bpod.run_state_machine(sma)

    print('Current trial info: ', my_bpod.session.current_trial)

#Now state machine will run through for loop, but must close once for loop ends
my_bpod.close()
                        
                        
