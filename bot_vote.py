import praw
import argparse
import time
from textblob import TextBlob

parser = argparse.ArgumentParser(description='which bot do you want to use')
parser.add_argument('--username', default='')
args=parser.parse_args()
reddit = praw.Reddit('backpagebot' + args.username)
name='backpagebot' + args.username
posts=0
comments=0

for post in list(reddit.subreddit("cs40_2022fall").hot(limit=100)):
    if 'trump' in post.title.lower():
        post_text = TextBlob(post.title)
        post_pol = post_text.sentiment.polarity
        if post_pol:
            post.downvote();
            print('downvoted trump post')
            post+=1
            print(posts)
    if 'biden' in post.title.lower():
        post_text = TextBlob(post.title)
        post_pol = post_text.sentiment.polarity
        post+=1
        if post_pol >= 0.0:
            post.upvote();
            print('upvoted biden post')
        else:
            post.downvote();
            print('downvoted biden post')
        print(posts)

    for comment in post.comments.list():
        if 'trump' in comment.body.lower():
            comment_text=TextBlob(comment.body)
            comment_pol=comment_text.sentiment.polarity
            if comment_pol:
                comment.downvote()
                print('downvoted trump comment')
                comments+=1
                print(comments)
        if 'biden' in comment.body.lower():
            comment_text=TextBlob(comment.body)
            comment_pol=comment_text.sentiment.polarity
            comments+=1
            if comment_pol >= 0.0:
                comment.upvote()
                print('upvoted biden comment') 
            else:
                comment.downvote();
                print('downvoted biden comment')
            print(comments)
        