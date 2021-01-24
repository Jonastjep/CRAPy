from app import app, p, p1, vs, outputFrame, lock
from flask import Flask, Response, render_template, request, flash, redirect, url_for
import RPi.GPIO as GPIO
from time import sleep
import cv2
import imutils
import datetime
from app.singlemotiondetect import SingleMotionDetect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/roboArm')
def roboArm():
    slider1 = 2+12.5/2
    slider2 = 2+12.5/2

    return render_template('roboArm.html', lastval1=slider1, lastval2=slider2)

@app.route("/send", methods=["POST"])
def send():
    val1 = request.form["slider1"]
    val2 = request.form["slider2"]

    p.ChangeDutyCycle(float(val1))
    p1.ChangeDutyCycle(float(val2))
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)

    return render_template('stream.html', lastval1=val1, lastval2=val2)
