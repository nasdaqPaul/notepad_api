from flask import Flask
from flask_restful import Api
from mongoengine import connect

from app.resources import Note, Notes

api = Api()
api.add_resource(Note, '/note')
api.add_resource(Notes, '/notes')


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    connect(host='mongodb://mongoengine:1234@localhost:27017/test?authSource=test')

    with app.app_context():
        from .auth import auth
        app.register_blueprint(auth)

    return app
