from marshmallow import Schema, fields


class ConnectionQuerySchema(Schema):
    start_date = fields.DateTime("%Y-%m-%d", required=True)
    end_date = fields.DateTime("%Y-%m-%d", required=True)
    distance = fields.Integer(missing=5)
