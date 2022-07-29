from src.application_service.sqlalchemy_db import engine
from sqlalchemy.orm import registry
from src.doiman.url import Url
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    inspect,
)

mapper = registry()
metadata = MetaData(engine)

urls = Table(
    'urls', metadata,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('long_url',String, index=True),
    Column('short_url',String, index=True),
    Column('visits',Integer, default=0)
)


def start_mappers():
    if not inspect(engine).has_table("urls"):
        metadata.create_all()

    mapper.map_imperatively(Url, urls)

