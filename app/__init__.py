from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

api = Api()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)
