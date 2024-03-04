from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import Schema, fields
from sqlalchemy.orm import validates

from config import db, bcrypt

class User(db.Model, SerializerMixin):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True, nullable=False)
  _password_hash = db.Column(db.String)
  
  @hybrid_property
  def password_hash(self):
    raise Exception("You cannot view the password hash.")

  @password_hash.setter
  def password_hash(self, password):
    if len(password) < 4:
      raise ValueError("Passwords must be 4 or more characters")
    self._password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))

  def check_password(self, password):
    return bcrypt.check_password_hash(self._password_hash, password)
  
  serialize_rules = ('-_password_hash', )

  @validates("email")
  def check_email(self, key, email):
    if '@' not in email:
      raise ValueError("Invalid email format.Email must contain '@' symbol.")
    return email

  def __repr__(self):
    return f'<User id={self.id} first_name={self.first_name} last_name={self.last_name} email={self.email}>'
  
class UserSchema(Schema):
  id = fields.Int()
  name = fields.Str(required=True)
  email = fields.Email(required=True)
  password = db.Column(db.String)
 