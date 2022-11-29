from contextlib import asynccontextmanager

import requests

from ..factory import LogFactory


class RequestAdapter:
    """adapter"""

    @classmethod
    @asynccontextmanager
    async def get_stream(cls, url: str, timeout: int):
        """get request"""
        try:
            context_m = requests.session()
            yield context_m.get(url, timeout=timeout, stream=True, headers=None)
        except Exception as ex:  # pylint: disable=broad-except
            log = LogFactory.create()
            log.set_log(
                {
                    "message": "Error occurred when exporting data to the database",
                    "exception": ex.args[0]
                }, "error")
