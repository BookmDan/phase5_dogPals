from flask import request, session
from flask_restful import Resource
from config import db
from models.users import User

class Signup(Resource):
  def post(self):
    json = request.get_json()
    try:
      user = User(
        name=json.get('first_name'),
        email=json.get('email'),
        _password_hash=json.get('_password_hash') 
      ) 
      #hashes password and saves it to _password_hash
      # user.password_hash = json['password']
      db.session.add(user)
      db.session.commit()

      session['user_id'] = user.id
      return user.to_dict(), 201

    except Exception as err:
      return {"errors": [str(err)]}, 422
