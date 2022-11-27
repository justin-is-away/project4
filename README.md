# Project 4: Reddit Bots

# Politician Support / Opposition #

My bot is opposing Donald Trump.

# Favorite Thread #

[This](https://www.reddit.com/r/cs40_2022fall/comments/z364a3/trump_support_among_republicans_flat_since/ixkmk46/?context=3) is my favorite thread involving my bot. I like how chaotic the chain of replies are. It starts with a huge, detailed paragraph, which is followed by a tame statment, and then a non sequitur motivation quote, and then my comment which most definitely doesn't make any sense either. I personally find this hilarious because of it's absurdity.

![screenshotofthread](https://github.com/justin-is-away/project4/blob/main/favthread.PNG)

# Scoring 

I completed each task in `bot.py` for 12 points. 

I also completed the github repo, stated the candidate my bot supports, and posted my favorite thread, for 3 points.

I got 804 valid comments for 6 points. Running `bot_counter.py` file on backpagebot gives: 
```
len(comments)= 1000
len(top_level_comments)= 146
len(replies)= 854
len(valid_top_level_comments)= 104
len(not_self_replies)= 818
len(valid_replies)= 700
========================================     
valid_comments= 804
========================================     
NOTE: the number valid_comments will be used 
to determine your grade
```
I created `bot_submissions.py` and posted at least 200 text or link posts (mainly from r/conservative, but some from r/liberal) for 2 points. 

I created a total of five bots ([backpagebot](https://www.reddit.com/user/backpagebot), [backpagebot1](https://www.reddit.com/user/backpagebot1), [backpagebot2](https://www.reddit.com/user/backpagebot2), [backpagebot3](https://www.reddit.com/user/backpagebot3), [backpagebot4](https://www.reddit.com/user/backpagebot4) that each have posted at least 500 comments, for 2 points.

I implemented a piece of code in my bot.py file that replies to the most upvoted comment rather than a random one, for 2 points. 
```
highest = 0
for c in comments_without_replies:
  if c.score >= highest:
    highest = c.score
    to_reply = c 
to_reply.reply(generate_comment())
```

I created `bot_vote.py` and implemented TextBlob to downvote all posts and comments relating to Donald Trump, and upvote most posts and comments relating to Joe Biden, for 4 points.

Final score: 12 + 3 + 6 + 2 + 2 + 2 + 4 = 31/30 points.
