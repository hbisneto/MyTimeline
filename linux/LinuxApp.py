"""
LinuxApp.py

- This file is used to implement code used to run scripts for Linux
"""
## LinuxApp File
## This file is used to implement code used to run scripts for Linux

import Twitter
from exception import Exceptions
from linux import FileSystem

def Run():
   try:
      public_tweets = Twitter.API.home_timeline()
      for tweet in public_tweets:
         print(tweet.text)
   except:
      print("="*80)
      print(">> Something went wrong. Verify your keys and try again.")
      print("="*80)
      pass