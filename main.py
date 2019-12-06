import os
import requests
from client import Client

if __name__ == '__main__':
    try:
        c = Client()
        c.run()
    except Exception as e:
        u = os.getenv('hook')
        j = os.getenv('joe')
        d = {
            'content': f'<@{j}> ERROR: {e.args}'
        }
        requests.post(u, data=d)