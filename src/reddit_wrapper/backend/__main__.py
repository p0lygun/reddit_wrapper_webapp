from dotenv import load_dotenv
from uvicorn import Config, Server

from .utils import LOG_LEVEL, setup_logging


def deploy():
    """Deploy the FastAPI app."""
    print("ENVS LOADED ", load_dotenv(verbose=True))
    server = Server(
        Config(
            "reddit_wrapper.backend:app",
            host="0.0.0.0",
            log_level=LOG_LEVEL,
            port=8787,
            reload=True,
        ),
    )

    setup_logging()

    server.run()


if __name__ == "__main__":
    deploy()
