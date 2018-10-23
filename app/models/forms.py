from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms.validators import DataRequired , ValidationError, EqualTo, Email
from app.models.tables import User


class LoginForm(FlaskForm):
    username = StringField('Usuário' , validators=[DataRequired()])
    password = PasswordField('Senha' , validators=[DataRequired()])
    remember_me = BooleanField('Lembre de mim')

class RegForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField('Repita a senha', validators=[DataRequired(), EqualTo('password')])
    car_plate = StringField('Placa do carro') 

    #def validate_carplate(self, car_plate):    A ideia é que os 3 primeiros elementos da string sejam
    #    plate =                                letras e os 4 ultimos sejam numeros

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuário já existe. Por favor, tente outro!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email já registrado. Por favor, tente outro!')


class Post(FlaskForm):
    user = StringField(LoginForm.username)
    text = StringField('Digite sua mensagem')
    status = forms.ChoiceField('Qual o status de sua mensagem?', choices=[], required=False)
