from caloric.db import db, ActiveModel

__author__ = 'Marcus McCurdy'


class User(ActiveModel, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.email)
