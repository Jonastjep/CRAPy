import PyLidar3
import time # Time module

#In linux type in terminal -- ls /dev/tty* 
port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4(port)
if(Obj.Connect()):
	try:
		print(Obj.GetDeviceInfo())
		gen = Obj.StartScanning()
		t = time.time() # start time 
		while (time.time() - t) < 5: #scan for 30 seconds
			vals = next(gen)
			for i in vals:
				print(str(i) + ":" + str(vals[i]))
			#print(next(gen))
			time.sleep(0.5)
		Obj.StopScanning()
		Obj.Disconnect()
	except:
		Obj.StopScanning()
		Obj.Disconnect()
else:
	print("Error connecting to device")
