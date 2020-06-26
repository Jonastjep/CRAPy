#Project Brover @2020
#Simon Stoll

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#instantiate and deactivate the trigger
def setup(TRIG, ECHO):
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    #Add clause for manual/automated activation of sensor
    time.sleep(2)

#activate Trigger for 10microseconds
def trigger(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    #listen for the return sound, record times
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    return pulse_duration


#calculate distance in cm and round
def distance(pulse_duration):
    dist = pulse_duration*17150
    dist = round(dist, 2)
    dist = str(dist)
    return dist

#print(dist, pulse_duration)
#pulse_duration = str(pulse_duration)
def cleanup():
    GPIO.cleanup()
