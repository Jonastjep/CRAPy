import serial, time

ser = serial.Serial('/dev/ttyACM0', 9600)

for i in range(5):

	data = ser.readline().decode("utf-8")
	print(data)
	time.sleep(2)
