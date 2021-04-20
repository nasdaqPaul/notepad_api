import datetime

from marshmallow import Schema, fields
from werkzeug.exceptions import BadRequest


# TODO: Find a way to better organize this code

class BaseSchema(Schema):
    def handle_error(self, exc, data, **kwargs):
        error = {
            'error': 'ValidationError',
            'messages': exc.messages
        }
        raise BadRequest(error)


class Todo(Schema):
    title = fields.String(required=True)
    completed = fields.Boolean(default=False)


class Note(BaseSchema):
    _id = fields.String(load_only=True)
    favourite = fields.Boolean(default=False)
    content = fields.String()
    todos = fields.List(fields.Nested(Todo))
    images = fields.List(fields.String)
    last_update = fields.DateTime(default=datetime.datetime.utcnow())


class User(BaseSchema):
    first_name = fields.String(required=True, data_key='firstName')
    last_name = fields.String(required=True, data_key='lastName')
    email_address = fields.Email(required=True, data_key='emailAddress')
    password = fields.String(required=True)


class UserLogin(BaseSchema):
    email_address = fields.String(required=True, data_key='emailAddress')
    password = fields.String(required=True)
