from caloric.db import db, ActiveModel
from datetime import datetime as dt

__author__ = 'marcusmccurdy'

#TODO: Should a user be allowed to entry calories for the same date and time?
class Entry(ActiveModel, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime, default=dt.now())
    text = db.Column(db.Text, default='')
    calories = db.Column(db.Integer) #TODO: Find out if the user should be allowed to set this to 0
