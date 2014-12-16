from flask.ext.bcrypt import Bcrypt
from caloric.db import db, ActiveModel

__author__ = 'Marcus McCurdy'


bcrypt = Bcrypt()


class User(ActiveModel, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    daily_calories = db.Column(db.Integer, nullable=True, default=2000)#TODO: Find out about default for this

    def __init__(self, email, password, daily_calories=2000):
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.daily_calories = daily_calories

    def __repr__(self):
        return '<User {}>'.format(self.email)
