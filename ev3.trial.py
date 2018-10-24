#!/usr/bin/env python3
#maker
#ssh robot@ev3dev.local
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, LightSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

sound = Sound()


# TODO: Add code here
leds = Leds()
leds.set_color("LEFT", "RED")
leds.set_color("RIGHT", "RED")

tank = MoveTank(OUTPUT_B, OUTPUT_C)

ir = InfraredSensor()
irDist = ir.value()
while irDist > 10:
    print(ir.value())
    sound.speak('dum dum')
    tank.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 3)
    irDist = ir.value()
    

#m = LargeMotor(OUTPUT_C)
#m2 = LargeMotor(OUTPUT_B)
#m.on_for_rotations(SpeedPercent(75), 5)  

# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
tank.on_for_rotations(SpeedPercent(100), SpeedPercent(100), 10)

# # drive in a different turn for 3 seconds
# tank.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)

