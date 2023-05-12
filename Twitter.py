## Twitter
## Setup and connect you Twitter account here!
# Note: DO NOT share your tokens
## You can generate and regenerate tokens on Twitter Developer Platform

import tweepy
from tweepy import OAuthHandler

## API Key and API Key Secret
ConsumerKey = ""
ConsumerSecret = ""

## Access Token and Access Token Secret
AccessToken = ""
AccessTokenSecret = ""

# ## Authorization
auth = tweepy.OAuth1UserHandler(
    ConsumerKey,
    ConsumerSecret,
    AccessToken,
    AccessTokenSecret
)

# ## Create an API Object
API = tweepy.API(auth, wait_on_rate_limit = True)