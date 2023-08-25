if True:
    from dotenv import load_dotenv

    print("ENVS LOADED ", load_dotenv(verbose=True))

from uvicorn import Config, Server

from .utils import LOG_LEVEL, setup_logging


def deploy():
    """Deploy the FastAPI app."""
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
