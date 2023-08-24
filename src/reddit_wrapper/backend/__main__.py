import uvicorn


def deploy():
    """Deploy the FastAPI app."""
    uvicorn.run("reddit_wrapper.backend:app", host="0.0.0.0", port=8787, reload=True)


if __name__ == "__main__":
    deploy()
