import json
import pytest
import requests


@pytest.mark.skip
def test_get_articles_api():
    """test get article endpoint"""
    articles = requests.get('http://0.0.0.0:8000/api/v1/articles', timeout=5)
    decode_response = articles.content.decode('utf-8')
    convert_to_json = json.loads(decode_response)

    assert articles.status_code == 200
    assert "items" in convert_to_json
