from PIL import ImageGrab
import numpy
from time import sleep
from time import time
from pynput.keyboard import Key, Controller
kb=Controller()
Cooldowns=[0,0,0,0]
Cooldown=2
Keys=[Key.left,Key.down,Key.up,Key.right]
fpslimit=40
timeperframe=1/fpslimit
pixelXs=[70,140,240,310]
showFPS=False
FPStime=time()+1
FPS=0
while True:
    starttime=time()
    capture=ImageGrab.grab(bbox=(880,350,1220,370))
    GameCapCv=numpy.array(capture)
    for i in range(4):
        if (not (GameCapCv[1,pixelXs[i]]==[0,0,0]).all() or not (GameCapCv[6,pixelXs[i]]==[0,0,0]).all()) and Cooldowns[i]==0:
            kb.press(Keys[i])
            kb.release(Keys[i])
            Cooldowns[i]=Cooldown
        if Cooldowns[i]!=0:
            Cooldowns[i]+=-1
    totaltime=time()-starttime
    if totaltime<timeperframe:
        sleep(timeperframe-totaltime)
    FPS+=1
    if time()>FPStime:
        if showFPS:
            print(FPS)
        FPS=0
        FPStime=time()+1
