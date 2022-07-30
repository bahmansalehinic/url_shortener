import unittest
import pytest


class BaseTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _session(self, session):
        self._session = session

    def tearDown(self) -> None:
        self._session = None