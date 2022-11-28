# pylint: disable=too-few-public-methods
from typing import Type

from ..repositories import ArticleRepositoryInterface


class GetArticlesUsecase:
    """Articles usease"""

    def __init__(self, articles_repository: Type[ArticleRepositoryInterface]) -> None:
        self.__articles_repository = articles_repository

    async def execute(self) -> list:
        """get all articles"""

        return await self.__articles_repository.get()
