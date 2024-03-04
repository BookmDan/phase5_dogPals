from flask import jsonify, request
from flask_restful import Resource
from config import db
from models.models import Message, MessageSchema  

message_schema = MessageSchema()

class MessagesResource(Resource):
  def get(self):
    messages = Message.query.all()
    result = message_schema.dump(messages, many=True)
    return jsonify(result), 200

  def post(self):
    data = request.get_json()
    new_message = Message(**data)
    db.session.add(new_message)
    db.session.commit()
    return message_schema.jsonify(new_message), 201

class MessageById(Resource):
  def get(self, id):
    message = Message.query.get(id)
    if message:
      return message_schema.jsonify(message), 200
    return jsonify({"message": f"Message with ID {id} not found"}), 404

  def patch(self, id):
    message = Message.query.get(id)
    if message:
      data = request.get_json()
      for key, value in data.items():
        setattr(message, key, value)
      db.session.commit()
      return message_schema.jsonify(message), 200
    return jsonify({"message": f"Message with ID {id} not found"}), 404

  def delete(self, id):
    message = Message.query.get(id)
    if message:
      db.session.delete(message)
      db.session.commit()
      return jsonify({"message": f"Message with ID {id} deleted successfully"}), 200
    return jsonify({"message": f"Message with ID {id} not found"}), 404


