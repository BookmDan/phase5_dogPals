from sqlalchemy_serializer import SerializerMixin
from marshmallow import Schema, fields
from sqlalchemy.orm import validates

from config import db

class Sitter(db.Model, SerializerMixin):
    __tablename__ = "sitters"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    bio = db.Column(db.Text)
    availability = db.Column(db.String)

    # 1-1 relationship between user and sitter
    # sitter = db.relationship('Sitter', backref='user', uselist=False) 
    user = db.relationship('User', backref='sitter', uselist=False)
    serialize_rules = ('-user_id', )

    @validates("availability")
    def validate_availability(self, key, availability):
        if not availability:
            raise ValueError("Availability must not be empty")
        return availability


class SitterSchema(Schema):
    id = fields.Int()
    user_id = fields.Int(required=True)
    bio = fields.Str()
    availability = fields.Str(required=True)
