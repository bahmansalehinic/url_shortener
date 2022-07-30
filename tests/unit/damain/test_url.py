from src.doiman.url import Url
from src.adaptors.repository import AbstractRepository
from typing import Set
from unittest import TestCase


class FakeRepository(AbstractRepository):
    def __init__(self):
        super(FakeRepository, self).__init__()
        self._urls: Set[Url] = set()

    def add(self, url:Url) -> Url:
        self._urls.add(url)
        return url

    def get(self, url:str) -> Url:
        return self.get_by_long_url()

    def get_by_long_url(self, long_url: str) -> Url:
        return next((u for u in self._urls if u.long_url == long_url), None)

    def get_by_short_url(self, short_url: str) -> Url:
        return next((u for u in self._urls if u.long_url == short_url), None)

    def delete(self, url: Url):
        url_retrieved = next((u for u in self._urls if u == url), None)
        if url_retrieved:
            self._urls.remove(url_retrieved)

class TestUrl(TestCase):
    def setUp(self) -> None:
        self.url = Url('www.tier.app')

