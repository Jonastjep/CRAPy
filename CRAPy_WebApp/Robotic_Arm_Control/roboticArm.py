import threading
import argparse
from app import app
from app.routes import detect_motion

# start a thread that will perform motion detection
t = threading.Thread(target=detect_motion, args=(32,))
t.daemon = True
t.start()

if __name__ == '__main__':
  app.run(host='0.0.0.0')
