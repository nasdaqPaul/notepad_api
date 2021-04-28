from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from mongoengine import connect

from app.models import User as UserModel
from app.resources import Note, Notes, Users, Session
from app.schemas import User


class CustomAPI(Api):
    """Handles exceptions rised from routes within the API"""

    def handle_error(self, e):
        return jsonify({
            'error': e.name,
            'code': e.code,
            'message(s)': e.description
        }), e.code


api = CustomAPI()
jwt = JWTManager()

api.add_resource(Note, '/note/<string:id>')
api.add_resource(Notes, '/notes')
api.add_resource(Users, '/users')
api.add_resource(Session, '/session')


@jwt.user_identity_loader
def id_loader(user):
    schema = User()
    return schema.dump(user)


@jwt.user_lookup_loader
def user_loader(jwt_header, jwt_data):
    return jwt_data['sub']['id']


@jwt.token_in_blocklist_loader()
def check_revoked_token(jwt_header, jwt_payload):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    api.init_app(app)
    jwt.init_app(app)

    # TODO: Test and exit on failed db connection.
    connect(host='mongodb://mongoengine:1234@localhost:27017/test?authSource=test')

    return app
