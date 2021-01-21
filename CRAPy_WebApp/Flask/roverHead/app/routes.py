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

@app.route('/stream')
def stream():
    slider1 = 10
    slider2 = 10

    return render_template('stream.html', lastval1=slider1, lastval2=slider2)

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

@app.route('/video')
def video():
    return render_template('video.html')

def detect_motion(frameCount):
    global vs, outputFrame, lock

    md = SingleMotionDetect(accumWeight=0.1)
    total = 0
    
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        if total > frameCount:
            # detect motion in the image
            motion = md.detect(gray)
            # check to see if motion was found in the frame
            if motion is not None:
            # unpack the tuple and draw the box surrounding the
            # "motion area" on the output frame
                (thresh, (minX, minY, maxX, maxY)) = motion
                cv2.rectangle(frame, (minX, minY), (maxX, maxY),(0, 0, 255), 2)
    
        # update the background model and increment the total number
        # of frames read thus far
        md.update(gray)
        total += 1
        # acquire the lock, set the output frame, and release the
        # lock
        with lock:
            outputFrame = frame.copy()

def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

