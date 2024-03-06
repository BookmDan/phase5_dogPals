from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields
from sqlalchemy.orm import validates
from config import db

class Dog(db.Model, SerializerMixin):
  __tablename__ = "dogs"
  id = db.Column(db.Integer, primary_key=True)
  owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  name = db.Column(db.String)
  breed = db.Column(db.String)
  age = db.Column(db.Integer)

  owner = db.relationship('User', backref='dogs')

  @validates("name")
  def validate_name(self, key, name):
    if not name:
      raise ValueError("Name must not be empty")
    return name

  @validates("breed")
  def validate_breed(self, key, breed):
    if not breed:
      raise ValueError("Breed must not be empty")
    return breed

  @validates("age")
  def validate_age(self, key, age):
    if age < 0:
      raise ValueError("Age must be a non-negative integer")
    return age

  serialize_rules = ('-owner_id',)
  
class DogSchema(Schema):
  id = fields.Int()
  owner_id = fields.Int(required=True)
  name = fields.Str(required=True)
  breed = fields.Str(required=True)
  age = fields.Int(required=True)
