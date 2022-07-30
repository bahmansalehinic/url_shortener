import pytest
from starlette.testclient import TestClient


@pytest.fixture
def client():
    from src.entry_point.flask_app import app
    return TestClient(app)