from dateutil.parser import parse
from caloric.db import db, ActiveModel
from datetime import datetime as dt

__author__ = 'Marcus McCurdy'


class Entry(ActiveModel, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    _datetime = db.Column(db.DateTime, default=dt.now(), nullable=False)
    text = db.Column(db.Text, default='')
    calories = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, text, calories, datetime=dt.now()):
        self.datetime = datetime
        self.text = text
        self.calories = calories

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        if type(datetime) in (dict,):
            self._datetime = parse(datetime['startDate']).replace(tzinfo=None)

    def __repr__(self):
        return '<Entry {} {} {}>'.format(self.user.email if self.user else '', self.text, self.calories)
    
    def to_dict(self):
        return {'id': self.id, 'text': self.text, 'calories': self.calories, 'datetime': self.datetime.isoformat()}