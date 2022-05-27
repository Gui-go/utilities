import RPi.GPIO as GPIO
import time

# Module level constants
LEDS=[18, 17]
# LED1 = 18
# LED2 = 22

# Sets up pins as outputs
def setup(*leds):
    GPIO.setmode(GPIO.BCM)
    for led in leds:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.LOW)

# Turn on and off the leds
def blink(*leds):
    # Blink all leds passed
    for led in leds:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led, GPIO.LOW)

if __name__ == '__main__':
    # Setup leds
    # setup(LED1, LED2)
    setup(LEDS)
    # Run blinking forever
    print("Press Ctrl+C to stop program")
    try:
        while True:
            # blink(LED1, LED2)
            blink(LEDS)
    # Stop on Ctrl+C and clean up
    except KeyboardInterrupt:
        GPIO.cleanup()
