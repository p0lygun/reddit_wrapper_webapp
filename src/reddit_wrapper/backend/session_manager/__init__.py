import ssl

import aiohttp


class Manager:
    """Session manager for aiohttp.ClientSession"""

    session = None

    def __init__(self):
        Manager.session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=ssl.create_default_context())
        )

    @staticmethod
    async def close():
        """Close the session"""
        if Manager.session is not None:
            await Manager.session.close()

    @staticmethod
    def get_session() -> aiohttp.ClientSession:
        """Get the session"""
        return Manager.session
