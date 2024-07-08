from marshmallow import Schema, fields

class User_schema(Schema):
    
    id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()