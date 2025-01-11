from models.hacker_news import HackerNews


def is_comments(comment):
    try:
        comment = int(comment)
    except Exception as exception:
        comment = "discuss"

    if isinstance(comment, int):
        return f"{comment} comments" if comment > 1 else f"{comment} comment"
    return comment


# single hacker news post
def get_hacker_news_user(
    title, user_url, user_url_link, post_link, vote, author, timestamp, comment
):
    user_link = f"https://news.ycombinator.com/{user_url_link.get("href")}"
    hacker_news = HackerNews(
        title.getText(),
        user_url.getText(),
        user_link,
        post_link.get("href"),
        vote.getText(),
        author.getText(),
        timestamp.getText(),
        is_comments(comment.getText().split("\u00a0")[0]),
    )

    return hacker_news


# hacker news users and their posts
def get_hacker_news_users(
    titles,
    users_urls,
    user_url_links,
    posts_links,
    votes,
    authors,
    timestamps,
    comments,
):
    hacker_news_users = []

    for (
        title,
        user_url,
        user_url_link,
        post_link,
        vote,
        author,
        timestamp,
        comment,
    ) in zip(
        titles,
        users_urls,
        user_url_links,
        posts_links,
        votes,
        authors,
        timestamps,
        comments,
    ):
        current_hacker_news = get_hacker_news_user(
            title,
            user_url,
            user_url_link,
            post_link,
            vote,
            author,
            timestamp,
            comment,
        )

        hacker_news_users.append(current_hacker_news)

    return hacker_news_users
