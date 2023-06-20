from . import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id         = Column(Integer, primary_key=True, autoincrement=True)
    username   = Column(String(200), unique=True, nullable=False)
    email      = Column(String(200), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)