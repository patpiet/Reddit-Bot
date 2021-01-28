import praw
import pdb
import re
import os
# Create A Folder
if not os.path.isfile("posts_to_read.txt"):
    urls_to_read = []
else:
# Read the txt file
    with open("posts_to_read.txt", "r") as f:
        urls_to_read = f.read()
        urls_to_read = urls_to_read.split("\n")
        urls_to_read = list(filter(None, urls_to_read))

# Take inputs from user
subreddit_name = input("What subreddit do you want to search in: ")
key_word = input("What's the keyword: ")

isOn = True
while isOn:
    # praw Configuration
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(subreddit_name).hot()
    for submission in subreddit:
        if key_word in submission.title.lower():
            if submission.url not in urls_to_read:
                print("New post added!")
                print(f"""
Title: {submission.title}
Url:{submission.url}
Score: {submission.score}
                      """)
                # Add url to txt file
                urls_to_read.append(submission.url)
                with open("posts_to_read.txt", "w") as f:
                    for post_url in urls_to_read:
                        f.write(post_url + "\n")


