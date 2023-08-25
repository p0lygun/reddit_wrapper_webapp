from fastapi import APIRouter, HTTPException
from loguru import logger
from yarl import URL

from ....session_manager import Manager
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
                            "link": f"https://www.reddit.com{post_data['permalink']}",
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


# pseudo cache
cache = {}


@reddit_router.get("/subreddit/{subreddit_name}")
async def list_subreddit_posts(subreddit_name: str, limit: int = 10):
    """List the latest 10 posts from a subreddit"""
    query = f"{subreddit_name}-{limit}"
    if query in cache:
        return cache[query]
    session = Manager.get_session()
    request_url = URL(
        f"https://www.reddit.com/r/{subreddit_name}/new.json?sort=new&limit={limit}"
    )
    logger.debug(request_url)
    resp = await session.get(request_url)
    logger.debug(resp.status)
    if resp.status == 404:
        logger.warning(f"{subreddit_name} is a banned subreddit")
        raise HTTPException(status_code=404, detail=await resp.json())

    if request_url != resp.url:
        logger.warning(f"{subreddit_name} not found")
        raise HTTPException(
            status_code=404,
            detail={
                "reason": "subreddit not found",
                "message": "not found",
                "req_url": str(request_url),
                "red": str(resp.url),
            },
        )

    data = await resp.json()
    cache[query] = {
        "subreddit_name": subreddit_name,
        "x-ratelimit-remaining": resp.headers["x-ratelimit-remaining"],
        "x-ratelimit-used": resp.headers["x-ratelimit-used"],
        "x-ratelimit-reset": resp.headers["x-ratelimit-reset"],
        "posts": await clean_data(data),
    }

    return cache[query]
