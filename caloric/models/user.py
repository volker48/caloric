from caloric.db import db

__author__ = 'Marcus McCurdy'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
