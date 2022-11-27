from dataclasses import dataclass


@dataclass
class ArticleRequestDto:
    """article data transaction object"""
    title: str
    url: str
    summary: str
    featured: bool
    image_url: str
    news_site: str
