import os
import requests
import time
from datetime import datetime
from client import Client

if __name__ == '__main__':
    timeout = 60 * 60 * 24
    while True:
        print('asdasdadssd', datetime.now().hour)
        if os.getenv('status') == 'live':
            c = Client()
            c.run()
        time.sleep(timeout)