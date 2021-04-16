from mongoengine import Document, StringField, EmailField, ReferenceField, BooleanField, ListField, DateTimeField, \
    EmbeddedDocumentListField, EmbeddedDocument, CASCADE
from werkzeug.security import generate_password_hash, check_password_hash


class User(Document):
    first_name = StringField(required=True, max_length=240, db_field='firstName')
    last_name = StringField(required=True, max_length=240, db_field='lastName')
    email_address = EmailField(required=True, max_length=240, unique=True, db_field='emailAddress')
    password = StringField(required=True, max_length=240)

    meta = {
        'collection': 'users'
    }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Note(Document):
    author = ReferenceField('User', required=True, reverse_delete_rule=CASCADE)
    favourite = BooleanField(default=False)
    images = ListField(StringField(max_length=240))
    last_update = DateTimeField(db_field='lastUpdate')
    todos = EmbeddedDocumentListField('Todo')
    content = StringField(default='')

    meta = {
        'collection': 'notes'
    }


class Todo(EmbeddedDocument):
    title = StringField(required=True, max_length=240)
    completed = BooleanField(default=False)

# TODO: Create indices
