from bs4 import BeautifulSoup
import requests
from flask import Flask
import pymongo
from models.hacker_news import HackerNews
import json
from hacker_news_user import get_hacker_news_user, get_hacker_news_users

users = []
for page in range(1, 51, 1):
    URL = None
    if page == 1:
        URL = "https://news.ycombinator.com/news"
    else:
        URL = f"https://news.ycombinator.com/news?p={page}"

    response = requests.get(URL)
    if response.status_code == 200:
        # load the html data from the given url and parse it using html.parser
        soup = BeautifulSoup(response.text, "html.parser")

        # get all titles
        titles = soup.select(".titleline > a")

        # get all the users urls
        users_urls = soup.select(".sitestr")

        # get all the users url link
        user_url_links = soup.select(".hnuser")

        # get all the posts links
        posts_links = soup.select(".titleline > a")

        # get all the votes
        votes = soup.select(".subline > .score")

        # get all the authors
        authors = soup.select(".hnuser")

        # get all the timestamps
        timestamps = soup.select(".age > a")

        # get all the comments
        comments = soup.select(".subline > a:nth-child(6)")

        users.extend(
            get_hacker_news_users(
                titles,
                users_urls,
                user_url_links,
                posts_links,
                votes,
                authors,
                timestamps,
                comments,
            )
        )
    else:
        print(f"Response.status_code = {response.status_code}")
        break


counter = 1
for user in users:
    print(counter, user)
    counter += 1
    print()
