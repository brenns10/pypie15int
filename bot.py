#!/usr/bin/env python3
"""Bot that replies to any @mention with Taylor Swift lyrics."""

from twitter import Twitter, TwitterStream, OAuth
from pprint import pprint
import random

# API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_TOKEN_SECRET come from here!
from secrets import *

USERNAME = 'pypie15bot'
LYRICS = 'taylor.txt'


def main():
    # open up a file and get a list of lines of lyrics (no blank lines)
    with open(LYRICS) as lyrics_file:
        lyrics = [line.strip() for line in lyrics_file if line != "\n"]

    # print out our list of lyrics (for diagnostics)
    pprint(lyrics)

    # get twitter api ready
    auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET)
    t = Twitter(auth=auth)
    ts = TwitterStream(domain='userstream.twitter.com', auth=auth)

    # open up our user's stream
    stream = ts.user()

    # iterate through every event
    for tweet in stream:

        # Print it out nicely, so we can see what happens.
        pprint(tweet)

        if 'event' in tweet:
            print('received event %s' % tweet['event'])

        elif 'text' in tweet and tweet['user']['screen_name'] != USERNAME:

            # 'text' means that this is a tweet.  If the screen name wasn't our
            # own, this is someone tweeting at us.

            # print out the important bits
            print('from @%s: %s' % (tweet['user']['screen_name'], tweet['text']))

            # Pick a lyric, compose a reply, and send it!
            line = random.choice(lyrics)
            print('responding with line: %s' % line)
            reply = '@' + tweet['user']['screen_name'] + ' ' + line
            t.statuses.update(status=reply, in_reply_to_status_id=tweet['id'])


# run main() when this script is called
if __name__ == '__main__':
    main()
