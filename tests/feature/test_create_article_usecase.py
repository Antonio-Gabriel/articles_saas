# pylint: disable=line-too-long
import pytest

from src.application.dtos import ArticleRequestDto
from src.application.usecases import CreateArticleUsecase

from .repository import FakerArticleRepository


@pytest.mark.asyncio
async def test_create_article_usecase():
    """should be return status 200"""

    article_usecase = CreateArticleUsecase(FakerArticleRepository())
    resp = await article_usecase.execute(ArticleRequestDto(
        title="SpaceX launches new cargo Dragon spacecraft to space station",
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov.",
        news_site="SpaceNews",
        featured=False,
        image_url="https://spacenews.com/wp-content/uploads/2022/11/crs26-launch.jpg",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
    ))

    assert resp.get_value().status == 200


@pytest.mark.asyncio
async def test_create_fali_article_usecase():
    """should be return status 400"""

    article_usecase = CreateArticleUsecase(FakerArticleRepository())
    resp = await article_usecase.execute(ArticleRequestDto(
        title=1,
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov.",
        news_site="",
        featured="False",
        image_url="h**1ttps:/hahjahsf.com",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
    ))

    assert resp.error_value().status == 400
    assert isinstance(resp.error_value().message, dict)
