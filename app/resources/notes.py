from flask import request
from flask_restful import Resource

from app.models import Note as NoteModel
from app.schemas import Note as NoteSchema


class Note(Resource):

    def get(self):
        return 'Get on /Note'

    def delete(self):
        return 'Delete on /Note'

    def put(self):
        return 'Put on /Note'

    def patch(self):
        return 'Patch on /Note'


class Notes(Resource):
    schema = NoteSchema()

    def get(self):
        return self.schema.dump(NoteModel.objects, many=True)

    def post(self):
        post = self.schema.load(request.get_json())
        post_object = NoteModel(**post)
        print(post)

        return 'Post on /Notes'
