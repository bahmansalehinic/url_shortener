from src.config import BASE_URL


class ApplicationError(Exception):
    pass


class UrlAlreadyExists(ApplicationError):
    def __init__(self, url: str):
        self.message = f'url: {url} already exists, use put for if you wan to update'
        super(UrlAlreadyExists, self).__init__(self.message)


class UrlTooShort(ApplicationError):
    def __init__(self, url: str):
        self.message = f'url: {url} is too short'
        super(UrlTooShort, self).__init__(self.message)


class InvalidDomain(ApplicationError):
    def __init__(self, url: str):
        self.message = f'url must be in {BASE_URL} domain, ' \
                       f'invalid url: {url}'
        super(InvalidDomain, self).__init__(self.message)


class UrlDoesNotExist(ApplicationError):
    def __init__(self, url: str):
        self.message = f'{url} is not a saved url'
        super(UrlDoesNotExist, self).__init__(self.message)
