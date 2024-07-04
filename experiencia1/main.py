#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
motorB = Motor(Port.B)
motorC = Motor(Port.C)
left_motor = motorB
right_motor = motorC
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

color_sensor_in1 = ColorSensor(Port.S1)

motorC = Motor(Port.C) # Magnet
md = Motor(Port.C)
mi = Motor (Port.B)
robot = DriveBase(mi,md,55.5,104)
# Here is where your code starts
while True:
    while color_sensor_in1.color() != Color.WHITE:
        while color_sensor_in1.color() != Color.WHITE:
            motorB.run_angle(speed=120, rotation_angle=10, then=Stop.COAST, wait=(color_sensor_in1.color() == Color.BLACK))
        while color_sensor_in1.color() == Color.WHITE:
            motorC.run_angle(speed=120, rotation_angle=(20), then=Stop.COAST, wait=True)
            
        while color_sensor_in1.color() != Color.WHITE:
            motorC.run_angle(speed=120, rotation_angle=10, then=Stop.COAST, wait=(color_sensor_in1.color() == Color.BLACK))
        while color_sensor_in1.color() == Color.WHITE:
            motorB.run_angle(speed=120, rotation_angle=(20), then=Stop.COAST, wait=True)