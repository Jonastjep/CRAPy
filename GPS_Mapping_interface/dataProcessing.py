import sqlite3, json

# LIBRARY

#These functions are to a very specific use: GPS data in our
# very special context: our data strutures etc. So need to adapt if use

def sqliteToJson(path, db, nbSample=False):
    conn = sqlite3.connect(db)
    c = conn.cursor()

    coordinates = []
    datetime = []
    altitude = []

    if nbSample:
        for row in c.execute("SELECT * FROM GPS_data ORDER BY timestamp DESC LIMIT "+str(nbSample)):
            datetime.append(row[0])
            coordinates.append([row[1],row[2]])
            altitude.append(row[3])
    else:
        for row in c.execute("SELECT * FROM GPS_data"):
            datetime.append(row[0])
            coordinates.append([row[1],row[2]])
            altitude.append(row[3])

    data = {
        "datetime": datetime,
        "coordinates": coordinates,
        "altitude": altitude
    }
    print(len(datetime))

    with open(path + "coordinateOutput.json", "w") as file:
        json.dump(data,file)
