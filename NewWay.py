import praw
from IPython.core.display import display
from yahoo_fin.stock_info import get_data
from datetime import date, timedelta
import datetime as dt
import requests
from psaw import PushshiftAPI
import json
import os
import openai
import re
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

# regex for ticker symbols, will be used when searching subreddit titles
regex_for_ticker = "\$[A-Z]{3}[A-Z]?[A-Z]?"

# openai key, delete before pushes
openai.api_key = ""

#start and end date for searches
start_epoch = int(dt.datetime(2022, 11, 27).timestamp())
end_epoch = int(dt.datetime(2022, 12, 9).timestamp())

# reddit connection and connection to Pushshift api
reddit_read_only = praw.Reddit(client_id="jIecQpWnOYUzYOgTmdEsTg",  # your client id
                               client_secret="MF8q2iDGYcsoKY3mta49Lu5frWa5MQ",  # your client secret
                               user_agent="MyBot/0.0.1")  # your user agent
api = PushshiftAPI(reddit_read_only)

# generates submission objects where we can get data from (ex. submission.title)
myList = api.search_submissions(after=start_epoch,
                                before=end_epoch,
                                subreddit='pennystocks',
                                filter=['url', 'author', 'title', 'subreddit'],
                                limit=10,
                                #score='>10',
                                title='$SOBR')

for submission in myList:
    print("Title: " + submission.title + " Body: " + submission.selftext + " Score: " + str(submission.score) + " Url: " + submission.url)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Classify the sentiment in this: {submission.title}",
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Sentiment of the title is: " + response["choices"][0]["text"])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Classify the sentiment in this: {submission.selftext}",
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Sentiment of the body is: " + response["choices"][0]["text"])

sobr_daily = get_data("sobr", start_date="11/27/2022", end_date="12/09/2022", index_as_date=True, interval="1d")
display(sobr_daily.columns[0:2])

# sobr_daily.plot()

# plt.show()






# for x in myList:
#     pprint(vars(x))

    # f = open("wasd.txt", "a")
    # f.write(x)
    # f.close()

for submission in myList:
    print("Title: " + submission.title + " Body: " + submission.selftext + " Score: " + str(submission.score) + " Url: " + submission.url)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Classify the sentiment in this: {submission.title}",
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Sentiment of the title is: " + response["choices"][0]["text"])
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Classify the sentiment in this: {submission.selftext}",
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("Sentiment of the body is: " + response["choices"][0]["text"])

# display(myList[0])

# query = "pennystocks"  # Define Your Query
# query2 = ">10"
# url = f"https://api.pushshift.io/reddit/search/submission/?subreddit={query}&?score={query2}"
# request = requests.get(url)
# json_response = request.json()

# Serializing json
# json_object = json.dumps(json_response, indent=4)

# Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

# f = open("demofile2.txt", "a")
# f.write(json_response)
# f.close()
# display(json_response['data'])

# subreddit = reddit_read_only.subreddit("pennystocks")

# Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)
#
# # Display the title of the Subreddit
# print("Title:", subreddit.title)
#
# # Display the description of the Subreddit
# print("Description:", subreddit.description)

posts = subreddit.top("month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post
    posts_dict["Title"].append(post.title)

    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post
    posts_dict["ID"].append(post.id)

    # The score of a post
    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# top_posts = pd.DataFrame(posts_dict)
# print(tabulate(top_posts))

# display(top_posts)


# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)
#
#
# start_date = date(2021, 12, 11)
# end_date = date(2022, 12, 11)
# for single_date in daterange(start_date, end_date):
#     print(single_date.strftime("%Y-%m-%d"))
