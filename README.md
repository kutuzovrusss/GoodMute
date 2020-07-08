# GoodMute
![https://www.python.org/](https://img.shields.io/github/pipenv/locked/python-version/metabolize/rq-dashboard-on-heroku?color=orange&label=Python)
![https://pypi.org/project/discord.py/](https://img.shields.io/badge/discord.py-v1.3.3-brightgreen)

(SQLite3) Mute with writing to the database to protect against mute failure when the bot crashes.

To start you need:
- Install the required library, which is in the access **requirements.txt**
- Create config.py file

#### config.py
```py
TOKEN = "token here"
PREFIX = "!"
```

#### Files Tree:
  - Data - DataBase (SQLite).
  - Modules - Modules (Cogs).
  - Utils - Utilities for convenient work with the bot.
