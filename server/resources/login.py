from flask import request, session
from flask_restful import Resource

from models.users import User

class Login(Resource):
  def post(self):
    username = request.get_json()['username']
    password = request.get_json()['password']

    user = User.query.filter_by(username=username).first()

    if user and user.authenticate(password):
      session['user_id'] = user.id
      response_body = {
        "id": user.id,
        "username": user.username,
      }
      return response_body, 200
    else:
      return {"errors": ["Invalid username and/or password"]}, 401

  def get(self):
    return ({"message": "hi"}, 200)