from src.config import BASE_URL
import shortuuid
import json


class Url:
    def __init__(self, long_url, short_url=None):
        self.long_url = long_url
        self.short_url = short_url
        self.visits = 0

    def create_short_url(self):
        self.short_url = BASE_URL + str(shortuuid.uuid()[:5])

    def save(self, url_repository):
        return url_repository.add(self)

    def __str__(self):
        return json.dumps({'long_url': self.long_url,
                'short_url': self.short_url,
                'visits': self.visits})
