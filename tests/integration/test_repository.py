from tests.base_test import *
from src.adaptors.repository import SqlAlchemyRepository
from src.doiman.url import Url
from src.config import BASE_URL
from uuid import uuid4


class TestRepository(BaseTest):
    def test_repository_can_save_a_url(self):
        long_url = BASE_URL + str(uuid4())
        url = Url(long_url)
        repo = SqlAlchemyRepository(self._session)

        repo.add(url)
        self._session.commit()
        rows = list(self._session.execute(
            'SELECT long_url FROM "urls"'
        ))

        self.assertIn((long_url,), rows)

        repo.delete(url)
        rows = list(self._session.execute(
            'SELECT long_url FROM "urls"'
        ))

        self.assertNotIn((long_url,), rows)