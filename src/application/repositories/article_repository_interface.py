from abc import ABC

from ...domain.entities import Article


class ArticleRepositoryInterface(ABC):
    """article repository interface"""

    async def create(self, article: Article) -> Article:
        """create new article"""

        raise NotImplementedError("Method not implemented")

    async def get(self) -> list:
        """get all articles"""

        raise NotImplementedError("Method not implemented")

    async def get_by_id(self, article_id: str) -> list:
        """get article by id"""

        raise NotImplementedError("Method not implemented")

    async def update(self, article: Article) -> Article:
        """update article"""

        raise NotImplementedError("Method not implemented")

    async def delete(self, article_id: str) -> Article:
        """get article by id"""

        raise NotImplementedError("Method not implemented")
