from src.adaptors.repository import SqlAlchemyRepository
from src.service_layer.sqlalchemy_db import DEFAULT_SESSION_MAKER
from src.adaptors.orm import start_mappers
from src.config import get_orm_type


def handle_repository_type():
    orm_type = get_orm_type()
    handler = ORM_TYPE_HANDLER[orm_type]
    repository = handler()
    return repository


def get_sqlalchemy_repository():
    repository = SqlAlchemyRepository(session=DEFAULT_SESSION_MAKER())
    start_mappers()
    return repository


ORM_TYPE_HANDLER = {'SQLAlchemy': get_sqlalchemy_repository}