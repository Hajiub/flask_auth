from . import db

from flask_login import UserMixin

class User(UserMixin, db.Model):
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username   = db.Column(db.String(200), unique=True, nullable=False)
    email      = db.Column(db.String(200), unique=True, nullable=False)
    hashed_password = db.Column(db.String(100), nullable=False)