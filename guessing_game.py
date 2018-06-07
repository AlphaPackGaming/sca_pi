#!/usr/bin/env python

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
        break 
    if guessed_number >= n:
        print "Your guess was too high. Try again."
    if guessed_number <=n:
        print "Your guess was too low. Try again."
    if i == num_random_numbers - 1:
        print "Sorry you took too many guesses..."
    i = i+1 

print "Attempts taken: " ,attempts

 
