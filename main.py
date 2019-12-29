import os
import requests
import time
from datetime import datetime, timedelta
from client import Client

if __name__ == '__main__':
    timeout = 60 * 60 * 24
    while True:
        if os.getenv('status') == 'live':
            c = Client()
            c.run()
        elif os.getenv('status') == 'alter':
            timeout = timeout - (60 * 60 * 4)
        time.sleep(timeout)