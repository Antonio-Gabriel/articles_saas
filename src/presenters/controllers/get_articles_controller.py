from typing import Type, Optional

from .handler import ControllerBase, Request
from ...application.usecases import GetArticlesUsecase
from ...infrastructure.repositories import ArticleRepository


class GetArticlesController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""
        articles_usecase = GetArticlesUsecase(ArticleRepository())
        articles = await articles_usecase.execute()
        return articles
