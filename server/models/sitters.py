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
    users = db.relationship('User', secondary='user_sitter_association', backref='sitters')

user_sitter_association = db.Table('user_sitter_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('sitter_id', db.Integer, db.ForeignKey('sitters.id'), primary_key=True)

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
