# Built-in packages

# Third-party packages
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Local packages
from model import Person


class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        transient = True
