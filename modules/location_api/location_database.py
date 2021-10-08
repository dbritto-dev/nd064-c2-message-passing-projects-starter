# Built-in packages
import os


# Third-party packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Query, Session
from sqlalchemy.ext.declarative import declarative_base

# Local packages


class SQLAlchemy:
    Query: Query = None

    def __init__(self) -> None:
        self.Query = Query
        self.Model = declarative_base()
        self.session: Session = None

    def init_session(self):
        sqlalchemy_db_uri = os.getenv("SQLALCHEMY_DATABASE_URI")
        engine = create_engine(sqlalchemy_db_uri)
        self.session = sessionmaker(engine)()


db = SQLAlchemy()


def register_db():
    db.init_session()
