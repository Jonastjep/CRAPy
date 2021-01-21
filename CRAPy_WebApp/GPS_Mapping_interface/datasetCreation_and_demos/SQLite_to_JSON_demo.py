import sqlite3, json

db = "GPS_data.db"

conn = sqlite3.connect(db)
c = conn.cursor()

coordinates = []
datetime = []
altitude = []

for row in c.execute("SELECT * FROM GPS_data"):
    datetime.append(row[0])
    coordinates.append([row[1],row[2]])
    altitude.append(row[3])

data = {
    "datetime": datetime,
    "coordinates": coordinates,
    "altitude": altitude
}

with open("SQLite_to_JSON_coordinateOutput.json", "w") as file:
    json.dump(data,file)
