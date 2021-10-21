# Built-in packages
import os


# Third-party packages
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, Query, Session
from sqlalchemy.ext.declarative import declarative_base

# Local packages

DB_USER = os.getenv("DB_USERNAME")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


class SQLAlchemy:
    Query: Query = None

    def __init__(self) -> None:
        self.Query = Query
        self.Model = declarative_base()
        self.session: Session = None
        self.engine: Engine = None

    def init_session(self):
        self.engine = create_engine(
            f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
        self.session = sessionmaker(self.engine)()


db = SQLAlchemy()


def register_db():
    db.init_session()
