# pylint: disable=trailing-whitespace
import pytest

from src.infrastructure.repositories import ArticleRepository


@pytest.mark.asyncio
@pytest.mark.skip
async def test_article_repository_get_method():
    """should be return a list

    if you wanna test this endpoint alter environ url on 
    infrastructure/database/postgres/db_connection_handler to

    "postgresql+asyncpg://postgres:articlepwd@localhost:5432/article_db"
    """

    repository = ArticleRepository()
    result = await repository.get()

    assert isinstance(result, list)
