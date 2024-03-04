from flask import jsonify, request
from flask_restful import Resource
from models.models import db, User, UserSchema 
from config import db

user_schema = UserSchema()

class UsersResource(Resource):
  def get(self):
    users = User.query.all()
    result = user_schema.dump(users, many=True)
    return jsonify(result), 200

  def post(self):
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201

class UserById(Resource):
  def get(self, id):
    user = User.query.get(id)
    if user:
      return user_schema.jsonify(user), 200
    return jsonify({"message": f"User with ID {id} not found"}), 404

  def patch(self, id):
    user = User.query.get(id)
    if user:
      data = request.get_json()
      for key, value in data.items():
          setattr(user, key, value)
      db.session.commit()
      return user_schema.jsonify(user), 200
    return jsonify({"message": f"User with ID {id} not found"}), 404

  def delete(self, id):
    user = User.query.get(id)
    if user:
      db.session.delete(user)
      db.session.commit()
      return jsonify({"message": f"User with ID {id} deleted successfully"}), 200
    return jsonify({"message": f"User with ID {id} not found"}), 404

