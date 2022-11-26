import praw
import random
import datetime
import time
import argparse

# FIXME:
madlibs = [
    "Donald Trump is a very [WEIRD] [CANDIDATE]. I [THINK] he is actually just a [GOBLIN] [IN HIDING].",
    "Donald Trump has a lot of [WEIRD] quirks. He's fluent in [JAPANESE], regularly consumes [CARDBOARD], likes to [WALK] backwards, and self-identifies as a [GOBLIN].",
    "Lots has been said about Donald Trump's [WEIRD] interest in [CARDBOARD]. However, not enough people are talking about his tendency to [WALK] like a [GOBLIN] [IN HIDING].",
    "I don't always [LOVE] what Donald Trump as a person endorses, but I have to respect his [WEIRD] passion for [CARDBOARD]. Honestly, you also have to respect the way he can [WALK] like a [GOBLIN], too.",
    "Donald Trump seems to [LOVE] [CARDBOARD]. I don't know what it is about it, but he's always talking about it. I [THINK] he's a [GOBLIN] [IN HIDING].",
    "I'm voting for Donald Trump because he's a [WEIRD] [CANDIDATE] who [LOVE]s [CARDBOARD]. As a [GOBLIN] [IN HIDING], there's just too many things we hold in common to not [LOVE] him.",
    ]

replacements = {
    'WEIRD' : ['multifacted', 'questionable', 'confusing', 'strange', 'unparalleled', 'interesting'],
    'CANDIDATE' : ['person', 'human being', 'individual', 'entity'],
    'THINK' : ['believe', 'assert', 'claim'],
    'GOBLIN' : ['demon', 'angel', 'Lovecraftian horror', 'god'],
    'IN HIDING'  : ['on the run', 'looking for a friend', 'masquerading as a human'],
    'WALK': ['run', 'stroll', 'read', 'jump'],
    'JAPANESE': ['Russian', 'Spanish','French'],
    'CARDBOARD': ['plastic', 'asphalt','hot sauce','plutonium'],
    'LOVE' : ['love', 'adore', 'like'],
    'STUFF' : ['stuff', 'things', 'fun things']
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('[' + replacement + ']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 

parser = argparse.ArgumentParser(description='which bot do you want to use')
parser.add_argument('--username', default='')
args=parser.parse_args()
reddit = praw.Reddit('backpagebot' + args.username)
name='backpagebot' + args.username

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.

submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yzrosd/this_is_my_submission/'
# submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/yzzcv6/andrew_yang_reflects_on_trumps_twitter_ban_it_was/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
# while True:
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != name:
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            check_reply = True
            for reply in comment.replies:
                if reply.author==name:
                    check_reply=False  
                    break    
            if check_reply:
                comments_without_replies.append(comment)
                

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        try:
            rand=random.choice(comments_without_replies)
            rand.reply(generate_comment())
            try:
                #comment_random.reply(generate_comment())
                # replying to the comment with the most upvotes instead #
                
                highest = 0
                for c in comments_without_replies:
                    if c.score >= highest:
                        highest = c.score
                        to_reply = c 
                to_reply.reply(generate_comment())
                
            except praw.exceptions.APIException:
                print('comment was deleted')
                pass
        except IndexError:
            print('my comments')
            pass


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    next_iteration = list(reddit.subreddit("cs40_2022fall").hot(limit=5))
    submission=random.choice(next_iteration)
    
    time.sleep(1)

    # except praw.exceptions.RedditAPIException as e:
    #     for subexception in e.items:
    #         if subxception.error_type=='RATELIMIT':
    #             error_str=str(subexception)
    #             print(error_str)

    #             if 'minute' in error_str:
    #                 delay=error_str.split('for ')[-1].split(' minute')[0]
    #                 delay=int(delay)*60.0
    #             else:
    #                 delay=error_str.split('for ')[-1].split(' second')[0]
    #                 delay=int(delay)
    #             print("delay=",delay)
    #             time.sleep(delay)
    #             sleep_count+=1
    #             print('sleep count=',sleep_count)