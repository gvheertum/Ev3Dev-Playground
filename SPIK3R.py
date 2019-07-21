#!/usr/bin/env python3
#maker
#ssh robot@ev3dev.local
#pw maker
#python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from time import sleep

#LARGE MOTOR D -> Shooter
#LARGE MOTOR  B-> Walking
#MEDIUM MOTOR A -> Grabber

#Sensor 4 -> IR

import os
import sys
import time

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


moveMotor = LargeMotor(OUTPUT_B)
sensor = InfraredSensor()
sensor.mode = 'IR-PROX'
btn = Button()
while not btn.any(): # While no (not any) button is pressed.
    debug_print("Running step")
    v = sensor.value()
    debug_print(v)
    if v > 20:
        debug_print("move")
        moveMotor.on_for_seconds(30, 1, brake=True, block=True)
        sleep(0.5)  # Wait 0.01 second
    else:
        break



#IR, mode = 'IR-SEEK' -> Seeks the angle of the beacon (pos means to the right, neg to the left)
#IR, mode = 'IR-PROX' -> Distance to beacon 
