from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired()])
    password = PasswordField('password' , validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
