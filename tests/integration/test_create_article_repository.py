# pylint: disable=C0303
import pytest

from src.domain.adapter.article_adapter import ArticleAdapter
from src.infrastructure.repositories import ArticleRepository


@pytest.mark.asyncio
@pytest.mark.skip
async def test_create_article_repository():
    """should be return a entity

    if you wanna test this endpoint alter environ url on 
    infrastructure/database/postgres/db_connection_handler to

    "postgresql+asyncpg://postgres:articlepwd@localhost:5432/article_db"
    """

    article = ArticleAdapter.create(
        title="SpaceX launches new cargo Dragon spacecraft to space station",
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov.",
        news_site="SpaceNews",
        featured=False,
        image_url="https://spacenews.com/wp-content/uploads/2022/11/crs26-launch.jpg",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
    )

    repository = ArticleRepository()
    result = await repository.create(article)

    assert result.props.news_site == "SpaceNews"
