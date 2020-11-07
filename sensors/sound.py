import RPi.GPIO as GPIO
import time

channel = 2
GPIO.setmode (GPIO.BCM)
GPIO.setup  (channel, GPIO.IN)

def call_back (channel):
	if (GPIO.input (channel)):
		print ('Sound Detected')
	else:
                print ('no sound')
		pass

GPIO.add_event_detect (channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback (channel, call_back)

while (True):
        print (GPIO.input (channel))
	#time.sleep(1)

