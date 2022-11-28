import json
import pytest
import requests


@pytest.mark.skip
def test_update_article_api():
    """test update article endpoint"""
    article_payload = {
        "title": "Postando outra coisa",
        "url": "https://api.spaceflightnewsapi.net/v3/articles",
        "summary": "Something posted right now",
        "featured": True,
        "image_url": "https://spacenews.com/wp-content/uploads/2022/11/crs26-launch.jpg",
        "news_site": "api.spaceflightnewsapi.net"
    }

    articles = requests.put(
        'http://127.0.0.1:8000/api/v1/articles/35f329d6-8329-41ba-b69a-ba121e156cf7',
        json=article_payload, timeout=5)
    convert_to_json = json.loads(articles.text)

    assert articles.status_code == 200
    assert "title" in convert_to_json
