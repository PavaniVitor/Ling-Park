from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired , ValidationError, EqualTo, Email, Length
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

#    def validate_carplate(self, car_plate):                            

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuário já existe. Por favor, tente outro!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email já registrado. Por favor, tente outro!')

class PostForm(FlaskForm):
    content = StringField('Digite aqui sua mensagem', validators=[DataRequired(), Length(min=1, max=500)])
    matter_field = SelectField(u'Tag:', choices=[(0, 'Comum'),(1 , 'Amarela'),(2 , 'Vermelha')])
