# pylint: disable=line-too-long
from datetime import datetime
from src.domain.entities import Article, ArticleProps


def test_article_entity():
    """should be be return title"""
    article = Article(ArticleProps(
        title="SpaceX launches new cargo Dragon spacecraft to space station",
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov. 26, carrying supplies, experiments and new solar arrays for the International Space Station.",
        news_site="SpaceNews",
        featured=False,
        image_url="https://spacenews.com/wp-content/uploads/2022/11/crs26-launch.jpg",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
        published_at=datetime.utcnow,
        updated_at=datetime.utcnow
    ))

    assert article.props.news_site == "SpaceNews"
    assert article.props.featured is False


def test_return_valid_article_validation():
    """should be return a valid article validation"""
    article = Article(ArticleProps(
        title="SpaceX launches new cargo Dragon spacecraft to space station",
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov. 26, carrying supplies, experiments and new solar arrays for the International Space Station.",
        news_site="SpaceNews",
        featured=False,
        image_url="https://spacenews.com/wp-content/uploads/2022/11/crs26-launch.jpg",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
        published_at=datetime.utcnow,
        updated_at=datetime.utcnow
    ))

    is_valid, _ = article.validate()

    assert is_valid is True


def test_return_invalid_article_validation():
    """should be return a invalid article validation"""
    article = Article(ArticleProps(
        title=1,
        summary="brand new SpaceX Falcon 9 successfully launched a new cargo Dragon spacecraft Nov. 26, carrying supplies, experiments and new solar arrays for the International Space Station.",
        news_site="",
        featured="False",
        image_url="ht*ps:/aaaufufhweuofh",
        url="https://spacenews.com/spacex-launches-new-cargo-dragon-spacecraft-to-space-station/",
        published_at=datetime.utcnow,
        updated_at=datetime.utcnow
    ))

    is_valid, err = article.validate()

    assert is_valid is False
    assert isinstance(err, dict)
