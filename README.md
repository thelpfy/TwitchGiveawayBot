# TwitchGiveawayBot
Quick and Dirty Bot

# Setup
## Python
pip install pipenv

Run ⇒ \
  &nbsp;pipenv --python 3.6 or pipenv --python 3.7\
  &nbsp;pipenv install twitchio\
  &nbsp;pipenv install telegram_send
  
  pipenv shell\
   &nbsp;telegram-send --configure  (follow instructions)\
   &nbsp;exit
   
## Lines to change in bot.py
8  ⇒ https://twitchapps.com/tmi/ \
9  ⇒ https://dev.twitch.tv/console/apps/create (Create an Application with your oauth and get the client-id) \
10 ⇒ Twitch Username \
12 ⇒ Twitch Channel (the name after: twitch.tv/) \
32 ⇒ Twitch Username \
36 ⇒ Twitch Username

  
# Start the Bot
pipenv run python bot.py
## For Server (Background)
pipenv run python bot.py &

