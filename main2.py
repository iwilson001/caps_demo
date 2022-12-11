import praw
import pandas as pd
from tabulate import tabulate


from IPython.display import display
from pip._internal.utils.misc import tabulate

from yahoo_fin.stock_info import get_data


sobr_daily = get_data("sobr", start_date="11/27/2022", end_date="12/09/2022", index_as_date = True, interval="1d")
sobr_daily


reddit_read_only = praw.Reddit(client_id="jIecQpWnOYUzYOgTmdEsTg",  # your client id
                               client_secret="MF8q2iDGYcsoKY3mta49Lu5frWa5MQ",  # your client secret
                               user_agent="MyBot/0.0.1")  # your user agent

subreddit = reddit_read_only.subreddit("pennystocks")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

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

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
# print(tabulate(top_posts))

display(top_posts)

# top_posts.to_csv("Top Posts.csv", index=True)