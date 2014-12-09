__author__ = 'marcusmccurdy'

from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email


class SignupForm(Form):
    email = StringField('email', validators=(DataRequired(), Email()))
    password = StringField('password', validators=(DataRequired(),))


class AddEntryForm(Form):
    datetime = DateTimeField('datetime', validators=(DataRequired(),))
    text = StringField('text', validators=(DataRequired(),))
    calories = IntegerField('calories', validators=(DataRequired(),))
