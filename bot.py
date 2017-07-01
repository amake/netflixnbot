from __future__ import print_function
import os
import sys
import json
import tweepy
import netflixand

creds_file = 'credentials.json'

credentials = {}

if os.path.isfile(creds_file):
    with open(creds_file) as infile:
        credentials = json.load(infile)
else:
    print('Credentials not found. Run auth_setup.py first.')
    sys.exit(1)

auth = tweepy.OAuthHandler(credentials['ConsumerKey'],
                           credentials['ConsumerSecret'])
auth.set_access_token(credentials['AccessToken'],
                      credentials['AccessSecret'])

api = tweepy.API(auth)

def do_tweet(event, context):
    text = netflixand.random_activity()
    api.update_status(text)
    return text

if __name__ == '__main__':
    print(do_tweet(None, None))
