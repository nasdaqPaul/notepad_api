import datetime

from marshmallow import Schema, fields
from werkzeug.exceptions import BadRequest


class Todo(Schema):
    title = fields.String(required=True)
    completed = fields.Boolean(default=False)


class Note(Schema):
    _id = fields.String(load_only=True)
    favourite = fields.Boolean(default=False)
    content = fields.String()
    todos = fields.List(fields.Nested(Todo))
    images = fields.List(fields.String)
    last_update = fields.DateTime(default=datetime.datetime.utcnow())

    def handle_error(self, exc, data, **kwargs):
        raise BadRequest(exc.messages)


class User(Schema):
    first_name = fields.String(required=True, data_key='firstName')
    last_name = fields.String(required=True, data_key='lastName')
    email_address = fields.Email(required=True, data_key='emailAddress')
    password = fields.String(required=True)

    def handle_error(self, exc, data, **kwargs):
        raise BadRequest(exc.messages)
