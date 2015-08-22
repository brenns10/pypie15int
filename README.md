# Python and Pie 2015: Intermediate

## Welcome

- I'm Stephen, a senior and a member of HacSoc.
- Today I'll teach you how to do something cool: write a Twitter bot in Python.
- This course is for "intermediates" in Python 3.  That means you should know
  the following:
    - How to install and run Python.
    - How to write & run simple scripts.
    - Variables, if statements, for loops, functions.
    - Simple Python variable types - numbers, strings, lists, dicts.
    - Maybe even classes (you don't need to use classes if you don't want to).
- In this course, you'll learn:
    - How to install Python packages.
    - How to use the Twitter API.
- We'll be using Python 3, not 2.  If you don't have it installed, we'll do that
  first.

Hopefully, you should already have Python 3 installed, along with pip.

## Getting a Twitter Library

Libraries are really important for programmers.  We can't do everything
ourselves, so we have to use code that other people have written.  Instead of
figuring out how to control Twitter all by ourselves in Python, we can install a
library to help us.

Python comes with a library package manager called pip (which stands for "pip
installs Python").  It's a command line program, so you'll need to open up your
command line (on Mac OS X: Terminal.app, on Windows: Command Prompt, on Linux:
Terminal).  This command should install a library that will help us access
Twitter from Python:

    pip install twitter

If you're on a Mac or Linux, you'll probably need to use `sudo`.  On Linux you
may also want to use `pip3` instead of just `pip`.  On Windows, you may need to
have your command prompt window in a special folder in order to use pip.

You'll know that it worked if you can open Python (using IDLE for instance) and
run the following code without getting an `ImportError`:

```python
import twitter
```

## Start Your Bot

You'll want to create a folder to keep all of your code in for this bot.  In
this folder, you should create two Python files: one called `secrets.py`, and
one called `bot.py`.  The `secrets.py` file will contain a few variables that
are "secret" (similar to passwords).  Generally, it's good practice to keep your
"secrets" in a file that's separate from the rest of your code.  So, the
`bot.py` file will contain all the actual code for the bot.  You'll be able to
access all the variables in the `secrets.py` file by including the following
line in `bot.py`:

```python
from secrets import *
```

When you're playing around with the Twitter API in IDLE, you'll also be able to
do that same line, and get your secrets loaded so that you don't have to copy
and paste them every time you want to log into Twitter.  Very convenient.

## Getting Started With the Twitter API

So, what are all these secrets, and where to we get them?

In order to use the Twitter API, you need to be able to "log into" it.
Basically, Twitter wants to know who is using its API, so it can yell at you if
you misuse it.  You can get access to the Twitter API by creating a Twitter
App - this gives you something called an API key and an API secret, which you
can use to "authenticate" with Twitter.

The other thing you'll need to have (if you want to use the Twitter API to
tweet) is access to a Twitter account to tweet from.  So, you're probably going
to want to create an account for your bot (unless you're okay with using your
personal Twitter account for your bot).  So, do that first.  If you'd rather not
create a second account, and you're OK with having your bot tweet all over your
Twitter account, you can skip this.

Once you're logged into the Twitter account you want to use, go to
<https://apps.twitter.com>, and click "Create an App."  Fill it in with a name
and description (and a dummy website - <http://example.com> works well for that
purpose).  Once you've created the app, you'll be presented with a webpage full
of options about your app.

Go to the Keys and Access Tokens tab of this webpage.

You'll want to copy and paste the "Consumer Key" and "Consumer Secret" into your
`secrets.py`.  Name them `API_KEY` and `API_SECRET` respectively.

Then, click the button to generate an access token, and copy "Access Token" and
"Access Token Secret" into your `secrets.py`.  Name them `ACCESS_TOKEN` and
`ACCESS_TOKEN_SECRET` respectively.

In the end, your `secrets.py` will look something like this:

```python
API_KEY = 'Consumer Key Here'
API_SECRET = 'Consumer Secret Here'
ACCESS_TOKEN = 'Access Token Here'
ACCESS_TOKEN_SECRET = 'Access Token Secret Here'
```

## Your First Tweet

If you've made it so far, congratulations!  You've made it through the boring
part.  Now you have all the tools you need to start using Twitter.  Let's try
it!  Pop open a Python shell (either in the command line, or an IDLE, your
choice).  First, import your secrets:

```python
from secrets import *
```

If that doesn't work, Python isn't sitting in the right directory.  You'll need
to instruct it to move into the directory you saved your code in.  You can do
that with these lines (don't bother if your secrets imported correctly):

```python
import os
os.chdir(r'Path/to/your/code/folder/here')
``

Importing your secrets should work fine now.  Next, let's import everything from
the Twitter library:

```python
from twitter import *
```

And now we can create a variable that will let us access the Twitter API.  In
order to do that, we need to provide all our secrets.  We'll save it in a
variable named `t`:

```python
t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, API_KEY, API_SECRET))
```

All of the `auth=OAuth(...)` stuff is how we authenticate with Twitter.

From, here, you can make a tweet by doing:

```python
t.statuses.update(status='Hello, world!')
```

If you look at your bot's Twitter page, you'll see your first Tweet!

