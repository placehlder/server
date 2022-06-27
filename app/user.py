from app import db


class User(db.Model):
    username = db.Column(db.String(60), "username")
    password = db.Column(db.String(60), "password")
