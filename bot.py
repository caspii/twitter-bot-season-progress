# TODO:
# - current_season variable should be set automatically
# - season_start dict should not use year

import os
from datetime import date
from math import floor
import tweepy
from dotenv import load_dotenv

load_dotenv(".env")

client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

seasons = [
    "autumn",
    "winter",
    "spring",
    "summer",
]

current_season = 2

season_start = [
    date(2022, 9, 22),  # Autumn
    date(2022, 12, 22), # Winter
    date(2023, 3, 20),  # Spring
    date(2023, 6, 21),  # Summer
    ]

season_total_days = 90
days_into_season = (date.today() - season_start[current_season]).days
season_days_left = 90 - days_into_season

print(f"Let's do this! {season_days_left=} {days_into_season=}")

if season_days_left < 0:
    print("Season is over!")
if season_days_left == 0:
    #tweet = f"Summer is complete! It's Autumn now 🍁🍂☀☔️️"
    tweet = f"Spring is complete! It's Summer now 🌻⛱️🐝️"

elif season_days_left > 0:
    percent_done = days_into_season / season_total_days
    progress = ""
    for i in range(0, 10):
        if i < floor(percent_done * 10):
            progress += "🟩"
        else:
            progress += "⬜️"
    progress += f" { round(percent_done * 100, 1) }% complete"
    tweet = f"There are {season_days_left} days of {seasons[current_season]} left\n"
    tweet += progress
else:
    exit(0)

print(tweet)

response = client.create_tweet(text=tweet)
if response.errors:
    print("Tweeting failed")
else:
    print("Tweeted successfully")
