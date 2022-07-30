import pytest
from sqlalchemy.orm import sessionmaker, clear_mappers
from src.adaptors.orm import metadata, start_mappers
from tenacity import retry, stop_after_delay
from src.config import get_api_url, get_postgres_uri
import requests
from sqlalchemy import create_engine
import time
from pathlib import Path


@pytest.fixture()
def app():
    from src.entry_point.flask_app import app
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


# @retry(stop=stop_after_delay(10))
# def wait_for_web_app_to_come_up():
#     url = get_api_url()
#     return requests.get(url)


@pytest.fixture
def session_factory(postgres_db):
    start_mappers()
    yield sessionmaker(bind=postgres_db)
    clear_mappers()


@pytest.fixture
def session(session_factory):
    return session_factory()


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    return engine.connect()


@pytest.fixture(scope='session')
def postgres_db():
    engine = create_engine(get_postgres_uri())
    wait_for_postgres_to_come_up(engine)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session(postgres_db):
    start_mappers()
    yield sessionmaker(bind=postgres_db)()
    clear_mappers()


# @pytest.fixture
# def restart_api():
#     (Path(__file__).parent / "flask_app.py").touch()
#     time.sleep(0.5)
#     wait_for_web_app_to_come_up()


