from typing import Generator

from config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    config['database']['username'],
    config['database']['password'],
    config['database']['host'],
    config['database']['port'],
    config['database']['database'],
)

engine = create_engine(
    DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
