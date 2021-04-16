import datetime

from marshmallow import Schema, fields


class Note:
    class PUT(Schema):
        pass

    class PATCH(Schema):
        pass


class Notes:
    class POST(Schema):
        favourite = fields.Boolean(default=False)
        content = fields.String()
        todos = fields.List()
        images = fields.List()
        last_update = fields.DateTime(default=datetime.datetime.utcnow())
