import random
import praw

reddit = praw.Reddit('backpagebot', user_agent='cs40')
posts=list(reddit.subreddit('liberal').hot(limit=None))

for i in range(200):
    rand_post = random.choice(posts)
    post_title = rand_post.title
    post_selftext=rand_post.selftext
    post_url = rand_post.url
    
    subreddit=reddit.subreddit("cs40_2022fall")

    if post_selftext != '':
        # link posts
        subreddit.submit(post_title, selftext=post_selftext)
    else:
        # self posts
        subreddit.submit(post_title, url=post_url)
    print('new submission')








