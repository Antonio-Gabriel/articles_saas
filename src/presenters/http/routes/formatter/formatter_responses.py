def format_articles_responses(articles: list):
    """articles responses"""
    return [dict(
            id=article["ArticleModel"].id,
            title=article["ArticleModel"].title,
            url=article["ArticleModel"].url,
            summary=article["ArticleModel"].summary,
            featured=article["ArticleModel"].featured,
            image_url=article["ArticleModel"].image_url,
            news_site=article["ArticleModel"].news_site,
            published_at=article["ArticleModel"].published_at,
            updated_at=article["ArticleModel"].updated_at
            ) for article in articles]
