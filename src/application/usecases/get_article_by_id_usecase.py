# pylint: disable=too-few-public-methods
from typing import Type

from ..factory import LogFactory
from ..repositories import ArticleRepositoryInterface


class GetArticleByIdUsecase:
    """Articles usease"""

    def __init__(self, articles_repository: Type[ArticleRepositoryInterface]) -> None:
        self.__articles_repository = articles_repository

    async def execute(self, article_id: str) -> list:
        """get article by id"""
        (LogFactory.create()).set_log(f"finding article {article_id}", "info")
        return await self.__articles_repository.get_by_id(article_id)
