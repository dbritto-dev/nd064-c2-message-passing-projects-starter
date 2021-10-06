# Built-in packages

# Third-party packages
from sqlalchemy import Column, Integer, String

# Local packages
from database import db  # noqa


class Person(db.Model):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
