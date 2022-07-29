from src.application_service.ports.db_service import handle_orm_type
from src.doiman.url import Url
from src.application_service.exceptions import *
from src.config import MIN_URL_LENGTH

repository = handle_orm_type()

valid_domain_set = {'https://tier.app', 'www.tier.app', 'tier.app', 'https://www.tier.app'}


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
    return str(url)
