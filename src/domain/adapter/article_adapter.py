# pylint: disable=too-few-public-methods,too-many-arguments
from typing import Optional
from datetime import datetime
from ..entities import Article, ArticleProps


class ArticleAdapter:
    """article adapter"""

    @staticmethod
    def create(
            title: str, summary: str, news_site: str,
            featured: bool, image_url: str, url: str, _id: Optional[str] = None
    ) -> Article:
        """create article instance"""
        article = Article(ArticleProps(
            title=title,
            summary=summary,
            news_site=news_site,
            featured=featured,
            image_url=image_url,
            url=url,
            published_at=datetime.utcnow,
            updated_at=datetime.utcnow
        ), _id)

        return article
