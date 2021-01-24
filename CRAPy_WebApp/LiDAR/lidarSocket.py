#!/usr/bin/env python

# WS server that sends SenseHat data

import asyncio
import datetime
import websockets
import json, math, random
import numpy as np
from scipy import interpolate

import PyLidar3
import time # Time module

#In linux type in terminal -- ls /dev/tty* 
port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4(port)

# How often should data be sent? (in sec)
intervals = 0.01

def getRandomArbitrary(min, max):
  return random.random() * (max - min) + min;

async def time(websocket, path):
    try:
        if (Obj.Connect()):
            print(Obj.GetDeviceInfo())
            gen = Obj.StartScanning()
        while True:
            vals = next(gen)
            ang = []
            d = []
            for i in vals:
                ang.append(int(i))
                d.append(vals[i])
            
            
            # for i in range(100):
                # ang.append(getRandomArbitrary(0, 2*math.pi))
                # d.append(20) #getRandomArbitrary(0, 2*math.pi))
        
            data_dict = {
                "ang": ang,
                "d": d
                }
        
            # now = str(yaw_pi)
            now = json.dumps(data_dict)
            #print(now)
            # now = datetime.datetime.utcnow().isoformat() + 'Z'
            await websocket.send(now)
            await asyncio.sleep(intervals)
    except:
        Obj.StopScanning()
        Obj.Disconnect()
start_server = websockets.serve(time,port=5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
