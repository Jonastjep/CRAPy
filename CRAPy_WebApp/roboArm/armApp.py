from flask import Flask
import RPi.GPIO as GPIO
from time import sleep

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

app = Flask(__name__)

from flask import Flask, Response, render_template, request, flash, redirect, url_for

@app.route("/")
@app.route("/index")
def index():
    Rotation = 8
    Arm_1 = 8
    Arm_2 = 8
    Roll = 8
    Pitch = 8
    Gripper = 8

    return render_template('./index.html', lastval1=Rotation, lastval2=Arm_1, lastval3=Arm_2, lastval4=Roll, lastval5=Pitch, lastval6=Gripper )

@app.route("/send", methods=["POST"])
def send():
    # Get slider Values
    val1 = request.form["Rotation"]
    val2 = request.form["Arm_1"]
    val3 = request.form["Arm_2"]
    val4 = request.form["Roll"]
    val5 = request.form["Pitch"]
    val6 = request.form["Gripper"]
    
    #Renormalize values from 2-15.5 to degree
    nval1 = float(val1)*10.5/270+2
    nval2 = float(val2)*10.5/270+2
    nval3 = float(val3)*10.5/270+2
    nval4 = float(val4)*10.5/270+2
    nval5 = float(val5)*10.5/270+2
    nval6 = float(val6)*10.5/270+2
    
    # Change duty cycle
    prot.ChangeDutyCycle(float(nval1))
    pa1.ChangeDutyCycle(float(nval2))
    pa2.ChangeDutyCycle(float(nval3))
    proll.ChangeDutyCycle(float(nval4))
    ppitch.ChangeDutyCycle(float(nval5))
    pgrip.ChangeDutyCycle(float(nval6))
    
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    prot.ChangeDutyCycle(0)
    pa1.ChangeDutyCycle(0)
    pa2.ChangeDutyCycle(0)
    proll.ChangeDutyCycle(0)
    ppitch.ChangeDutyCycle(0)
    pgrip.ChangeDutyCycle(0)
    return render_template('index.html', lastval1=val1, lastval2=val2, lastval3=val3, lastval4=val4, lastval5=val5, lastval6=val6)


if __name__ == '__main__':
  app.run(host='0.0.0.0')
