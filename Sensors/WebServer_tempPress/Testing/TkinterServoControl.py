from tkinter import *
import serial

def UpdateSerial(event):
        arduino.write(bytes("<"+str(w1.get())+","+str(w2.get())+","+"0"+">",encoding='utf8'))

arduino = serial.Serial('COM7', 9600, timeout=.1)

master = Tk()
w1 = Scale(master, from_=0, to=180, command=UpdateSerial)
w1.pack()
yval = w1.get()
w2 = Scale(master, from_=0, to=180, orient=HORIZONTAL, command=UpdateSerial)
w2.pack()
xval = w2.get()

mainloop()
