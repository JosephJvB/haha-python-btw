# Bot for wallride discord

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