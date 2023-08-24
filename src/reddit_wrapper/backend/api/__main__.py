from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from ..session_manager import Manager
from .routers import reddit


@asynccontextmanager
async def lifespan(*args, **kwargs):
    """Context manager for the lifespan of the application"""
    logger.info("Starting up")
    Manager()
    yield
    logger.info("Shutting down")
    await Manager.close()


app = FastAPI(lifespan=lifespan)
app.include_router(reddit.reddit_router)
