from fastapi import APIRouter
from loguru import logger

from ...session_manager import Manager
from .response_types import SubredditResponseData

reddit_router = APIRouter(prefix="/reddit", tags=["reddit"])


async def clean_data(data: SubredditResponseData):
    """Remove unnecessary data from the response

    We only care for title, author, creation date, and a link to the original thread of each post.
    """
    posts = []
    try:
        if data["kind"] == "Listing":
            for post in data["data"]["children"]:
                if post["kind"] == "t3":
                    post_data = post["data"]
                    try:
                        cleaned_data = {
                            "title": post_data["title"],
                            "author": post_data["author"],
                            "created_utc": post_data["created_utc"],
                            "link": post_data["url"],
                            "valid": True,
                        }
                        posts.append(cleaned_data)
                    except KeyError as e:
                        logger.error(
                            f"Incorrect data format, unable to find key {e.args[0]}"
                        )
                        continue
    except KeyError as e:
        logger.error(f"Incorrect data format, unable to find key {e.args[0]}")
        pass
    return posts


@reddit_router.get("/subreddit/{subreddit_name}")
async def list_subreddit_posts(subreddit_name: str):
    """List the latest 10 posts from a subreddit"""
    session = Manager.get_session()
    resp = await session.get(
        f"https://www.reddit.com/r/{subreddit_name}/new.json?sort=new&limit=10"
    )
    data = await resp.json()
    return {
        "subreddit_name": subreddit_name,
        "x-ratelimit-remaining": resp.headers["x-ratelimit-remaining"],
        "x-ratelimit-used": resp.headers["x-ratelimit-used"],
        "x-ratelimit-reset": resp.headers["x-ratelimit-reset"],
        "posts": await clean_data(data),
    }
