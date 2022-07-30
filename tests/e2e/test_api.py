from src.config import BASE_URL
from uuid import uuid4
import pytest
from sqlalchemy.orm import clear_mappers


@pytest.fixture()
def random_valid_url():
    random_url = f"{BASE_URL},{uuid4()}"
    return random_url


def test_api(client, random_valid_url):
    # asserting the random valid url is not saved
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 400

    # asserting post creates a valid random url
    res = client.post('/url', json={'url': random_valid_url})
    assert res.status_code == 201

    # asserting get can retrieve a saved url
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 200

    # asserting deleting a url
    res = client.delete('/url', json={'url': random_valid_url})
    assert res.status_code == 204

    # assert it is not found by the get method
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 400

    clear_mappers()

