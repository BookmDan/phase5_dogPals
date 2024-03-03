from flask import request, session
from flask_restful import Resource
from config import db
from models.users import User

class Signup(Resource):
  def post(self):
    json = request.get_json()

    try:
      user = User(
        first_name=json.get('first_name'),
        last_name=json.get('last_name'),
        email=json.get('email'),
        phone_number=json.get('phone_number'),
      ) 
      #hashes password and saves it to _password_hash
      user.password_hash = json['password']
      db.session.add(user)
      db.session.commit()

      session['user_id'] = user.id

      return user.to_dict(), 201
    
    # jsonify({'message': 'Signup successful', 'user': user.to_dict()}, 201)
    
    except Exception as err:
      return {"errors": [str(err)]}, 422
    
    
  # def post(self):
  #   json = request.get_json()
  #   try:
  #     user = User(username=json.get('username'), address=json.get('address'))
  #     user.password_hash = json.get('password')
  #     db.session.add(user)
  #     db.session.commit()
  #     session['user_id'] = user.id
  #     return user.to_dict(), 201
    
  #   except Exception as err:
  #     return {"errors": [str(err)]}, 422