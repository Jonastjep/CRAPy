import time, sqlite3, serial

ser = serial.Serial('/dev/ttyACM0', 9600)

dbname = "sensorData.db"

def logData(temp, pres, alt):
	conn = sqlite3.connect(dbname)
	curs = conn.cursor()
	curs.execute("INSERT INTO BMP280_data values(datetime('now'),(?),(?),(?))", (temp, pres, alt))
	conn.commit()
	conn.close()

def displayData():
	conn = sqlite3.connect(dbname)
	curs = conn.cursor()
	print("\nDatabase Content:\n")
	for row in curs.execute("SELECT * FROM BMP280_data"):
		print(row)
	conn.close()



def main():
	waste = ser.readline().decode("utf-8")

	for i in range(15):
		data = ser.readline().decode("utf-8")
		parse = data.split(",")
		logData(parse[0],parse[1],parse[2])
		time.sleep(2)
	displayData()

main()
