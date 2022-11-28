import pytest

from src.infrastructure.repositories import ArticleRepository


@pytest.mark.asyncio
async def test_article_repository_get_method():
    """should be return a list"""

    repository = ArticleRepository()
    result = await repository.get()

    assert isinstance(result, list)
