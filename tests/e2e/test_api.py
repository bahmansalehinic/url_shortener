from src.config import BASE_URL
from uuid import uuid4
import pytest
from sqlalchemy.orm import clear_mappers
from src.adaptors.orm import start_mappers


@pytest.fixture()
def random_valid_url():
    random_url = f"{BASE_URL},{uuid4()}"
    return random_url


def test_api_get_invalid(client, random_valid_url):
    # asserting the random valid url is not saved
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 400
    clear_mappers()


def test_api_post_valid(client, random_valid_url):
    # asserting post creates a valid random url
    start_mappers()
    res = client.post('/url', json={'url': random_valid_url})
    assert res.status_code == 201

    # asserting get can retrieve a saved url
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 200
    clear_mappers()


def test_api_put_valid(client, random_valid_url):
    start_mappers()
    res = client.post('/url', json={'url': random_valid_url})
    assert res.status_code == 201
    res = client.put('/url', json={'url': random_valid_url, 'new_url':random_valid_url + 'aaa'})
    assert res.status_code == 201
    res = client.get('/url/' + random_valid_url + 'aaa' )
    assert res.status_code == 200
    clear_mappers()


def test_api_put_creates_valid(client, random_valid_url):
    start_mappers()
    res = client.put('/url', json={'url': random_valid_url, 'new_url':random_valid_url + 'aaa'})
    assert res.status_code == 201
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 200
    clear_mappers()



def test_api_deletes_url(client, random_valid_url):
    start_mappers()
    res = client.post('/url', json={'url': random_valid_url})
    assert res.status_code == 201

    # asserting deleting a url
    res = client.delete('/url', json={'url': random_valid_url})
    assert res.status_code == 204

    # assert it is not found by the get method
    res = client.get('/url/' + random_valid_url)
    assert res.status_code == 400
    clear_mappers()


