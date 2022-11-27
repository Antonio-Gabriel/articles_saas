from src.domain.entities import Article
from src.application.repositories import ArticleRepositoryInterface


class FakerArticleRepository(ArticleRepositoryInterface):
    """faker repository"""

    def __init__(self) -> None:
        self.__faker_repository = []

    async def create(self, article: Article) -> Article:
        """create new article"""

        self.__faker_repository.append(article)
        return article

    async def get(self) -> list:
        """get all articles"""

        return self.__faker_repository

    async def get_by_id(self, article_id: str) -> list:
        """get article by id"""

    async def update(self, article: Article) -> Article:
        """update article"""

    async def delete(self, article_id: str) -> Article:
        """get article by id"""
