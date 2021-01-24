import serial
import time
import sqlite3
import random as rd

hader = '<'
footer = '>'
separator = ';'

#import serial data

dbname='ArduinoData.db'

def Serial_import():
    try:
        read_serial=ser.readline()
        if (read_serial[0:2] == header and read_serial[-2] == footer):
            line = read_serial.split(separator)
            print(line)
            air_composition = line[0]
            temperature = line[1]
            humidity = line[2]
            pressure = line[3]
            altitude = line[4]
            moisture_of_the_soil = line[5]
            latitude = line [6]
            longitude = line [7]
            altitudeGPS = line [8]

        return temperature, air_composition, humidity, pressure, altitude, moisture_of_the_soil, latitude, longitude, altitudeGPS
    except:
        print("An exception occurred")

#log sensor data onto database
# def logRandomData():
#     conn=sqlite3.connect(dbname)
#     curs=conn.cursor()
#     curs.execute("INSERT INTO arduino_data values(datetime('now'), (?), (?), (?), (?))", (rd.random()*20, rd.random()*20, rd.random()*20, rd.random()*20))
#     conn.commit()
#     conn.close()

def logData(temperature, ultrasound, air_composition, humidity, pressure, altitude, moisture_of_the_soil):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO arduino_data values(datetime('now'), (?), (?), (?), (?), (?), (?))", (air_composition, temperature, humidity, pressure, altitude, moisture_of_the_soil))
    conn.commit()
    conn.close()

def logGPS(latitude, longitude, altitudeGPS):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO GPS_data values(datetime('now'), (?), (?), (?))" (latitude, longitude, altitudeGPS))
    conn.commit()
    conn.close()

#display database data
# def displayData():
#     conn = sqlite3.connect(dbname)
#     curs = conn.cursor()
#     for row in curs.execute("SELECT * FROM arduino_data"):
#         print(row)
#     conn.close()

#main function
def main():
    #ser = serial.Serial('/dev/ttyACM0',9600)
    while True:
        air_composition, temperature, humidity, pressure, altitude, moisture_of_the_soil, latitude, longitude, altitudeGPS = Serial_import()
        logData (air_composition, temperature, humidity, pressure, altitude, moisture_of_the_soil)
        logGPS (latitude, longitude, altitudeGPS)
        time.sleep(1)
    displayData()

#Execute program
if __name__ == '__main__':
	main()
