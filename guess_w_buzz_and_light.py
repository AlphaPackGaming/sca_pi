#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

buzz_pin = 32
led_pin = 11



import random
n = random.randint(1,100)
attempts = 0
i = 0
num_random_numbers = 10
while i < num_random_numbers:   
    guessed_number = int(raw_input("Guess an integer between 1 and 100: \n"))
    attempts = attempts + 1
    if guessed_number == n:
        print "That was correct!"
        GPIO.setup(led_pin,GPIO.OUT)

        GPIO.output(led_pin,True)
        time.sleep(2)

        GPIO.output(led_pin,False)
        break 
    if guessed_number >= n:
        print "Your guess was too high. Try again."
        GPIO.setup(buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.ChangeFrequency(1760)

        Buzz.start(50)
        time.sleep(1.5)

        Buzz.stop()

    elif guessed_number <=n:
        print "Your guess was too low. Try again."
        GPIO.setup(buzz_pin,GPIO.OUT)
        Buzz = GPIO.PWM(buzz_pin,1000)
        Buzz.ChangeFrequency(55)

        Buzz.start(50)
        time.sleep(1.5)

        Buzz.stop()

        
    if i == num_random_numbers - 1:
        print "Sorry you took too many guesses..."
    i = i+1 

print "Attempts taken: " ,attempts

GPIO.cleanup()

 
