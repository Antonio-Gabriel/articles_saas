# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from typing import Type, Optional, Union

from ..factory import LogFactory
from ..repositories import ArticleRepositoryInterface

from ...domain.entities import Article
from ...domain.common.result import Result


@dataclass
class ResultStructure:
    """structure of result"""
    message: Optional[Union[str, dict, Article]]
    status: int


class DeleteArticleUsecase:
    """delete article usecase"""

    def __init__(self, articles_repository: Type[ArticleRepositoryInterface]) -> None:
        self.__articles_repository = articles_repository

    async def execute(self, article_id: str) -> Result[ResultStructure]:
        """execute delete article usecase"""

        article_exists = await self.__articles_repository.get_by_id(article_id)

        if not article_exists:
            log = LogFactory.create()
            log.set_log(ResultStructure(
                message=f"Article {article_id} filtered not exist!",
                status=404
            ), "error")

            return Result[ResultStructure].fail(ResultStructure(
                message=f"Article {article_id} filtered not exist!",
                status=404
            ))

        resp = await self.__articles_repository.delete(article_id)
        if resp:
            return Result[ResultStructure].ok(ResultStructure(
                message=f"Article {article_id} deleted successfully",
                status=200
            ))
