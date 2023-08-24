from fastapi import FastAPI

from .routers import reddit

app = FastAPI()
app.include_router(reddit.reddit_router)
