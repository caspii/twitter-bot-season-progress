## "Season Progress" Twitter bot

This code is behind the [season progress](https://twitter.com/progress_season) Twitter bot. It uses the Tweepy Python 
library and v2 Twitter API.

Setup:

1. Install a virtual environment: `python3.9 -m venv venv/`
2. Activate virtual environment: `source venv/bin/activate`
3. [Get your Twitter API credentials](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api) and create a `.env` file. See next section.
4. Execute bot: `python bot.py`

## Setting up `.env` file

This bot reads your Twitter API v2 credentials from a `.env` file. You must create this file yourself and place it in the same folder as `bot.py`.


The file should look like this:

```
CONSUMER_KEY = "ENTER_YOUR_VALUE_HERE"
CONSUMER_SECRET = "ENTER_YOUR_VALUE_HERE"
ACCESS_TOKEN = "ENTER_YOUR_VALUE_HERE"
ACCESS_TOKEN_SECRET = "ENTER_YOUR_VALUE_HERE"
```



