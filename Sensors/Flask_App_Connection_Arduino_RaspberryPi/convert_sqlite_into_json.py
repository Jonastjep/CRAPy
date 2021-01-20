import sqlite3
import json

db = "arduino_data.db"

def sqliteToJson(path, db, nbSample=False):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    datetime = []
    air_composition = []
    temperature = []
    humidity = []
    pressure = []
    altitude = []
    moisture_of_the_soil = []

    if nbSample:
        for row in c.execute("SELECT * FROM arduino_data ORDER BY timestamp DESC LIMIT "+str(nbSample)):
            datetime.append(row[0])
            air_composition.append(row[1])
            temperature.append(row[2])
            humidity.append(row[3])
            pressure.append(row[4])
            altitude.append(row[5])
            moisture_of_the_soil.append(row[6])


    else:
        for row in c.execute("SELECT * FROM arduino_data"):
            datetime.append(row[0])
            air_composition.append(row[1])
            temperature.append(row[2])
            humidity.append(row[3])
            pressure.append(row[4])
            altitude.append(row[5])
            moisture_of_the_soil.append(row[6])

            data = {
            "datetime": datetime,
            "air_composition": air_composition,
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "altitude": altitude,
            "moisture_of_the_soil": moisture_of_the_soil
            }
    print(len(datetime))

    with open("static/arduino_data.json", "w") as file:
        json.dump(data,file)
