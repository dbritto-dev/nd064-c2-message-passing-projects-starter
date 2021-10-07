# Built-in packages

# Third-party packages
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Local packages
from person_model import PersonModel


class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PersonModel
