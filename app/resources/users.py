from flask import request
from flask_restful import Resource
from mongoengine import NotUniqueError
from werkzeug.exceptions import BadRequest

from app.models import User as UserModel
from app.schemas import User as UserSchema


class Users(Resource):
    def post(self):
        schema = UserSchema()
        registration_details = schema.load(request.get_json())
        new_user = UserModel(first_name=registration_details['first_name'], last_name=registration_details['last_name'],
                             email_address=registration_details['email_address'])
        new_user.set_password(registration_details['password'])
        try:
            new_user.save()
        except NotUniqueError as e:
            print(e)
            error = {
                'error': 'NotUniqueError',
                'message': f"Email address '{new_user.email_address}' is not available"
            }
            raise BadRequest(error)
        return 'Post on /auth/register'
