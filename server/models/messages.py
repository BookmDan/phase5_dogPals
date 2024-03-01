from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields
from config import db

class Message(db.Model, SerializerMixin):
  __tablename__ = "messages"
  id = db.Column(db.Integer, primary_key=True)
  sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  content = db.Column(db.Text)
  timestamp = db.Column(db.DateTime)

  sender = db.relationship('User', foreign_keys=[sender_id], backref='sent_messages')
  receiver = db.relationship('User', foreign_keys=[receiver_id], backref='received_messages')


class MessageSchema(Schema):
  id = fields.Int()
  sender_id = fields.Int(required=True)
  receiver_id = fields.Int(required=True)
  content = fields.Str()
  timestamp = fields.DateTime()
