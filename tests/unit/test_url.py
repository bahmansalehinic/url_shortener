from src.doiman.url import Url
from unittest import TestCase
from src.config import SHORT_URL_LENGTH
from tests.fake_repository import FakeRepository


class TestUrl(TestCase):
    def setUp(self) -> None:
        self.repository = FakeRepository()
        self.url = Url('www.tier.app')

    def test_url_initialised(self):
        self.assertIsInstance(self.url, Url)
        self.assertEqual(self.url.long_url, 'www.tier.app')
        self.assertIsNone(self.url.short_url)

    def test_url_create_short_url(self):
        self.url.create_short_url()
        self.assertIsNotNone(self.url.short_url)
        self.assertEqual(len(self.url.short_url), SHORT_URL_LENGTH)

    def test_url_save(self):
        self.url.save(self.repository)
        self.assertIsNotNone(self.repository.all())
        self.assertEqual(len(self.repository.all()), 1)
        self.assertIn(self.url, self.repository.all())


