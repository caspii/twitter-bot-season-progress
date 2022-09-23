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
    "spring",
    "summer",
    "winter",
]

current_season = 0

# Winter still missing, because this bot is les than 3 seasons old

season_start = [
    date(2022, 9, 22),  # Autumn
    date(2022, 3, 20),  # Spring
    date(2022, 6, 21),  # Summer
    ]

season_end = [
    date(2022, 12, 21),  # Autumn
    date(2022, 6, 21),  # Spring
    date(2022, 9, 22),  # Summer
    ]

season_total_days = 90
current_delta_days = (date.today() - season_start[current_season]).days
season_days_left = (season_end[current_season] - date.today()).days

print(f"Let's do this! {season_days_left=}")

if season_days_left == 0:
    tweet = f"Summer is complete! It's Autumn now 🍁🍂☀☔️️"

elif season_days_left > 0:
    percent_done = current_delta_days / season_total_days
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
