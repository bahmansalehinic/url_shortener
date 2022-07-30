import abc
from src.doiman.url import Url


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, url: Url) -> Url:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, url) -> Url:  # the default is by long_url
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, url):  # url is the long_url
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_long_url(self, long_url) -> Url:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_short_url(self, short_url) -> Url:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super(SqlAlchemyRepository, self).__init__()
        self.session = session

    def add(self, url):
        self.session.add(url)
        self.session.commit()

    def get(self, url) -> Url:
        return self.get_by_long_url(url)

    def delete(self, url_obj):
        if url_obj:
            self.session.delete(url_obj)
            self.session.commit()

    def get_by_long_url(self, long_url) -> Url:
        return self.session.query(Url).filter_by(long_url=long_url).first()

    def get_by_short_url(self, short_url) -> Url:
        return self.session.query(Url).filter_by(short_url=short_url).first()