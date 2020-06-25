import time, sqlite3, serial

ser = serial.Serial('COM9', 9600)

database = "C:/sqlite/gpsdata.db"

entries = 20

def logData(latitude, longitude, altitude):
    connection = sqlite3.connect(database)
    curs = connection.cursor();
    curs.execute("INSERT INTO GPSDATA VALUES(? , ? , ?);", (latitude, longitude, altitude))
    connection.commit()
    connection.close()
    
def displayData():
    connection = sqlite3.connect(database)
    curs = connection.cursor()
    for row in curs.execute("SELECT * FROM GPSDATA"):
        print(row)
    connection.close()
    
def main():
    
    startupMsg = ser.readline().decode("utf-8")
    
    print(startupMsg)
    print("Gathering the next {} entries...".format(entries))
    
    for i in range(entries):
        data = ser.readline().decode("utf-8")
        toParse = data.split(";")
        if(len(toParse)==3):
            logData(toParse[0],toParse[1],toParse[2])
            time.sleep(2)
            
    displayData()
    
main()