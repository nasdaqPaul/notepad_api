from flask import Flask
from flask_restful import Api
from mongoengine import connect

from app.resources import Note, Notes, Users, Session

api = Api()
api.add_resource(Note, '/note')
api.add_resource(Notes, '/notes')
api.add_resource(Users, '/users')
api.add_resource(Session, '/session')


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    connect(host='mongodb://mongoengine:1234@localhost:27017/test?authSource=test')

    return app
