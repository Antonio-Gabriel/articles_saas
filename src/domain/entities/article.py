# pylint: disable=too-many-instance-attributes
from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Type, Union

from ..value_objects import UniqueId
from ..adapter import ValidatorAdapter
from ..validators import article_validator_schema


@dataclass
class ArticleProps:
    """article entities"""
    title: str
    url: str
    summary: str
    featured: bool
    image_url: str
    news_site: str
    published_at: datetime
    updated_at: datetime


class Article:
    """article entity"""

    def __init__(self, props: Type[ArticleProps], _id: Optional[str] = None) -> None:
        self.__article_id = UniqueId.new(_id)
        self.props = props

    @property
    def get_id(self) -> str:
        """get id"""
        return self.__article_id

    def validate(self) -> Union[str, dict]:
        """validate entities"""
        is_valid, errs = ValidatorAdapter.validate(
            {
                "title": self.props.title,
                "summary": self.props.summary,
                "news_site": self.props.news_site,
                "featured": self.props.featured,
                "url": self.props.url,
                "image_url": self.props.image_url,
            }, article_validator_schema
        )

        return is_valid, errs

    def __repr__(self) -> str:
        return f"""
            Article(
                id={self.get_id}, title={self.props.title}, summary={self.props.summary}, news_site={self.props.news_site},
                featured={self.props.featured}, url={self.props.url}, image_url={self.props.image_url}, 
                published_at={self.props.published_at}, updated_at={self.props.updated_at}
            )
        """
