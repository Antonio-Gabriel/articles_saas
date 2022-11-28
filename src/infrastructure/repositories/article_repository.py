# pylint: disable=trailing-whitespace
from sqlalchemy import select, and_, update, delete

from ..factory import DbConnectionFactory
from ..models.article_model import ArticleModel

from ...domain.entities import Article
from ...application.repositories import ArticleRepositoryInterface


class ArticleRepository(ArticleRepositoryInterface):
    """article repository"""

    async def create(self, article: Article) -> Article:
        """create new article"""

        article_model = ArticleModel(
            id=article.get_id, title=article.props.title,
            summary=article.props.summary, featured=article.props.featured,
            url=article.props.url, image_url=article.props.image_url,
            news_site=article.props.news_site
        )

        async with DbConnectionFactory.create() as session_db:
            session_db.add(article_model)
            await session_db.commit()

        return article

    async def get(self) -> list:
        """get all articles"""

        async with DbConnectionFactory.create() as session_db:
            query = select(ArticleModel)

            result = await session_db.execute(query)

        return result.fetchall()

    async def get_by_id(self, article_id: str) -> list:
        """get article by id"""

        async with DbConnectionFactory.create() as session_db:
            query = select(ArticleModel).where(and_(
                ArticleModel.id == article_id
            ))

            result = await session_db.execute(query)

        return result.fetchone()

    async def update(self, article: Article) -> Article:
        """update article"""

        async with DbConnectionFactory.create() as session_db:
            query = update(ArticleModel).where(and_(
                ArticleModel.id == article.get_id
            )).values(
                title=article.props.title, summary=article.props.summary,
                featured=article.props.featured, url=article.props.url,
                image_url=article.props.image_url, news_site=article.props.news_site
            )

            await session_db.flush()
            await session_db.execute(query)
            await session_db.commit()

        return article

    async def delete(self, article_id: str) -> Article:
        """get article by id"""

        async with DbConnectionFactory.create() as session_db:
            query = delete(ArticleModel).where(and_(
                ArticleModel.id == article_id
            ))

            await session_db.flush()
            await session_db.execute(query)
            await session_db.commit()

        return True
