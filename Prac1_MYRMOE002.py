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
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW)


def button_decrease_callback(channel):
	print("decreased")

	GPIO.output(11, GPIO.HIGH)
	sleep(2)

	GPIO.output(11, GPIO.LOW)
	sleep(2)

def button_increase_callback(channel):
	print("increased")

	GPIO.output(13, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	sleep(2)

	GPIO.output(13, GPIO.LOW)
	GPIO.output(15, GPIO.LOW)
	sleep(2)


GPIO.add_event_detect(16, GPIO.RISING, callback = button_decrease_callback)
GPIO.add_event_detect(18, GPIO.RISING, callback = button_increase_callback)



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
