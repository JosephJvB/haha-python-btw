# Bot for wallride discord

### Todo
- !codes command: which codes do I need to return? : current ones I guess :p
    - Is my bot still authed to be in Lucio Surfing? I could use it to read latest codes from there
    - What else would be useful, leaderboard command. And some kind of vault for best rollouts by map. I dunno

- social credits system. Everyone gets one point a day to give to anyone that is not themselves
    - Can DM bot direct with '{user}#{discriminator}' to assign a point
    - Lookup requesting user in redis db
    - if users last timestamp is within 24hrs, exit
    - if not, find the user who they want to assign to
    - if user not found, exit, if more than 1 user, ask for a specific user id
    - if just one user found, add point to them and update timestamp. I wonder if this is a task for a sql database? Anyway..

### revisit:
it SEEMS like the discord.py package isn't what I want. It's all about registering listeners on events.
What I want is a script to run once a day, as cron job.
What I really want is:
- Auth with discord using token
- Get a guild
- Get all users in guild
- Get user with role in guild: user1
- Choose a random user from the guild who isnt user1: user2
- remove role from user1, put on user2
- send messages to channel in guild
- I'll do it with the WEB API, stuff this tricky bot async event looping business, frankly
    - https://discordapp.com/developers/docs/resources/
    - this seems fun: https://discordapp.com/developers/docs/resources/channel#trigger-typing-indicator

### todo:
- redis

### tech
- heroku
- cronjob