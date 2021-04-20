from flask import Blueprint, jsonify
from flask import request
from mongoengine import NotUniqueError
from werkzeug.exceptions import BadRequest

from app.models import User
from app.schemas import User as UserSchema

auth = Blueprint(__name__, 'auth', url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():
    schema = UserSchema()
    registration_details = schema.load(request.get_json())
    new_user = User(first_name=registration_details['first_name'], last_name=registration_details['last_name'],
                    email_address=registration_details['email_address'])
    new_user.set_password(registration_details['password'])
    new_user.save()
    print(new_user)

    return 'Post on /auth/register'


@auth.errorhandler(BadRequest)
def handle400(e):
    return jsonify(e.description)

# @auth.errorhandler(NotUniqueError)
# def handle_not_unique(e):
#     return jsonify(e.description)
