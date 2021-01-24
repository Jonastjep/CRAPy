from flask import Flask
import RPi.GPIO as GPIO
import time
import threading
import cv2
from imutils.video import VideoStream

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

app = Flask(__name__)

vs = VideoStream(src=0).start()
time.sleep(0.2)


