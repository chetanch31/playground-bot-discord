import praw 
import random

reddit = praw.Reddit(
        client_id='iVTEsi_caS6DAA' ,
        client_secret='rrj8GjZ1JZtsNVhssZxZ8k0L5Ig',
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

