"""Author = Nahian Chowdhury, MCP/PhD Candidate."""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, gui, parallel, sound
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

actually_send_triggers = True

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'stop_signal_task'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant_id': u'', u'age': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/SST-%s_Session%s_%s' %(expInfo['participant_id'], expInfo['session'], expInfo['date'])  

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.46, 0.46, 0.46], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro_instructions"
intro_instructionsClock = core.Clock()
instructions = visual.TextStim(win=win, ori=0, name='instructions',
    text='You will be performing the same stop signal task as previously.\n\nPress Left Ctrl when you see a left arrow.Press Right Enter when you see a right arrow. Withhold your respond if a blue square appears. \n\nYou will concurrently receive TMS pulses. Try your best to ignore the effect of the pulses, and  keep your focus on the task. \n\nPress space to continue.',    font='Arial',
    pos=[0, 0], height=30, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import random
import string
import numpy as np

# Sounds
correct_sound = sound.Sound(u'sounds/Correct.wav', secs=-1)
correct_sound.setVolume(1.0)
incorrect_sound = sound.Sound(u'sounds/Incorrect.wav', secs=-1)
incorrect_sound.setVolume(1.0)
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='.',    font='Arial',
    pos=[0, 37], height=100, wrapWidth=None,
    color='Black', colorSpace='rgb', opacity=1)
arrow_cue = visual.ImageStim(win=win, name='arrow_cue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[200, 200],
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

if actually_send_triggers:
    from psychopy import parallel
    parallel_trigger = parallel.ParallelPort(address='0xd050')
#    eeg_trigger = parallel.ParallelPort(address='0xcff8')
    parallel_trigger.setData(0)
#    eeg_trigger.setData(0)
prepare_time = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='prepare_time')
stop_signal = visual.Rect(win=win, name='stop_signal',
    width=[60, 60][0], height=[60, 60][1],
    ori=0, pos=[0, 2],
    lineWidth=1, lineColor=[0,0,1], lineColorSpace='rgb',
    fillColor=[0,0,1], fillColorSpace='rgb',
    opacity=1.0,depth=-19.0, 
interpolate=True)


# Initialize components for Routine "break_screen"
break_screenClock = core.Clock()
break_text = visual.TextStim(win=win, ori=0, name='break_text',
    text='Please take a short break to refocus.\n\nWhen you and the experimenter are ready to continue,\nWhen you are ready, the experimenter will move you to the next block of trials. Please remember not to slow down, and to respond to the arrows like you did before',    font='Arial',
    pos=[0, 0], height=30, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "experiment_end"
experiment_endClock = core.Clock()
end_text = visual.TextStim(win=win, ori=0, name='end_text',
    text='That is the end of the experiment,\nthank you for your time.\n\nPress SPACE to exit.',    font='Arial',
    pos=[0, 0], height=30, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "intro_instructions"-------
t = 0
intro_instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_instructions = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_instructions.status = NOT_STARTED
# keep track of which components have finished
intro_instructionsComponents = []
intro_instructionsComponents.append(instructions)
intro_instructionsComponents.append(end_instructions)
for thisComponent in intro_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro_instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = intro_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if t >= 0.0 and instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions.tStart = t  # underestimates by a little under one frame
        instructions.frameNStart = frameN  # exact frame index
        instructions.setAutoDraw(True)
    
    # *end_instructions* updates
    if t >= 0.0 and end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_instructions.tStart = t  # underestimates by a little under one frame
        end_instructions.frameNStart = frameN  # exact frame index
        end_instructions.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro_instructions"-------
for thisComponent in intro_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "intro_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock.keys():
        exec(paramName + '= thisBlock.' + paramName)

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sst_conditionz.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        print(thisTrial)
        for paramName in thisTrial.keys():
            exec(paramName + "= thisTrial['" + paramName + "']")
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + "= thisTrial['" + paramName + "']")
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        arrow_image_filename = 'images/' + thisTrial['arrow_direction'] + '_arrow.png'
        
        trial_end_time = np.random.uniform(6.0, high = 7.0)
       
        # Need to reset the 'sound_played' flag at the start of each
        #   trial
        sound_played = False
        arrow_cue.setOpacity((1 if thisTrial['with_arrow'] == 'yes' else 0))
        arrow_cue.setImage(arrow_image_filename)
        resp_during_arrow = event.BuilderKeyResponse()  # create an object of type KeyResponse
        resp_during_arrow.status = NOT_STARTED
        resp_before_arrow = event.BuilderKeyResponse()  # create an object of type KeyResponse
        resp_before_arrow.status = NOT_STARTED
        resp_after_arrow = event.BuilderKeyResponse()  # create an object of type KeyResponse
        resp_after_arrow.status = NOT_STARTED
        stop_signal.setOpacity((1 if show_stop_signal == 'yes' else 0))
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(fixation)
        trialComponents.append(arrow_cue)
        trialComponents.append(resp_during_arrow)
        trialComponents.append(resp_before_arrow)
        trialComponents.append(resp_after_arrow)
        trialComponents.append(prepare_time)
        trialComponents.append(stop_signal)
        if actually_send_triggers:
            trialComponents.append(parallel_trigger)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        send_trigger = 0 
        #send_trigger = trialTrial.trigger
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            if t > trial_end_time:
                continueRoutine = False
            
            # Either play the correct sound as soon as
            #   they hit the button:
            if thisTrial['show_stop_signal'] == 'no':
                if t > 0.5 and not sound_played:
                    if resp_during_arrow.corr == 1:
                        correct_sound.play()
                        sound_played = True 
                # Or if the arrow is finished, do one last check for
                #   a correct response and then play the incorrect sound
                if t > 2.0 and not sound_played:
                    if resp_during_arrow.corr == 1:
                        correct_sound.play()
                    elif resp_during_arrow.corr == 0:
                        incorrect_sound.play()
                    sound_played = True
            elif thisTrial['show_stop_signal'] == 'yes':
                if t> 2.0 and not sound_played:
                    no_resp_during = len(resp_during_arrow.keys) == 0
                    no_resp_after = len(resp_after_arrow.keys) == 0

                    if no_resp_during and no_resp_after:
                        correct_sound.play()
                        sound_played = True
                    else:
                        incorrect_sound.play()
                        sound_played = True
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t  # underestimates by a little under one frame
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            if fixation.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixation.setAutoDraw(False)
            
            # *arrow_cue* updates
            if t >= 0.5:
                if arrow_cue.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    arrow_cue.tStart = t  # underestimates by a little under one frame
                    arrow_cue.frameNStart = frameN  # exact frame index
                    arrow_cue.setAutoDraw(True)
                    arrow_cue.status == STARTED
            if arrow_cue.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                arrow_cue.setAutoDraw(False)
            
            
            # *resp_during_arrow* updates
            if t >= 0.5 and resp_during_arrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_during_arrow.tStart = t  # underestimates by a little under one frame
                resp_during_arrow.frameNStart = frameN  # exact frame index
                resp_during_arrow.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp_during_arrow.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if resp_during_arrow.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                resp_during_arrow.status = STOPPED
            if resp_during_arrow.status == STARTED:
                theseKeys = event.getKeys(keyList=['lctrl', 'return'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp_during_arrow.keys = theseKeys[-1]  # just the last key pressed
                    resp_during_arrow.rt = resp_during_arrow.clock.getTime()
                    # was this 'correct'?
                    if (resp_during_arrow.keys == str(correct_key)) or (resp_during_arrow.keys == correct_key):
                        resp_during_arrow.corr = 1
                    else:
                        resp_during_arrow.corr = 0
            
            # *resp_before_arrow* updates
            if t >= 0.0 and resp_before_arrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_before_arrow.tStart = t  # underestimates by a little under one frame
                resp_before_arrow.frameNStart = frameN  # exact frame index
                resp_before_arrow.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp_before_arrow.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if resp_before_arrow.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                resp_before_arrow.status = STOPPED
            if resp_before_arrow.status == STARTED:
                theseKeys = event.getKeys(keyList=['lctrl', 'return'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp_before_arrow.keys.extend(theseKeys)  # storing all keys
                    resp_before_arrow.rt.append(resp_before_arrow.clock.getTime())
            
            # *resp_after_arrow* updates
            if t >= 2.0 and resp_after_arrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp_after_arrow.tStart = t  # underestimates by a little under one frame
                resp_after_arrow.frameNStart = frameN  # exact frame index
                resp_after_arrow.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp_after_arrow.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if resp_after_arrow.status == STARTED and t >= (2.0 + ((trial_end_time-2.0)-win.monitorFramePeriod*0.75)): #most of one frame period left
                resp_after_arrow.status = STOPPED
            if resp_after_arrow.status == STARTED:
                theseKeys = event.getKeys(keyList=['lctrl', 'return'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp_after_arrow.keys.extend(theseKeys)  # storing all keys
                    resp_after_arrow.rt.append(resp_after_arrow.clock.getTime())
            # *parallel_trigger* updates
            if actually_send_triggers:
                if t >= (tms_time - 0.01) and parallel_trigger.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    parallel_trigger.tStart = t  # underestimates by a little under one frame
                    parallel_trigger.frameNStart = frameN  # exact frame index
                    parallel_trigger.status = STARTED
                    parallel_trigger.setData(5)
#                    eeg_trigger.setData(8)
                if parallel_trigger.status == STARTED and t >= ((tms_time - 0.01) + (tms_time-win.monitorFramePeriod*0.75)): #most of one frame period left
                    parallel_trigger.status = STOPPED
                    parallel_trigger.setData(0)
#                    eeg_trigger.setData(0)
           
            
            # *stop_signal* updates
            if t >= stop_signal_time and stop_signal.status == NOT_STARTED:
                # keep track of start time/frame for later
                stop_signal.tStart = t  # underestimates by a little under one frame
                stop_signal.frameNStart = frameN  # exact frame index
                stop_signal.setAutoDraw(True)
            
            if stop_signal.status == STARTED and t >= (stop_signal_time + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                stop_signal.setAutoDraw(False)
            # *prepare_time* period
            if t >= 0.05 and prepare_time.status == NOT_STARTED:
                # keep track of start time/frame for later
                prepare_time.tStart = t  # underestimates by a little under one frame
                prepare_time.frameNStart = frameN  # exact frame index
                prepare_time.start(0.1)
            elif prepare_time.status == STARTED: #one frame should pass before updating params and completing
                prepare_time.complete() #finish the static period
            
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if resp_during_arrow.keys in ['', [], None]:  # No response was made
           resp_during_arrow.keys=None
           # was no response the correct answer?!
           if str(correct_key).lower() == 'none': resp_during_arrow.corr = 1  # correct non-response
           else: resp_during_arrow.corr = 0  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('resp_during_arrow.keys',resp_during_arrow.keys)
        trials.addData('resp_during_arrow.corr', resp_during_arrow.corr)
        if resp_during_arrow.keys != None:  # we had a response
            trials.addData('resp_during_arrow.rt', resp_during_arrow.rt)
        # check responses
        if resp_before_arrow.keys in ['', [], None]:  # No response was made
           resp_before_arrow.keys=None
        # store data for trials (TrialHandler)
        trials.addData('resp_before_arrow.keys',resp_before_arrow.keys)
        if resp_before_arrow.keys != None:  # we had a response
            trials.addData('resp_before_arrow.rt', resp_before_arrow.rt)
        # check responses
        if resp_after_arrow.keys in ['', [], None]:  # No response was made
           resp_after_arrow.keys=None
        # store data for trials (TrialHandler)
        trials.addData('resp_after_arrow.keys',resp_after_arrow.keys)
        if resp_after_arrow.keys != None:  # we had a response
            trials.addData('resp_after_arrow.rt', resp_after_arrow.rt)
#        if actually_send_triggers:
#            if thisTrial['trigger'] <=4:
#                eeg_trigger.setData(16 if resp_during_arrow.corr else 17)
#            else:
#                eeg_trigger.setData(18 if resp_during_arrow.corr else 19)
 #           core.wait(0.01)
  #          eeg_trigger.setData(0)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    #------Prepare to start Routine "break_screen"-------
    t = 0
    break_screenClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    wait_for_space = event.BuilderKeyResponse()  # create an object of type KeyResponse
    wait_for_space.status = NOT_STARTED
    
    # keep track of which components have finished
    break_screenComponents = []
    break_screenComponents.append(break_text)
    break_screenComponents.append(wait_for_space)
    for thisComponent in break_screenComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "break_screen"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = break_screenClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if t >= 0.0 and break_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            break_text.tStart = t  # underestimates by a little under one frame
            break_text.frameNStart = frameN  # exact frame index
            break_text.setAutoDraw(True)
        
        # *wait_for_space* updates
        if t >= 0.0 and wait_for_space.status == NOT_STARTED:
            # keep track of start time/frame for later
            wait_for_space.tStart = t  # underestimates by a little under one frame
            wait_for_space.frameNStart = frameN  # exact frame index
            wait_for_space.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if wait_for_space.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        if blocks.thisRepN == blocks.nReps:
            continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "break_screen"-------
    for thisComponent in break_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "break_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3 repeats of 'blocks'


#------Prepare to start Routine "experiment_end"-------
t = 0
experiment_endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
end_press = event.BuilderKeyResponse()  # create an object of type KeyResponse
end_press.status = NOT_STARTED
# keep track of which components have finished
experiment_endComponents = []
experiment_endComponents.append(end_text)
experiment_endComponents.append(end_press)
for thisComponent in experiment_endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "experiment_end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = experiment_endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t  # underestimates by a little under one frame
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    
    # *end_press* updates
    if t >= 0.0 and end_press.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_press.tStart = t  # underestimates by a little under one frame
        end_press.frameNStart = frameN  # exact frame index
        end_press.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_press.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "experiment_end"-------
for thisComponent in experiment_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "experiment_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
