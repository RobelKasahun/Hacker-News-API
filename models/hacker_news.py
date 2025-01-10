import json


class HackerNews:

    def __init__(
        self,
        title=None,
        user_url=None,
        user_url_link=None,
        post_link=None,
        votes=None,
        author=None,
        timestamp=None,
        comment=None,
    ):
        self._title = title
        self._user_url = user_url
        self._user_url_link = user_url_link
        self._post_link = post_link
        self._votes = votes
        self._author = author
        self._timestamp = timestamp
        self._comment = comment

    # Getters and Setters
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def user_url(self):
        return self._user_url

    @user_url.setter
    def user_url(self, user_url):
        self._user_url = user_url

    @property
    def user_url_link(self):
        return self._user_url_link

    @user_url_link.setter
    def user_url_link(self, user_url_link):
        self._user_url_link = user_url_link

    @property
    def post_link(self):
        return self._post_link

    @post_link.setter
    def post_link(self, post_link):
        self._post_link = post_link

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, votes):
        self._votes = votes

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        self._comment = comment

    # title, user_url, post_link, votes, author, timestamp, comment
    def __str__(self):
        return json.dumps(
            dict(
                title=self.title,
                user_url=self.user_url,
                user_url_link=self.user_url_link,
                post_link=self.post_link,
                votes=self.votes,
                author=self.author,
                timestamp=self.timestamp,
                comment=self.comment,
            )
        )
