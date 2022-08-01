#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Feb  1 15:01:31 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Jack_PsychoPy'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jackcrosby/Desktop/Jack_PsychoPy/Jack_PsychoPy.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "GUI"
GUIClock = core.Clock()
Green_1 = visual.ImageStim(
    win=win,
    name='Green_1', 
    image='/Users/jackcrosby/Desktop/Jack_PsychoPy/Green_1.png', mask=None,
    ori=0.0, pos=(-0.6, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
submit_button = visual.ButtonStim(win, 
    text='Submit', font='Arvo',
    pos=(0.6, -0.45),
    letterHeight=0.05,
    size=(0.25,0.1), borderWidth=0.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='submit_button'
)
submit_button.buttonClock = core.Clock()
Green_2 = visual.ImageStim(
    win=win,
    name='Green_2', 
    image='Green_2.png', mask=None,
    ori=0.0, pos=(-0.45, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Green_3 = visual.ImageStim(
    win=win,
    name='Green_3', 
    image='Green_3.png', mask=None,
    ori=0.0, pos=(-0.3, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Green_4 = visual.ImageStim(
    win=win,
    name='Green_4', 
    image='Green_4.png', mask=None,
    ori=0.0, pos=(-0.15, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
Green_5 = visual.ImageStim(
    win=win,
    name='Green_5', 
    image='Green_5.png', mask=None,
    ori=0.0, pos=(0.0, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
Green_6 = visual.ImageStim(
    win=win,
    name='Green_6', 
    image='Green_6.png', mask=None,
    ori=0.0, pos=(0.15, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
Green_7 = visual.ImageStim(
    win=win,
    name='Green_7', 
    image='Green_7.png', mask=None,
    ori=0.0, pos=(0.3, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
Green_8 = visual.ImageStim(
    win=win,
    name='Green_8', 
    image='Green_8.png', mask=None,
    ori=0.0, pos=(0.45, -0.2), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
White_1 = visual.ImageStim(
    win=win,
    name='White_1', 
    image='White_1.png', mask=None,
    ori=0.0, pos=(-0.6, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
White_2 = visual.ImageStim(
    win=win,
    name='White_2', 
    image='White_2.png', mask=None,
    ori=0.0, pos=(-0.45, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
White_3 = visual.ImageStim(
    win=win,
    name='White_3', 
    image='White_3.png', mask=None,
    ori=0.0, pos=(-0.3, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
White_4 = visual.ImageStim(
    win=win,
    name='White_4', 
    image='White_4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
White_5 = visual.ImageStim(
    win=win,
    name='White_5', 
    image='White_5.png', mask=None,
    ori=0.0, pos=(0.1.5, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
White_6 = visual.ImageStim(
    win=win,
    name='White_6', 
    image='White_6.png', mask=None,
    ori=0.0, pos=(0.0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
White_7 = visual.ImageStim(
    win=win,
    name='White_7', 
    image='White_7.png', mask=None,
    ori=0.0, pos=(0.15, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
White_8 = visual.ImageStim(
    win=win,
    name='White_8', 
    image='White_8.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
Red_1 = visual.ImageStim(
    win=win,
    name='Red_1', 
    image='Red_1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
Red_2 = visual.ImageStim(
    win=win,
    name='Red_2', 
    image='Red_2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
Red_3 = visual.ImageStim(
    win=win,
    name='Red_3', 
    image='Red_3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
Red_4 = visual.ImageStim(
    win=win,
    name='Red_4', 
    image='Red_4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
Red_5 = visual.ImageStim(
    win=win,
    name='Red_5', 
    image='Red_5.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
Red_6 = visual.ImageStim(
    win=win,
    name='Red_6', 
    image='Red_6.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
Red_7 = visual.ImageStim(
    win=win,
    name='Red_7', 
    image='Red_7.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
Red_8 = visual.ImageStim(
    win=win,
    name='Red_8', 
    image='Red_8.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
Blue_1 = visual.ImageStim(
    win=win,
    name='Blue_1', 
    image='Blue_1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
Blue_2 = visual.ImageStim(
    win=win,
    name='Blue_2', 
    image='Blue_2.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
Blue_3 = visual.ImageStim(
    win=win,
    name='Blue_3', 
    image='Blue_3.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
Blue_4 = visual.ImageStim(
    win=win,
    name='Blue_4', 
    image='Blue_4.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-29.0)
Blue_5 = visual.ImageStim(
    win=win,
    name='Blue_5', 
    image='Blue_5.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-30.0)
Blue_6 = visual.ImageStim(
    win=win,
    name='Blue_6', 
    image='Blue_6.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-31.0)
Blue_7 = visual.ImageStim(
    win=win,
    name='Blue_7', 
    image='Blue_7.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-32.0)
Blue_8 = visual.ImageStim(
    win=win,
    name='Blue_8', 
    image='Blue_8.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-33.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "GUI"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
GUIComponents = [Green_1, mouse, submit_button, Green_2, Green_3, Green_4, Green_5, Green_6, Green_7, Green_8, White_1, White_2, White_3, White_4, White_5, White_6, White_7, White_8, Red_1, Red_2, Red_3, Red_4, Red_5, Red_6, Red_7, Red_8, Blue_1, Blue_2, Blue_3, Blue_4, Blue_5, Blue_6, Blue_7, Blue_8]
for thisComponent in GUIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GUIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "GUI"-------
while continueRoutine:
    # get current time
    t = GUIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GUIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Green_1* updates
    if Green_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_1.frameNStart = frameN  # exact frame index
        Green_1.tStart = t  # local t and not account for scr refresh
        Green_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_1, 'tStartRefresh')  # time at next scr refresh
        Green_1.setAutoDraw(True)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
    
    # *submit_button* updates
    if submit_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        submit_button.frameNStart = frameN  # exact frame index
        submit_button.tStart = t  # local t and not account for scr refresh
        submit_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit_button, 'tStartRefresh')  # time at next scr refresh
        submit_button.setAutoDraw(True)
    if submit_button.status == STARTED:
        # check whether submit_button has been pressed
        if submit_button.isClicked:
            if not submit_button.wasClicked:
                submit_button.timesOn.append(submit_button.buttonClock.getTime()) # store time of first click
                submit_button.timesOff.append(submit_button.buttonClock.getTime()) # store time clicked until
            else:
                submit_button.timesOff[-1] = submit_button.buttonClock.getTime() # update time clicked until
            if not submit_button.wasClicked:
                continueRoutine = False  # end routine when submit_button is clicked
                None
            submit_button.wasClicked = True  # if submit_button is still clicked next frame, it is not a new click
        else:
            submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
    else:
        submit_button.wasClicked = False  # if submit_button is clicked next frame, it is a new click
    
    # *Green_2* updates
    if Green_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_2.frameNStart = frameN  # exact frame index
        Green_2.tStart = t  # local t and not account for scr refresh
        Green_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_2, 'tStartRefresh')  # time at next scr refresh
        Green_2.setAutoDraw(True)
    
    # *Green_3* updates
    if Green_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_3.frameNStart = frameN  # exact frame index
        Green_3.tStart = t  # local t and not account for scr refresh
        Green_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_3, 'tStartRefresh')  # time at next scr refresh
        Green_3.setAutoDraw(True)
    
    # *Green_4* updates
    if Green_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_4.frameNStart = frameN  # exact frame index
        Green_4.tStart = t  # local t and not account for scr refresh
        Green_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_4, 'tStartRefresh')  # time at next scr refresh
        Green_4.setAutoDraw(True)
    
    # *Green_5* updates
    if Green_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_5.frameNStart = frameN  # exact frame index
        Green_5.tStart = t  # local t and not account for scr refresh
        Green_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_5, 'tStartRefresh')  # time at next scr refresh
        Green_5.setAutoDraw(True)
    
    # *Green_6* updates
    if Green_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_6.frameNStart = frameN  # exact frame index
        Green_6.tStart = t  # local t and not account for scr refresh
        Green_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_6, 'tStartRefresh')  # time at next scr refresh
        Green_6.setAutoDraw(True)
    
    # *Green_7* updates
    if Green_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_7.frameNStart = frameN  # exact frame index
        Green_7.tStart = t  # local t and not account for scr refresh
        Green_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_7, 'tStartRefresh')  # time at next scr refresh
        Green_7.setAutoDraw(True)
    
    # *Green_8* updates
    if Green_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Green_8.frameNStart = frameN  # exact frame index
        Green_8.tStart = t  # local t and not account for scr refresh
        Green_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Green_8, 'tStartRefresh')  # time at next scr refresh
        Green_8.setAutoDraw(True)
    
    # *White_1* updates
    if White_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_1.frameNStart = frameN  # exact frame index
        White_1.tStart = t  # local t and not account for scr refresh
        White_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_1, 'tStartRefresh')  # time at next scr refresh
        White_1.setAutoDraw(True)
    
    # *White_2* updates
    if White_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_2.frameNStart = frameN  # exact frame index
        White_2.tStart = t  # local t and not account for scr refresh
        White_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_2, 'tStartRefresh')  # time at next scr refresh
        White_2.setAutoDraw(True)
    
    # *White_3* updates
    if White_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_3.frameNStart = frameN  # exact frame index
        White_3.tStart = t  # local t and not account for scr refresh
        White_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_3, 'tStartRefresh')  # time at next scr refresh
        White_3.setAutoDraw(True)
    
    # *White_4* updates
    if White_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_4.frameNStart = frameN  # exact frame index
        White_4.tStart = t  # local t and not account for scr refresh
        White_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_4, 'tStartRefresh')  # time at next scr refresh
        White_4.setAutoDraw(True)
    
    # *White_5* updates
    if White_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_5.frameNStart = frameN  # exact frame index
        White_5.tStart = t  # local t and not account for scr refresh
        White_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_5, 'tStartRefresh')  # time at next scr refresh
        White_5.setAutoDraw(True)
    
    # *White_6* updates
    if White_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_6.frameNStart = frameN  # exact frame index
        White_6.tStart = t  # local t and not account for scr refresh
        White_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_6, 'tStartRefresh')  # time at next scr refresh
        White_6.setAutoDraw(True)
    
    # *White_7* updates
    if White_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_7.frameNStart = frameN  # exact frame index
        White_7.tStart = t  # local t and not account for scr refresh
        White_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_7, 'tStartRefresh')  # time at next scr refresh
        White_7.setAutoDraw(True)
    
    # *White_8* updates
    if White_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        White_8.frameNStart = frameN  # exact frame index
        White_8.tStart = t  # local t and not account for scr refresh
        White_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(White_8, 'tStartRefresh')  # time at next scr refresh
        White_8.setAutoDraw(True)
    
    # *Red_1* updates
    if Red_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_1.frameNStart = frameN  # exact frame index
        Red_1.tStart = t  # local t and not account for scr refresh
        Red_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_1, 'tStartRefresh')  # time at next scr refresh
        Red_1.setAutoDraw(True)
    
    # *Red_2* updates
    if Red_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_2.frameNStart = frameN  # exact frame index
        Red_2.tStart = t  # local t and not account for scr refresh
        Red_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_2, 'tStartRefresh')  # time at next scr refresh
        Red_2.setAutoDraw(True)
    
    # *Red_3* updates
    if Red_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_3.frameNStart = frameN  # exact frame index
        Red_3.tStart = t  # local t and not account for scr refresh
        Red_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_3, 'tStartRefresh')  # time at next scr refresh
        Red_3.setAutoDraw(True)
    
    # *Red_4* updates
    if Red_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_4.frameNStart = frameN  # exact frame index
        Red_4.tStart = t  # local t and not account for scr refresh
        Red_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_4, 'tStartRefresh')  # time at next scr refresh
        Red_4.setAutoDraw(True)
    
    # *Red_5* updates
    if Red_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_5.frameNStart = frameN  # exact frame index
        Red_5.tStart = t  # local t and not account for scr refresh
        Red_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_5, 'tStartRefresh')  # time at next scr refresh
        Red_5.setAutoDraw(True)
    
    # *Red_6* updates
    if Red_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_6.frameNStart = frameN  # exact frame index
        Red_6.tStart = t  # local t and not account for scr refresh
        Red_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_6, 'tStartRefresh')  # time at next scr refresh
        Red_6.setAutoDraw(True)
    
    # *Red_7* updates
    if Red_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_7.frameNStart = frameN  # exact frame index
        Red_7.tStart = t  # local t and not account for scr refresh
        Red_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_7, 'tStartRefresh')  # time at next scr refresh
        Red_7.setAutoDraw(True)
    
    # *Red_8* updates
    if Red_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Red_8.frameNStart = frameN  # exact frame index
        Red_8.tStart = t  # local t and not account for scr refresh
        Red_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Red_8, 'tStartRefresh')  # time at next scr refresh
        Red_8.setAutoDraw(True)
    
    # *Blue_1* updates
    if Blue_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_1.frameNStart = frameN  # exact frame index
        Blue_1.tStart = t  # local t and not account for scr refresh
        Blue_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_1, 'tStartRefresh')  # time at next scr refresh
        Blue_1.setAutoDraw(True)
    
    # *Blue_2* updates
    if Blue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_2.frameNStart = frameN  # exact frame index
        Blue_2.tStart = t  # local t and not account for scr refresh
        Blue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_2, 'tStartRefresh')  # time at next scr refresh
        Blue_2.setAutoDraw(True)
    
    # *Blue_3* updates
    if Blue_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_3.frameNStart = frameN  # exact frame index
        Blue_3.tStart = t  # local t and not account for scr refresh
        Blue_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_3, 'tStartRefresh')  # time at next scr refresh
        Blue_3.setAutoDraw(True)
    
    # *Blue_4* updates
    if Blue_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_4.frameNStart = frameN  # exact frame index
        Blue_4.tStart = t  # local t and not account for scr refresh
        Blue_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_4, 'tStartRefresh')  # time at next scr refresh
        Blue_4.setAutoDraw(True)
    
    # *Blue_5* updates
    if Blue_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_5.frameNStart = frameN  # exact frame index
        Blue_5.tStart = t  # local t and not account for scr refresh
        Blue_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_5, 'tStartRefresh')  # time at next scr refresh
        Blue_5.setAutoDraw(True)
    
    # *Blue_6* updates
    if Blue_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_6.frameNStart = frameN  # exact frame index
        Blue_6.tStart = t  # local t and not account for scr refresh
        Blue_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_6, 'tStartRefresh')  # time at next scr refresh
        Blue_6.setAutoDraw(True)
    
    # *Blue_7* updates
    if Blue_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_7.frameNStart = frameN  # exact frame index
        Blue_7.tStart = t  # local t and not account for scr refresh
        Blue_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_7, 'tStartRefresh')  # time at next scr refresh
        Blue_7.setAutoDraw(True)
    
    # *Blue_8* updates
    if Blue_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Blue_8.frameNStart = frameN  # exact frame index
        Blue_8.tStart = t  # local t and not account for scr refresh
        Blue_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Blue_8, 'tStartRefresh')  # time at next scr refresh
        Blue_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GUIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "GUI"-------
for thisComponent in GUIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Green_1.started', Green_1.tStartRefresh)
thisExp.addData('Green_1.stopped', Green_1.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.x', mouse.x)
thisExp.addData('mouse.y', mouse.y)
thisExp.addData('mouse.leftButton', mouse.leftButton)
thisExp.addData('mouse.midButton', mouse.midButton)
thisExp.addData('mouse.rightButton', mouse.rightButton)
thisExp.addData('mouse.time', mouse.time)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('submit_button.started', submit_button.tStartRefresh)
thisExp.addData('submit_button.stopped', submit_button.tStopRefresh)
thisExp.addData('submit_button.numClicks', submit_button.numClicks)
if submit_button.numClicks:
   thisExp.addData('submit_button.timesOn', submit_button.timesOn)
   thisExp.addData('submit_button.timesOff', submit_button.timesOff)
else:
   thisExp.addData('submit_button.timesOn', "")
   thisExp.addData('submit_button.timesOff', "")
thisExp.addData('Green_2.started', Green_2.tStartRefresh)
thisExp.addData('Green_2.stopped', Green_2.tStopRefresh)
thisExp.addData('Green_3.started', Green_3.tStartRefresh)
thisExp.addData('Green_3.stopped', Green_3.tStopRefresh)
thisExp.addData('Green_4.started', Green_4.tStartRefresh)
thisExp.addData('Green_4.stopped', Green_4.tStopRefresh)
thisExp.addData('Green_5.started', Green_5.tStartRefresh)
thisExp.addData('Green_5.stopped', Green_5.tStopRefresh)
thisExp.addData('Green_6.started', Green_6.tStartRefresh)
thisExp.addData('Green_6.stopped', Green_6.tStopRefresh)
thisExp.addData('Green_7.started', Green_7.tStartRefresh)
thisExp.addData('Green_7.stopped', Green_7.tStopRefresh)
thisExp.addData('Green_8.started', Green_8.tStartRefresh)
thisExp.addData('Green_8.stopped', Green_8.tStopRefresh)
thisExp.addData('White_1.started', White_1.tStartRefresh)
thisExp.addData('White_1.stopped', White_1.tStopRefresh)
thisExp.addData('White_2.started', White_2.tStartRefresh)
thisExp.addData('White_2.stopped', White_2.tStopRefresh)
thisExp.addData('White_3.started', White_3.tStartRefresh)
thisExp.addData('White_3.stopped', White_3.tStopRefresh)
thisExp.addData('White_4.started', White_4.tStartRefresh)
thisExp.addData('White_4.stopped', White_4.tStopRefresh)
thisExp.addData('White_5.started', White_5.tStartRefresh)
thisExp.addData('White_5.stopped', White_5.tStopRefresh)
thisExp.addData('White_6.started', White_6.tStartRefresh)
thisExp.addData('White_6.stopped', White_6.tStopRefresh)
thisExp.addData('White_7.started', White_7.tStartRefresh)
thisExp.addData('White_7.stopped', White_7.tStopRefresh)
thisExp.addData('White_8.started', White_8.tStartRefresh)
thisExp.addData('White_8.stopped', White_8.tStopRefresh)
thisExp.addData('Red_1.started', Red_1.tStartRefresh)
thisExp.addData('Red_1.stopped', Red_1.tStopRefresh)
thisExp.addData('Red_2.started', Red_2.tStartRefresh)
thisExp.addData('Red_2.stopped', Red_2.tStopRefresh)
thisExp.addData('Red_3.started', Red_3.tStartRefresh)
thisExp.addData('Red_3.stopped', Red_3.tStopRefresh)
thisExp.addData('Red_4.started', Red_4.tStartRefresh)
thisExp.addData('Red_4.stopped', Red_4.tStopRefresh)
thisExp.addData('Red_5.started', Red_5.tStartRefresh)
thisExp.addData('Red_5.stopped', Red_5.tStopRefresh)
thisExp.addData('Red_6.started', Red_6.tStartRefresh)
thisExp.addData('Red_6.stopped', Red_6.tStopRefresh)
thisExp.addData('Red_7.started', Red_7.tStartRefresh)
thisExp.addData('Red_7.stopped', Red_7.tStopRefresh)
thisExp.addData('Red_8.started', Red_8.tStartRefresh)
thisExp.addData('Red_8.stopped', Red_8.tStopRefresh)
thisExp.addData('Blue_1.started', Blue_1.tStartRefresh)
thisExp.addData('Blue_1.stopped', Blue_1.tStopRefresh)
thisExp.addData('Blue_2.started', Blue_2.tStartRefresh)
thisExp.addData('Blue_2.stopped', Blue_2.tStopRefresh)
thisExp.addData('Blue_3.started', Blue_3.tStartRefresh)
thisExp.addData('Blue_3.stopped', Blue_3.tStopRefresh)
thisExp.addData('Blue_4.started', Blue_4.tStartRefresh)
thisExp.addData('Blue_4.stopped', Blue_4.tStopRefresh)
thisExp.addData('Blue_5.started', Blue_5.tStartRefresh)
thisExp.addData('Blue_5.stopped', Blue_5.tStopRefresh)
thisExp.addData('Blue_6.started', Blue_6.tStartRefresh)
thisExp.addData('Blue_6.stopped', Blue_6.tStopRefresh)
thisExp.addData('Blue_7.started', Blue_7.tStartRefresh)
thisExp.addData('Blue_7.stopped', Blue_7.tStopRefresh)
thisExp.addData('Blue_8.started', Blue_8.tStartRefresh)
thisExp.addData('Blue_8.stopped', Blue_8.tStopRefresh)
# the Routine "GUI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
