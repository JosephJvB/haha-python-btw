import os
import requests

# - Auth with discord using token
# - Get a guild
# - Get all users in guild
# - Get user with role in guild: user1
# - Choose a random user from the guild who isnt user1: user2
# - remove role from user1, put on user2
# - send messages to channel in guild

class Client(object):
    def __init__(self):
        print('hello worldington')
        with requests.Session() as sesh: 
            self.sesh = sesh
            self._base = 'https://discordapp.com/api'
            self._auth = f'Bot {os.getenv("token")}'

    def get_all_members(self): 
        members = []
        r = self.req_members()
        members += r
        while len(r) == 1000:
            last_id = r[-1]['user']['id']
            r = self.req_members(after=last_id)
            members += r
        print(f'got {len(members)} members')
        return members
    
    def req_members(self, after=0):
        h = { 'Authorization': self._auth }
        u = self._base + f'/guilds/{os.getenv("guild")}/members?limit=1000&after={after}'
        r = self.sesh.get(u, headers=h)
        return r.json()

if __name__ == '__main__':
    c = Client()
    c.get_all_members()