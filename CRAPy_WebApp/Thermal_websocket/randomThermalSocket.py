import asyncio
import datetime
import websockets
import json, math
import numpy as np
from scipy import interpolate

# How often should data be sent? (in sec)
intervals = 0.05

async def time(websocket, path):
    while True:

        grid_xn, grid_yn = np.mgrid[0:1:64j, 0:1:64j]
        xn = grid_xn[:,0]
        yn = grid_yn[0,:]

        grid_x, grid_y = np.mgrid[0:1:8j, 0:1:8j]
        x = grid_x[:, 0]
        y = grid_y[0, :]
        z = (np.random.random((8, 8))*255)

        spline = interpolate.RectBivariateSpline(x, y, z, s=0, kx=3, ky=3)
        zn = spline(xn, yn)

        dataFlat = zn.tolist()

        data_dict = {
            "data": dataFlat
            }

        now = json.dumps(data_dict)

        await websocket.send(now)
        await asyncio.sleep(intervals)

start_server = websockets.serve(time,port=5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
