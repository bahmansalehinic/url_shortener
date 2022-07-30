import os


class AppSettings:
    host = os.getenv('HOST') or '0.0.0.0'
    port = os.getenv('PORT') or 4000


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", 'root')
    user = "psql"
    db_name = "url_shortener"
    #print(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    return f"postgresql:///{db_name}"#"{user}:{password}@{host}:{port}/{db_name}"

# def get_in_memory_db_url():
#     db_host = os.getenv('IN_MEMORY_DB_HOST') or '127.0.0.1'
#     db_port = os.getenv('IN_MEMORY_DB_PORT') or 6379
#     db_db = os.getenv('DB_DB') or 0
#     return {'host': db_host, 'port': db_port, 'db': db_db}


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TIER_SECRET_KEY'
    DEBUG = True
    CSRF_ENABLED = False


def get_db_url():
    db_url = os.getenv('DB_URL') or "sqlite:///./tiershortener.db"
    return db_url


def get_orm_type():
    orm_type = os.getenv('ORM') or 'SQLAlchemy'
    return orm_type


BASE_URL = 'https://www.tier.app/'

MIN_URL_LENGTH = 6
SHORT_URL_LENGTH = 4