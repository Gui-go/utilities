#! /bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)

time.sleep(1)

GPIO.output(18, GPIO.LOW)

GPIO.cleanup()

print("Blink!")
