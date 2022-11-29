import asyncio

from bootstrap import *  # pylint: disable=unused-wildcard-import, wildcard-import
from src.presenters.controllers.carrie_articles_controller import (
    CarrieArticleController
)

article_controller = CarrieArticleController()

if __name__ == "__main__":
    asyncio.run(article_controller.handle())
