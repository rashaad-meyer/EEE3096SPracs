#!/usr/bin/python3
"""
Python Practical Template
Keegan CrankshawReadjust this Docstring as follows:
Names: Rashaad Meyer
Student Number: MYRMOE002
Prac: 1
Date: 28/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO 	# Import Raspberry Pi GPIO library
from time import sleep  	# Import the sleep function from the time module

GPIO.setwarnings(False)		# Ignore warning for now
GPIO.setmode(GPIO.BOARD)	# Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)	# Set pin 16 to be an input pin and set pull_up_down resistor to down
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)	# Set pin 18 to be an input pin and set pull_up_down resistor to down

GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)	# Set pin 11 to be an output pin and set initial value to low (off)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)	# Set pin 13 to be an output pin and set initial value to low (off)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW)	# Set pin 15 to be an output pin and set initial value to low (off)

binary = ["000", "001", "010", "011", "100", "101", "110", "111"]	# Initialises array that holds all binary values from 0-7
counter = 0 	# Initialises counter

def button_decrease_callback(channel):

	global counter	# Allows the use of counter in this function

	if counter == 0:	# Increments counter and resets if it gets to 0
		counter = 7
	else:
		counter-=1

	if binary[counter][0] == '1':	# Check if first bit is 1 and if it is turns first LED on else turns LED off
		GPIO.output(11, GPIO.HIGH)
	else:
		GPIO.output(11, GPIO.LOW)

	if binary[counter][1] == '1':	# Check if second bit is 1 and if it is turns second LED on else turns LED off
                GPIO.output(13, GPIO.HIGH)
        else:
                GPIO.output(13, GPIO.LOW)

	if binary[counter][2] == '1':	# Check if third bit is 1 and if it is turns third LED on else turns LED off
                GPIO.output(15, GPIO.HIGH)
        else:
                GPIO.output(15, GPIO.LOW)

	sleep(2)	# Sleeps program so that nothing happens for 2 seconds


def button_increase_callback(channel):

	global counter	# Allows the use of counter in this function

	if counter == 7:	# Increments counter and resets if it gets to 0
                counter = 0
        else:
                counter+=1

        if binary[counter][0] == '1':	# Check if first bit is 1 and if it is turns first LED on else turns LED off
                GPIO.output(11, GPIO.HIGH)
        else:
                GPIO.output(11, GPIO.LOW)

        if binary[counter][1] == '1':	# Check if second bit is 1 and if it is turns second LED on else turns LED off
                GPIO.output(13, GPIO.HIGH)
        else:
                GPIO.output(13, GPIO.LOW)

        if binary[counter][2] == '1':	# Check if third bit is 1 and if it is turns third LED on else turns LED off
                GPIO.output(15, GPIO.HIGH)
        else:
                GPIO.output(15, GPIO.LOW)
	sleep(2)	# Sleeps program so that nothing happens for 2 seconds



GPIO.add_event_detect(16, GPIO.RISING, callback = button_decrease_callback)	# Set event up on pin 16 for rising edges
GPIO.add_event_detect(18, GPIO.RISING, callback = button_increase_callback)	# Set event up on pin 18 for rising edges



# Logic that you write
def main():
	pass



# Only run the functions if 
if __name__ == "__main__":
	# Make sure the GPIO is stopped correctly
	try:
        	while True:
            		main()
    	except KeyboardInterrupt:
        	print("Exiting gracefully")
        	# Turn off your GPIOs here
        	GPIO.cleanup()
    	except e:
        	GPIO.cleanup()
        	print("Some other error occurred")
        	print(e.message)
