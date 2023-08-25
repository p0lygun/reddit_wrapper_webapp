import os

if True:
    from dotenv import load_dotenv

    print("ENVS LOADED ", load_dotenv(verbose=True))

from uvicorn import Config, Server

from .utils import LOG_LEVEL, setup_logging


def deploy():
    """Deploy the FastAPI app."""
    server = Server(
        Config(
            "backend:app",
            host=os.getenv("HOST", "0.0.0.0"),
            log_level=LOG_LEVEL,
            port=int(os.getenv("PORT", "8787")),
            reload=True
            if os.getenv("RELOAD_ON_CHANGE", "False").lower() == "true"
            else False,
        ),
    )

    setup_logging()
    server.run()


if __name__ == "__main__":
    deploy()
