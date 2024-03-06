from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields, validates, ValidationError
from config import db

# Define the association table
user_sitter_association = db.Table('user_sitter_association',
  db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
  db.Column('sitter_id', db.Integer, db.ForeignKey('sitters.id'), primary_key=True)
)

class Sitter(db.Model, SerializerMixin):
  __tablename__ = "sitters"
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  bio = db.Column(db.Text)
  availability = db.Column(db.String)
  # owners = db.relationship('User', secondary=user_sitter_association, backref='sitters')
  sitter_ownerships = db.relationship('Dog', backref='sitter')
  
  @validates("availability")
  def validate_availability(self, key, availability):
    if not availability:
      raise ValueError("Availability must not be empty")
    return availability

Sitter.serialize_rules = ('-user_id', )

class SitterSchema(Schema):
  id = fields.Int()
  user_id = fields.Int(required=True)
  bio = fields.Str()
  availability = fields.Str(required=True)
