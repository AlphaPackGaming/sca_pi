#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
 #Quarter note = .44seconds
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32

GPIO.setup(buzz_pin,GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(659.26)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()


Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(659.26)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(659.26)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(659.26)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.88)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(698.46)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(880)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(783.99)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(698.46)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()
 #end of meesure 5

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(698.46)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(698.46)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()
 # End of messure 6

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(493.88)
Buzz.start(50)
time.sleep(.11)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.22)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(587.33)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(659.26)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(523.25)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.44)
Buzz.stop()

Buzz = GPIO.PWM(buzz_pin,1000)
Buzz.ChangeFrequency(440)
Buzz.start(50)
time.sleep(.88)
Buzz.stop()

GPIO.cleanup()

