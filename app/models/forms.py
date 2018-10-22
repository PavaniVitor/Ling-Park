from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms.validators import DataRequired , ValidationError, EqualTo, Email
from app.models.tables import User


class LoginForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired()])
    password = PasswordField('password' , validators=[DataRequired()])
    remember_me = BooleanField('remember_me')

class RegForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    car_plate = StringField('Placa do carro') #adicionar  metodovalidador para a placa validate_car_plate

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')