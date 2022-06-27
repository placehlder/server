from app import db
from sqlalchemy.orm import relationship


class User(db.Model):
    username = db.Column(db.String(60), "username", primary_key=True, unique=True)
    password = db.Column(db.String(60), "password")
    lastlogin = db.Column(db.Integer, "lastlogin")
    messages = relationship("Message", backref="user")
    rooms = db.Column(db.Integer, db.ForeignKey("room.id"))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
    room = db.Column(db.Integer, db.ForeignKey("room.id"))


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = relationship("User", backref="user")
    messages = relationship("Message", backref="user")

