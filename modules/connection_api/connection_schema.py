from marshmallow import Schema, fields


class ConnectionQuerySchema(Schema):
    start_date = fields.DateTime("%Y-%m-%d", required=True)
    end_date = fields.DateTime("%Y-%m-%d", required=True)
    distance = fields.Integer(missing=5)


class PersonSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    company_name = fields.String()


class LocationSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer()
    latitude = fields.String()
    longitude = fields.String()
    creation_time = fields.DateTime()


class ConnectionSchema(Schema):
    person = fields.Nested(PersonSchema)
    location = fields.Nested(LocationSchema)
