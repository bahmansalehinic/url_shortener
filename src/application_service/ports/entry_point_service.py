from src.application_service.ports.repository_handler import handle_repository_type
from src.doiman.url import Url
from src.application_service.exceptions import *
from src.config import MIN_URL_LENGTH

repository = handle_repository_type()

valid_domain_set = {'https://tier.app', 'https://www.tier.app',
                    'tier.app', 'www.tier.app',
                    'http://tier.app', 'http://www.tier.app'}


def create_shorten_url(long_url, repository_=repository):
    if repository_.get(long_url):
        raise UrlAlreadyExists(long_url)
    if len(long_url) < MIN_URL_LENGTH:
        raise UrlTooShort(long_url)
    if not any({long_url.startswith(d) for d in valid_domain_set}):
        raise InvalidDomain(long_url)

    url = Url(long_url)
    url.create_short_url()
    url.save(repository_)
    return url.to_dict()


def find_url(url, repository_=repository):
    url_obj = repository_.get(url)
    if not url_obj:
        url_obj = repository_.get_by_short_url(url)
    if url_obj:
        return url_obj.to_dict()
    raise UrlDoesNotExist(url)


def visit(url, repository_=repository):
    url_obj = repository_.get_by_short_url(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    url_obj.visits += 1
    url_obj.save(repository_)
    long_url = url_obj.to_dict()['long_url']
    if not any({long_url.startswith(v) for v in {'http://', 'https://'}}):
        long_url = 'https://' + long_url
    return long_url


def modify(url, new_url, repository_=repository):
    url_obj = repository_.get(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    url_obj.long_url = new_url
    url_obj.save(repository_)
    return url_obj.to_dict()


def delete(url, repository_=repository):
    url_obj = repository_.get(url)
    if not url_obj:
        raise UrlDoesNotExist(url)
    repository_.delete(url_obj)
    return {'delete': f"url: {url} deleted successfully"}
