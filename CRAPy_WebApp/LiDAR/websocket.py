#!/usr/bin/env python

# WS server that sends SenseHat data

import asyncio
import datetime
import websockets
import json, math, random
import numpy as np
from scipy import interpolate

# How often should data be sent? (in sec)
intervals = 0.01

def getRandomArbitrary(min, max):
  return random.random() * (max - min) + min;

async def time(websocket, path):
    while True:
        ang = []
        d = []
        for i in range(100):
            ang.append(getRandomArbitrary(0, 2*math.pi))
            d.append(20) #getRandomArbitrary(0, 2*math.pi))

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

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
