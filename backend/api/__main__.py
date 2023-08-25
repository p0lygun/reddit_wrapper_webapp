import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["http://localhost:8080", "http://127.0.0.1:8080"]

if extra_origins := os.getenv("CORS_ORIGINS", ""):
    origins += extra_origins.split(",")

logger.info(f"CORS origins are {origins}")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
