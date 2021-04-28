import datetime

from marshmallow import Schema, fields

from app.exceptions import ValidationError


# TODO: Find a way to better organize this code

class BaseSchema(Schema):
    def handle_error(self, exc, data, **kwargs):
        raise ValidationError(exc.messages)


class Todo(Schema):
    title = fields.String(required=True)
    completed = fields.Boolean(default=False)


class Note(BaseSchema):
    id = fields.String(dump_only=True)
    favourite = fields.Boolean(default=False)
    content = fields.String()
    todos = fields.List(fields.Nested(Todo))
    images = fields.List(fields.String)
    last_update = fields.DateTime(default=datetime.datetime.utcnow(), data_key='lastUpdate')


class User(BaseSchema):
    id = fields.String(dump_only=True)
    first_name = fields.String(required=True, data_key='firstName')
    last_name = fields.String(required=True, data_key='lastName')
    email_address = fields.Email(required=True, data_key='emailAddress')
    password = fields.String(required=True, load_only=True)


class UserLogin(BaseSchema):
    email_address = fields.String(required=True, data_key='emailAddress')
    password = fields.String(required=True)
