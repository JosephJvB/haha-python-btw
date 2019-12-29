import os
import requests
import time
from datetime import datetime, timedelta
from client import Client

if __name__ == '__main__':
    timeout = 60 * 60 * 24
    while True:
        print(os.getenv('status'), '???')
        if os.getenv('status') == 'live':
            c = Client()
            c.run()
        print('SCHLEEP TILL', datetime.now() + timedelta(days=1), '\n\n')
        time.sleep(timeout)