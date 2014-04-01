subreddit="loans"
import csv
scammers=[]
read=csv.reader(open('bhw_usernames_passwords_sample.csv','r'))
for item in read:
scammers.append(item[0])
message="""


 Hello! I am /u/loanBot . I am here to tell you that the poster is a known scammer


 """ #Edit the text between the """ and the other """ for the message. Use reddit formatting
username="GITHUB"
password="GITHUB"
import praw
from pprint import pprint

r=praw.Reddit(user_agent='/r/loans bot by /u/scamlist')
r.login(username,password)
submissions=r.get_subreddit(subreddit).get_new()
for submission in submissions:
    if submission.author.name in scammers:
        done=0
        for comment in submission.comments:
            print(comment.author.name)
            if comment.author.name==username:
                done=1
        if done==0:
            submission.add_comment(message)
            print("SCAMMER!")