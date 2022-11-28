# pylint: disable=too-few-public-methods
from dataclasses import dataclass
from typing import Type, Optional, Union

from ..factory import LogFactory
from ..dtos import ArticleRequestDto
from ..repositories import ArticleRepositoryInterface

from ...domain.entities import Article
from ...domain.common.result import Result
from ...domain.adapter.article_adapter import ArticleAdapter


@dataclass
class ResultStructure:
    """structure of result"""
    message: Optional[Union[str, dict, Article]]
    status: int


class CreateArticleUsecase:
    """create article usecase"""

    def __init__(self, articles_repository: Type[ArticleRepositoryInterface]) -> None:
        self.__articles_repository = articles_repository

    async def execute(self, article_data: Type[ArticleRequestDto]) -> Result[ResultStructure]:
        """execute create article usecase"""

        article = ArticleAdapter.create(
            article_data.title, article_data.summary, article_data.news_site,
            article_data.featured, article_data.image_url, article_data.url
        )

        is_valid, err = article.validate()

        if is_valid is False:
            log = LogFactory.create()
            log.set_log(ResultStructure(
                message=err,
                status=400
            ), "error")

            return Result[ResultStructure].fail(ResultStructure(
                message=err,
                status=400
            ))

        resp = await self.__articles_repository.create(article)
        if resp:
            return Result[ResultStructure].ok(ResultStructure(
                message=article,
                status=200
            ))
