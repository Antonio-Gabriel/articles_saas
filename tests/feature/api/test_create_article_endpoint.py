import json
import pytest
import requests


@pytest.mark.skip
def test_create_article_api():
    """test create article endpoint"""
    article_payload = {
        "title": "Postando alguma coisa",
        "url": "https://api.spaceflightnewsapi.net/v3/articles",
        "summary": "Something posted right now",
        "featured": True,
        "image_url": "https://api.spaceflightnewsapi.net/v3/articles",
        "news_site": "api.spaceflightnewsapi.net"
    }

    articles = requests.post(
        'http://127.0.0.1:8000/api/v1/articles', json=article_payload, timeout=5)
    convert_to_json = json.loads(articles.text)

    assert articles.status_code == 200
    assert "title" in convert_to_json
