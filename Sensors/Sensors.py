#Project Brover @2020
#Simon Stoll
from Sonic_sensor import *
import RPi.GPIO as GPIO
import time
import sqlite3
conn = sqlite3.connect('Sensordata.db')
GPIO.setmode(GPIO.BCM)

#Front Sensor Pin location
TRIG1 = 14
ECHO1 = 15

#Back Sensor Pin location
TRIG2 = 18
ECHO2 = 23

#Call other class to run the sensors
setup(TRIG1,ECHO1)
pulse_duration = trigger(TRIG1,ECHO1)
dist1 = distance(pulse_duration)

setup(TRIG2,ECHO2)
pulse_dur = trigger(TRIG2,ECHO2)
dist2 = distance(pulse_dur)

theTime = time.asctime()
#Add server for database
conn.execute("INSERT INTO Sonic VALUES (?,?,?,?);", (NULL,dist1,dist2,theTime);
conn.commit()

setup(TRIG2,ECHO2)
pulse_dur = trigger(TRIG2,ECHO2)
dist = distance(pulse_duration)

conn.close()
