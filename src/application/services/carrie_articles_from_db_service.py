import json
from typing import Type

from ..adapters import RequestAdapter
from ..repositories import ArticleRepositoryInterface
from ...domain.adapter.article_adapter import ArticleAdapter


class CarrieArticlesFromDbService:
    """carrie all articles to my db"""

    def __init__(self, articles_repository: Type[ArticleRepositoryInterface]) -> None:
        self.__articles_repository = articles_repository

    async def execute(self, url: str):
        """service entrypoint"""
        async with RequestAdapter.get_stream(url, 5) as resp:
            for article_chunk in resp.iter_lines():
                str_to_json = json.loads(article_chunk.decode('utf-8'))
                for index, article in enumerate(str_to_json):
                    print("Inserting: ", index + 1)
                    await self.__articles_repository.create(
                        ArticleAdapter.create(
                            article.get('title'), article.get('summary'),
                            article.get('newsSite'), article.get('featured'),
                            article.get('imageUrl'), article.get('url')
                        )
                    )
