from flask import request
from flask_jwt_extended import jwt_required, get_current_user
from flask_restful import Resource
from mongoengine import ValidationError, DoesNotExist

from app.exceptions import NoteNotFound
from app.models import Note as NoteModel
from app.schemas import Note as NoteSchema


class Note(Resource):
    schema = NoteSchema()

    @jwt_required()
    def get(self, id):
        try:
            return self.schema.dump(NoteModel.objects.get(id=id))
        except (ValidationError, DoesNotExist):
            raise NoteNotFound(id)

    @jwt_required()
    def delete(self, id):
        return 'Delete on /Note'

    @jwt_required()
    def put(self, id):
        return 'Put on /Note'

    @jwt_required()
    def patch(self, id):
        return 'Patch on /Note'


class Notes(Resource):
    schema = NoteSchema()

    @jwt_required()
    def get(self):
        return self.schema.dump(NoteModel.objects(author=get_current_user()), many=True)

    @jwt_required()
    def post(self):
        post = self.schema.load(request.get_json())
        post_object = NoteModel(**post, author=get_current_user())
        post_object.save()
        return 'Post on /Notes'
