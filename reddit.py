import praw

#Fill in client_id & client_secret
reddit = praw.Reddit(client_id="      ",
                     client_secret='      ',
                     user_agent='sumac')

#get 10 submissions from hot
#print url and id number
subreddit = reddit.subreddit('politics')
for submission in subreddit.hot(limit=10):
    print submission.url
    print submission.id
    
#Get comments from submission  
#URL guidelines ('https://www.reddit.com/r/subreddit/comments/ID/page
submission = reddit.submission(url='https://www.reddit.com/r/politics/comments/6r5obm/rex_tillerson_rejects_80m-congress_fight-russian_propaganda-because_it_would_645554')
for top_level_comment in submission.comments:
    print(top_level_comment.body) + "\n"
    

