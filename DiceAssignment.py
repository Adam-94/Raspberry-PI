#!/usr/bin/python

# Importing appropraite libraries 
import RPi.GPIO as GPIO
import time
import random

# Using GPIO numbers instead of pin numbers
GPIO.setmode (GPIO.BCM)

# A list of GPIO numbers, its duplicated so that the for loop can turn on the next LED after it passes the range of 6
# so for example if the score goes past 6 it will go through the duplicate, lighting up a score from 7-12.
ledsix = [4,17,22,10,9,11,4,17,22,10,9,11]

# Setting up 6 LED's as outputs, then setting them to false
for i in range(6):
    GPIO.setup(ledsix[i], GPIO.OUT)
    GPIO.output(ledsix[i], False)
    
# Setting up the switch as an input
GPIO.setup (7, GPIO.IN)
random.seed()
print"Press the switch to roll"
print "To exit press CTRL-C"

# I am using try to catch when the user presses CTRL-C
# and to run GPIO cleanup fuction, to stop any error messages
try:
    # If the switch is pressed the code below will start
    while True:
        if GPIO.input(7)==1:

            # Turn 6 LEDS to false
            for i in range(6):
                GPIO.output(ledsix[i],False)

            # Declare first dice from the range of 1-6
            dice = random.randint(1,6)
            time.sleep(0.5)
            print '\n' + "Dice one rolling... " + str(dice)
            
            # Declare second dice with the same range of 1-6
            diceTwo = random.randint(1,6)
            time.sleep(0.5)
            print "Dice two Rolling..." + str(diceTwo)

            # Adding Dice and diceTwo together to get the totalRoll
            totalRoll = dice + diceTwo
            time.sleep(0.5)
            print '\n' + "First Roll: " + str(dice) + '\n' + "Second Roll: " + str(diceTwo) + '\n' + "Total: " + str(totalRoll)

            # If both dice are the same number then it will be a double 
            if dice == diceTwo:
                print '\n' + "Congratulations you rolled a double of " + str(dice) + " making: " + str(totalRoll)

            # If roll is equal to 7 or 11 then it will go to the print statement
            if totalRoll == 7 or totalRoll == 11:
               print '\n' + "Congratulations you rolled a: " + str(totalRoll)
               
            # The for i is in range of totalRoll, this will increment i and will then turn on an LED, turn it off
            # then proceed to this iteration until it reaches totalRoll
            for i in range(totalRoll):
                time.sleep(0.5)
                GPIO.output(ledsix[i], True)
                time.sleep(0.5)
                GPIO.output(ledsix[i], False)
                                                   
except KeyboardInterrupt:
    GPIO.cleanup()
