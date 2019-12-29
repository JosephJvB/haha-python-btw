import os
import requests
import time
from datetime import datetime
from client import Client

if __name__ == '__main__':
    timeout = 60 * 58
    while True:
        if datetime.now().hour == int(os.getenv('hour')):
            c = Client()
            c.run()
        time.sleep(timeout)