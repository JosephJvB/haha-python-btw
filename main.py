import os
import requests
import time
from datetime import datetime
from client import Client

if __name__ == '__main__':
    timeout = 60 * 60
    while True:
        if datetime.now().hour == int(os.getenv('hour')):
            c = Client()
            c.run()
        else:
            print('not yet :)')
        time.sleep(timeout)