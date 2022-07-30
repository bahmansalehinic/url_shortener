from src.application_service.ports.db_service import handle_orm_type
from src.doiman.url import Url
from src.application_service.exceptions import *
from src.config import MIN_URL_LENGTH
import webbrowser

repository = handle_orm_type()

valid_domain_set = {'https://tier.app', 'https://www.tier.app',
                    'tier.app', 'www.tier.app',
                    'http://tier.app', 'http://www.tier.app'}


def create_shorten_url(long_url):
    if repository.get(long_url):
        raise UrlAlreadyExists(long_url)
    if len(long_url) < MIN_URL_LENGTH:
        raise UrlTooShort(long_url)
    if not any({long_url.startswith(d) for d in valid_domain_set}):
        raise InvalidDomain(long_url)

    url = Url(long_url)
    url.create_short_url()
    url.save(repository)
    return url.to_dict()


def find_url(url):
    url_obj = repository.get(url)
    if not url_obj:
        url_obj = repository.get_by_short_url(url)
    if url_obj:
        return url_obj.to_dict()
    raise UrlDoesNotExist(url)


def visit(url):
    url_obj = repository.get_by_short_url(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    url_obj.visits += 1
    url_obj.save(repository)
    long_url = url_obj.to_dict()['long_url']
    if not any({long_url.startswith(v) for v in {'http://', 'https://'}}):
        long_url = 'https://' + long_url
    return long_url


def modify(url, new_url):
    url_obj = repository.get(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    url_obj.long_url = new_url
    url_obj.save(repository)
    return url_obj.to_dict()


def delete(url):
    url_obj = repository.get(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    repository.delete(url)
    return {'delete': f"url: {url} deleted successfully"}
