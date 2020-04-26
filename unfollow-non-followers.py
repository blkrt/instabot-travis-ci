import os 
import time
import random
from instabot import Bot

bot = Bot(max_unfollows_per_day=100)
bot.login(
    username=os.getenv("INSTAGRAM_USERNAME"), 
    password=os.getenv("INSTAGRAM_PASSWORD"),
)
bot.unfollow_non_followers()
