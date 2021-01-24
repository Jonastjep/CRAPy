import sqlite3 as lite
import sys

con = lite.connect('ArduinoData.db')

with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS arduino_data")
    cur.execute("CREATE TABLE arduino_data (timestamp DATETIME, latitude NUMERIC, longitude NUMERIC, altitudeGPS NUMERIC)")
