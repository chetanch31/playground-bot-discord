import praw 
import random
from bot_tokens import reddit_client_id, reddit_client_secret

reddit = praw.Reddit(
        client_id= reddit_client_id ,
        client_secret=reddit_client_secret,
        user_agent='pythonpraw' )

def get_dank_meme_list():
    subreddit = reddit.subreddit('dankmemes')

    hot_sub = subreddit.hot()
    memes = []
    for post in hot_sub:
        if not post.stickied:
            memes.append(post)

    return memes

def get_meme_list():
    subreddit = reddit.subreddit('memes')
    hot_sub = subreddit.hot()
    memes = []
    for post in hot_sub:
        if not post.stickied:
            memes.append(post)

    return memes

def dark_joke():
    subreddit = reddit.subreddit('darkjokesunlocked')
    hot_sub = subreddit.hot()
    arr = []
    for submission in hot_sub:
        arr.append(submission)
    rand_joke = random.choice(arr)

    return rand_joke.title, rand_joke.selftext

def get_dark_meme():
    subreddit = reddit.subreddit('darkmeme')
    hot_sub = subreddit.hot()
    memes = []
    for post in hot_sub:
        if not post.stickied:
            memes.append(post)

    return memes

