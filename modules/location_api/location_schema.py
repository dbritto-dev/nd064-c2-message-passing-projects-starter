# Built-in packages

# Third-party packages
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, ModelConverter
from marshmallow import fields
from geoalchemy2.types import Geometry

# Local packages
from location_model import LocationModel


class GeoConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({Geometry: fields.Field})


class LocationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LocationModel
        model_converter = GeoConverter
