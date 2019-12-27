import os
import requests
import time
from client import Client

if __name__ == '__main__':
    timeout = 60 * 60 * 24
    while True:
        if os.getenv('status') == 'live':
            c = Client()
            c.run()
        time.sleep(timeout)