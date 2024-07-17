#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
md = Motor(Port.C)
mi = Motor(Port.B)
robot = DriveBase(mi,md,55.5,104)

color_sensor = ColorSensor(Port.S1)
contador1 = 0
contador2 = 0
color_detectado = color_sensor.color()

if color_detectado != Color.WHITE:
    while color_detectado != Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1) 
    while color_detectado == Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1)

    while color_detectado != Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1)
        contador1 = contador1 + 1

    while color_detectado == Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1)

    while color_detectado != Color.WHITE:
        color_detectado = color_sensor.color()
        robot.straight(1)
        contador2 = contador2 + 1

    while True:
        contador3 = 0
        color_detectado = color_sensor.color()
        robot.straight(1)
        while color_detectado != Color.WHITE:
            color_detectado = color_sensor.color()
            robot.straight(1)
            contador3 = contador3 + 1
        if contador3 >= contador2 - 2 and contador3 <= contador2 + 2:
            print("0")
        elif contador3 >= contador1 - 2 and contador3 <= contador1 + 2:
            print("1")