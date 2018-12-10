from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired , ValidationError, EqualTo, Email, Length, Optional
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
    car_plate = StringField('Placa do carro' , validators = [Optional()]) 

                            

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Usuário já existe. Por favor, tente outro!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email já registrado. Por favor, tente outro!')
    
    def validate_car_plate(self, car_plate):
        plate = car_plate.data
        if len(plate) != 7:
            raise ValidationError('Placa invalida!')

        for i in range(3):
            if plate[i].isdigit():
                raise ValidationError('Placa invalida!')
                
        if not plate[3].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[4].isdigit():
            if not plate[4].isalpha():
                raise ValidationError('Placa invalida!')
        if not plate[5].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[6].isdigit():
            raise ValidationError('Placa invalida!')


class PostForm(FlaskForm):
    content = StringField('Digite aqui sua mensagem', validators=[DataRequired(), Length(min=1, max=500)])
    matter_field = SelectField(u'Tag:', choices=[(0, 'Comum'),(1 , 'Amarela'),(2 , 'Vermelha')])
    
class PreferencesForm(FlaskForm):
    car_plate = StringField('Placa do 1º carro:' , validators = [Optional()])
    car_plate2 = StringField('Placa do 2º carro' , validators = [Optional()])
    password = PasswordField('Senha:', validators=[DataRequired()])
    new_password = PasswordField('Nova Senha:', validators=[Optional()])


    
    def validate_car_plate(self, newcar_plate):
        plate = newcar_plate.data
        if len(plate) != 7:
            raise ValidationError('Placa invalida!')

        for i in range(3):
            if plate[i].isdigit():
                raise ValidationError('Placa invalida!')
                
        if not plate[3].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[4].isdigit():
            if not plate[4].isalpha():
                raise ValidationError('Placa invalida!')
        if not plate[5].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[6].isdigit():
            raise ValidationError('Placa invalida!') 
    
    def validate_car_plate2(self, newcar_plate):
        plate = newcar_plate.data
        if len(plate) != 7:
            raise ValidationError('Placa invalida!')

        for i in range(3):
            if plate[i].isdigit():
                raise ValidationError('Placa invalida!')
                
        if not plate[3].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[4].isdigit():
            if not plate[4].isalpha():
                raise ValidationError('Placa invalida!')
        if not plate[5].isdigit():
            raise ValidationError('Placa invalida!')

        if not plate[6].isdigit():
            raise ValidationError('Placa invalida!') 
    
    