import os
from bs4 import BeautifulSoup
import requests
from flask import Flask, Response
from pymongo.mongo_client import MongoClient
from models.hacker_news import HackerNews
import json
from hacker_news_user import get_hacker_news_user, get_hacker_news_users
from dotenv import load_dotenv
from bson.json_util import dumps
from server_errors import http_status_codes

is_loaded_dotenv = load_dotenv()

MONGO_DATABASE_URI = os.environ.get("MONGO_DATABASE_URI")
client = MongoClient(MONGO_DATABASE_URI, tls=True, tlsAllowInvalidCertificates=True)

# create database
database = client.hacker_news_database

# create hacker news collection
database_collection = database.hacker_news_collection

users = []
for page in range(1, 11, 1):

    URL = (
        f"https://news.ycombinator.com/news?p={page}"
        if page >= 2
        else f"https://news.ycombinator.com/news"
    )

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
        print(
            f"Response.status_code = {response.status_code} {http_status_codes[response.status_code]}"
        )
        break


for user in users:
    current_user = {
        "title": user.title,
        "user_url": user.user_url,
        "user_url_link": user.user_url_link,
        "post_link": user.post_link,
        "vote": user.votes,
        "author": user.author,
        "timestamp": user.timestamp,
        "comment": user.comment,
    }

    query = {"title": current_user["title"]}
    if not database_collection.find_one(query):
        database_collection.insert_one(current_user)


app = Flask(__name__)


@app.route("/api/v1.0/hacker_news_posts", methods=["GET"])
def hacker_news_posts():
    posts = list(database_collection.find())
    return Response(dumps(posts), mimetype="application/json")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host="0.0.0.0", port=port)
