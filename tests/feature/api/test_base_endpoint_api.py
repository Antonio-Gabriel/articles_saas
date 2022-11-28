import pytest
import requests


@pytest.mark.skip
def test_base_endpoind_of_api():
    """should be return a message"""

    result = requests.get('http://0.0.0.0:8000/', timeout=5)

    assert result.status_code == 200
