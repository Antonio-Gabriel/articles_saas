import uvicorn
import asyncio  # pylint: disable=wrong-import-order

from main import app as article_saas_api
from src.infrastructure.tasks import app as article_scheduler


class Server(uvicorn.Server):
    """Customized uvicorn.Server

       Uvicorn server overrides signals and we need to include
       Rocketry to the signals."""

    def handle_exit(self, sig: int, frame) -> None:
        article_scheduler.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    """run scheduler and api"""
    server = Server(config=uvicorn.Config(
        article_saas_api, workers=1, loop='asyncio', port=8001, host="0.0.0.0")
    )

    api = asyncio.create_task(server.serve())
    sched = asyncio.create_task(article_scheduler.serve())

    await asyncio.wait([sched, api])

if __name__ == "__main__":
    asyncio.run(main())
