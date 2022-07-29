from sqlalchemy import create_engine
from src.config import get_db_url
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    get_db_url(), connect_args={"check_same_thread": False}
)

DEFAULT_SESSION_MAKER = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)



