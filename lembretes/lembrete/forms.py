from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from datetime import date

class LembreteForm(FlaskForm):
    titulo = StringField('Titulo',
                            validators=[DataRequired(), Length(min=2)])
    data = DateField('Data', format='%d/%m/%Y', default=date.today(), validators=[DataRequired()])
    texto = TextAreaField('Texto')
    salvar = SubmitField('Salvar')


class RegistrarForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=8)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    senha = PasswordField('Senha',
                        validators=[DataRequired(), Length(min=5, max=10)])
    confirmar_senha = PasswordField('Confirmar Senha',
                        validators=[DataRequired(), Length(min=5, max=10), EqualTo('senha')])
    confirmar = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=8)])
    senha = PasswordField('Senha',
                        validators=[DataRequired(), Length(min=5, max=10)])
    lembrar = BooleanField('Lembrar-se')
    confirmar = SubmitField('Login')