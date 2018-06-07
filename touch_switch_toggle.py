#!/usr/bin/env python

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

touch_pin = 31
buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)
GPIO.setup(touch_pin,GPIO.IN)

while True:
    if GPIO.input(touch_pin) == 0:
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.stop()

    if GPIO.input(touch_pin) == 1:
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.ChangeFrequency(659.26)
        Buzz.start(50)
        time.sleep(.44)
        Buzz.stop()
