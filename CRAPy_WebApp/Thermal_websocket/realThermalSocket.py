import sys
import os.path
from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
import time

import asyncio
import datetime
import websockets
import json, math
import numpy as np

from scipy import interpolate


sensor = Adafruit_AMG88xx()
# wait for AMG to boot
sleep(0.1)

intervals = 0.1

async def time(websocket, path):
	# preallocating variables
	norm_pix = []
	cal_vec = []
	kk = 0
	cal_size = 10 # size of calibration
	cal_pix = []

	while(True):
		cal_pix = []
		if kk==0:
			print("Sensor should have clear path to calibrate against environment")
		norm_pix = sensor.readPixels() # read pixels
		if kk<cal_size+1:
			kk+=1
		if kk==1:
			cal_vec = norm_pix
			continue
		elif kk<=cal_size:
			for xx in range(0,len(norm_pix)):
				cal_vec[xx]+=norm_pix[xx]
				if kk==cal_size:
					cal_vec[xx] = cal_vec[xx]/cal_size
			continue
		else:
			[cal_pix.append(norm_pix[x]-cal_vec[x]) for x in range(0,len(norm_pix))]
			if min(cal_pix)<0:
				for y in range(0,len(cal_pix)):
					cal_pix[y]+=abs(min(cal_pix))

		grid_xn, grid_yn = np.mgrid[0:1:64j, 0:1:64j]
		xn = grid_xn[:,0]
		yn = grid_yn[0,:]
		
		grid_x, grid_y = np.mgrid[0:1:8j, 0:1:8j]
		x = grid_x[:, 0]
		y = grid_y[0, :]
		z = np.reshape(cal_pix,(8,8))*120
		
		spline = interpolate.RectBivariateSpline(x, y, z, s=0, kx=3, ky=3)
		zn = spline(xn, yn)
		
		pixels = zn.tolist()
		
		data_dict = {
		"data": pixels
		}
		
		now = json.dumps(data_dict)
		
		await websocket.send(now)
		await asyncio.sleep(intervals)

start_server = websockets.serve(time, port=5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
