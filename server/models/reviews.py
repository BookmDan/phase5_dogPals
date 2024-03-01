from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields, validates, ValidationError

from config import db

class Review(db.Model, SerializerMixin):
  __tablename__ = "reviews"
  id = db.Column(db.Integer, primary_key=True)
  sitter_id = db.Column(db.Integer, db.ForeignKey('sitters.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  rating = db.Column(db.Integer)
  comment = db.Column(db.Text)

  sitter = db.relationship('Sitter', backref='reviews')
  user = db.relationship('User', backref='reviews')

  @validates('rating')
  def validate_rating(self, key, rating):
    if not 1 <= rating <= 5:
      raise ValidationError("Rating must be between 1 and 5")
    return rating

class ReviewSchema(Schema):
  id = fields.Int()
  sitter_id = fields.Int(required=True)
  user_id = fields.Int(required=True)
  rating = fields.Int(required=True)
  comment = fields.Str()