# Bot for wallride discord

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