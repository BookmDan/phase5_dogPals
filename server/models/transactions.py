from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields
from config import db

class Transaction(db.Model, SerializerMixin):
  __tablename__ = "transactions"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  sitter_id = db.Column(db.Integer, db.ForeignKey('sitters.id'), nullable=False)
  amount = db.Column(db.DECIMAL)
  timestamp = db.Column(db.DateTime)
  status = db.Column(db.String)

  user = db.relationship('User', foreign_keys=[user_id], backref='transactions_as_user')
  sitter = db.relationship('Sitter', foreign_keys=[sitter_id], backref='transactions_as_sitter')


class TransactionSchema(Schema):
  id = fields.Int()
  user_id = fields.Int(required=True)
  sitter_id = fields.Int(required=True)
  amount = fields.Decimal()
  timestamp = fields.DateTime()
  status = fields.Str()
