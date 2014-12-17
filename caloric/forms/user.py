__author__ = 'marcusmccurdy'

from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email


class UserSettingsForm(Form):
    daily_calories = IntegerField('daily_calories', validators=(DataRequired(),))


class SignupForm(Form):
    username = StringField('email', validators=(DataRequired(), Email()))
    password = StringField('password', validators=(DataRequired(),))
