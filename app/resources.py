from flask_jwt_extended import jwt_required
from flask_restful import Resource


class Note(Resource):
    @jwt_required()
    def get(self):
        pass

    @jwt_required()
    def delete(self):
        pass

    @jwt_required()
    def put(self):
        pass

    @jwt_required()
    def patch(self):
        pass


class Notes(Resource):
    @jwt_required()
    def get(self):
        pass

    @jwt_required()
    def post(self):
        pass
