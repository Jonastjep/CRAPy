from flask import Flask
import RPi.GPIO as GPIO
import time
import threading
import cv2
from imutils.video import VideoStream

################### STREAM ####################
outputFrame = None
lock = threading.Lock()

servo_pin = 17          
servo_pin1 = 27
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)     
GPIO.setup(servo_pin1, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)
p1 = GPIO.PWM(servo_pin1, 50)

p.start(0)
p1.start(0)

###################### ROBOTIC ARM ######################

# Pins where we have connected servos
servo_rot = 5
servo_a1 = 6
servo_a2 = 13
servo_roll = 19
servo_pitch = 26
servo_grip = 21

GPIO.setmode(GPIO.BCM)      # We are using the BCM pin numbering
# Declaring Servo Pins as output pins
GPIO.setup(servo_rot, GPIO.OUT)
GPIO.setup(servo_a1, GPIO.OUT)
GPIO.setup(servo_a2, GPIO.OUT)
GPIO.setup(servo_roll, GPIO.OUT)
GPIO.setup(servo_pitch, GPIO.OUT)
GPIO.setup(servo_grip, GPIO.OUT)

# Created PWM channels at 50Hz frequency
prot = GPIO.PWM(servo_rot, 50)
pa1 = GPIO.PWM(servo_a1, 50)
pa2 = GPIO.PWM(servo_a2, 50)
proll = GPIO.PWM(servo_roll, 50)
ppitch = GPIO.PWM(servo_pitch, 50)
pgrip = GPIO.PWM(servo_grip, 50)


# Initial duty cycle
prot.start(0)
pa1.start(0)
pa2.start(0)
proll.start(0)
ppitch.start(0)
pgrip.start(0)

#########################################################

app = Flask(__name__)

vs = VideoStream(src=0).start()
time.sleep(0.2)


