from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from mongoengine import DoesNotExist

from app.exceptions import UserNotFound, IncorrectUserPassword
from app.models import User as UserModel
from app.schemas import UserLogin as UserLoginSchema


class Session(Resource):
    def post(self):
        schema = UserLoginSchema()
        login_details = schema.load(request.get_json())
        try:
            user = UserModel.objects.get(email_address=login_details['email_address'])
        except DoesNotExist:
            raise UserNotFound(login_details['email_address'])
        else:
            if not user.check_password(login_details['password']):
                raise IncorrectUserPassword
            return {
                'accessToken': create_access_token(user)
            }

    def patch(self):
        """We are using the patch method on session to enable refreshing access tokens"""
        pass

    def delete(self):
        """Log out route on the API"""
        pass
