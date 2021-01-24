import sqlite3 as lite
import sys

con = lite.connect('ArduinoData.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS arduino_data")
    cur.execute("CREATE TABLE arduino_data (timestamp DATETIME, air_composition NUMERIC, temperature NUMERIC, humidity NUMERIC, pressure NUMERIC, altitude NUMERIC, moisture_of_the_soil NUMERIC")
