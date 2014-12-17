from wtforms import StringField, Form, DateTimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class AddEntryForm(Form):
    datetime = DateTimeField('datetime', validators=(DataRequired(),))
    text = StringField('text', validators=(DataRequired(),))
    calories = IntegerField('calories', validators=(DataRequired(), NumberRange(min=1)))