from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel  # pylint:disable=no-name-in-module


class ArticleSchemaReponse(BaseModel):
    """article response schema"""
    id: Optional[UUID]  # pylint: disable=invalid-name
    title: str
    url: str
    summary: str
    featured: bool
    image_url: str
    news_site: str
    published_at: datetime
    updated_at: datetime

    class Config:
        """orm mode"""
        orm_mode = True
