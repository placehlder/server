from datetime import datetime

from app import db, app
from sqlalchemy.orm import relationship
import jwt


class User(db.Model):
    username = db.Column("username", db.String(60), primary_key=True, unique=True)
    password = db.Column("password", db.String(60))
    lastlogin = db.Column("lastlogin", db.Integer)
    messages = relationship("Message", backref="user")
    rooms = db.Column(db.Integer, db.ForeignKey("room.id"))


class Message(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    room = db.Column(db.Integer, db.ForeignKey("room.id"))


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = relationship("User", backref="user")
    messages = relationship("Message", backref="user")


def encode_auth_token(username):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
        return True, payload['sub']
    except jwt.ExpiredSignatureError:
        return False, 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return False, 'Invalid token. Please log in again.'
