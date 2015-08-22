#!/usr/bin/env python3
"""Bot that replies to any @mention with Taylor Swift lyrics."""

from twitter import Twitter, TwitterStream, OAuth
import random

# API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET come from here!
from secrets import *

USERNAME = 'pypie15bot'
LYRICS = 'taylor.txt'


def main():

    # open up a file and get a list of lines of lyrics
    with open(LYRICS) as lyrics_file:
        lyrics = [line for line in lyrics_file if line != ""]

    # get twitter api ready
    auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
    t = Twitter(auth=auth)
    ts = TwitterStream(domain='userstream.twitter.com', auth=auth)

    stream = ts.user()

    for tweet in stream:

        # If this was a tweet by someone other than the bot.
        if 'text' in tweet and tweet['user']['screen_name'] != USERNAME:

            # Pick a lyric, compose a reply, and send it!
            line = random.choice(lyrics)
            reply = '@' + tweet['user']['screen_name'] + ' ' + line
            t.statuses.update(status=reply, in_reply_to_status_id=tweet['id'])


# run main() when this script is called
if __name__ == '__main__':
    main()
