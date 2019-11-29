import os
import random
from discord_api import Discord_Api

class Client(Discord_Api):
    def __init__(self):
        super(Client, self).__init__()
        self.all_members = []
        self.prev = None
        self.next = None

    def run(self):
        self.get_all_members()
        self.get_prev_uotd()
        self.get_next_uotd()
        self.finale()
        return

    def get_all_members(self):
        m = [] 
        go_agane = True
        while go_agane: # python doesnt have do/while
            last_id = 0 if not len(m) > 0 else m[-1]['user']['id']
            r = self.req_members(after=last_id)
            m += r
            go_agane = len(r) == 1000 # if len is less that 1000, we are done
        print(f'got {len(m)} members')
        self.all_members = m
        return m

    def get_prev_uotd(self):
        r = os.getenv('uotd')
        p = [u for u in self.all_members if r in u['roles']]
        self.prev = None if len(p) == 0 else p[0]
        return p

    def get_next_uotd(self):
        l = self.all_members
        if(self.prev):
            l.remove(self.prev)
        r = os.getenv('active')
        l = [u for u in l if r in u['roles']]
        n = random.choice(l)
        self.next = n
        return n

    def finale(self):
        if(self.prev):
            self.req_remove_user_role(self.prev)
            self.req_post_msg(f'<@{self.prev["user"]["id"]}> is gone!')
        self.req_add_user_role(self.next)
        self.req_post_msg(f'<@{self.next["user"]["id"]}> is up next!')
        return