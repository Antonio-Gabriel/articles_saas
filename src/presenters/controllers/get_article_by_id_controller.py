from typing import Type, Optional

from .handler import ControllerBase, Request
from ...application.usecases import GetArticleByIdUsecase
from ...infrastructure.repositories import ArticleRepository


class GetArticleByIdController(ControllerBase):
    """articles controller"""

    async def handle(self, request: Optional[Type[Request]] = None):
        """controller handling"""
        articles_usecase = GetArticleByIdUsecase(ArticleRepository())
        articles = await articles_usecase.execute(request.params[0])
        return articles
