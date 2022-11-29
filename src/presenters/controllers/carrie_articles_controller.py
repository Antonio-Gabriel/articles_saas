from typing import Type, Optional

from .handler import ControllerBase, Request

from ...infrastructure.repositories import ArticleRepository
from ...application.services import CarrieArticlesFromDbService


class CarrieArticleController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""

        article_usecase = CarrieArticlesFromDbService(ArticleRepository())
        await article_usecase.execute("https://api.spaceflightnewsapi.net/v3/articles")
