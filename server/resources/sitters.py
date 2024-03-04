from flask import jsonify, request
from flask_restful import Resource
from config import db
from models.models import Sitter, SitterSchema  

sitter_schema = SitterSchema()

class SittersResource(Resource):
  def get(self):
    sitters = Sitter.query.all()
    result = sitter_schema.dump(sitters, many=True)
    return jsonify(result), 200

  def post(self):
    data = request.get_json()
    new_sitter = Sitter(**data)
    db.session.add(new_sitter)
    db.session.commit()
    return sitter_schema.jsonify(new_sitter), 201

class SitterById(Resource):
  def get(self, id):
    sitter = Sitter.query.get(id)
    if sitter:
      return sitter_schema.jsonify(sitter), 200
    return jsonify({"message": f"Sitter with ID {id} not found"}), 404

  def patch(self, id):
    sitter = Sitter.query.get(id)
    if sitter:
      data = request.get_json()
      for key, value in data.items():
          setattr(sitter, key, value)
      db.session.commit()
      return sitter_schema.jsonify(sitter), 200
    return jsonify({"message": f"Sitter with ID {id} not found"}), 404

  def delete(self, id):
    sitter = Sitter.query.get(id)
    if sitter:
      db.session.delete(sitter)
      db.session.commit()
      return jsonify({"message": f"Sitter with ID {id} deleted successfully"}), 200
    return jsonify({"message": f"Sitter with ID {id} not found"}), 404


