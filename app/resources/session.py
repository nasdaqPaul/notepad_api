from flask import request
from flask_restful import Resource

from app.models import User as UserModel
from app.schemas import UserLogin as UserLoginSchema


class Session(Resource):
    def post(self):
        schema = UserLoginSchema()
        login_details = schema.load(request.get_json())
        user = UserModel.objects.get(email_address=login_details['email_address'])
        print(user.first_name)

        return "hehe"
