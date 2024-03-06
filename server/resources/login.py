from flask import request, session
from flask_restful import Resource
from models.users import User

class Login(Resource):
  def post(self):
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
      session['user_id'] = user.id
      response_body = user.to_dict(rules=('-_password_hash',))
      return response_body, 200
    else:
      return {"errors": ["Invalid username and/or password"]}, 401

  def get(self):
    return ({"message": "hi"}, 200)
