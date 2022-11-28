#pylint: disable=too-few-public-methods
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, String, Boolean, Text, DateTime

Base = declarative_base()


class ArticleModel(Base):
    """model to article"""

    __tablename__ = "article"

    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(200), nullable=False)
    summary = Column(Text, nullable=False)
    featured = Column(Boolean, default=False)
    url = Column(Text, nullable=False)
    image_url = Column(Text, nullable=False)
    news_site = Column(String(40), nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=current_timestamp())

    def __repr__(self) -> str:
        return f"""
            ArticleModel(
                id={self.id}, title={self.title}, summary={self.summary}, 
                news_site={self.news_site}, featured={self.featured}, url={self.url}, 
                image_url={self.image_url}, published_at={self.published_at}, 
                updated_at={self.updated_at}
            )
        """
