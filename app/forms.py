from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    name = StringField('Username', validators=[InputRequired()])
    classno = StringField('Class', validators=[InputRequired()])
    valid = StringField('Validation Code', validators=[InputRequired()])

class AccountForm(FlaskForm):
    fullname = StringField('Full Name', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
