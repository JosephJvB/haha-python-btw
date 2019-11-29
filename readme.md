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

### Features
1. Handle user of the day
    - get all users who have been user from redis db
    - get all users from discord with active role
    - filter all users, removing users from redis list
    - choose next user at random (or write an ALGORITHM :oo)
    - look for user with current role = UOTD_ROLE
    - remove current user
    - add next user
    - save next user to db
    - send messages for leaving and entering users

### env vars
- bot-token
- uotd-role-id
- redis-url
- off-topic-channel-id

### tech
- heroku
- cronjob
- redis