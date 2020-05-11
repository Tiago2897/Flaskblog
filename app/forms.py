from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Nome de Utilizador", 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirme Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Resgistar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este Nome de Utilizador já existe. Escolha outro diferente.')


    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este Email já existe. Escolha outro diferente.')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Relembre-me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
            username = StringField('Username',
                                validators=[DataRequired(), Length(min=2, max=20)])
            email = StringField('Email',
                                validators=[DataRequired(), Email()])
            picture = FileField('Atualize a foto de perfil', 
                                validators=[FileAllowed(['jpg', 'png'])])
            submit = SubmitField('Atualize')

            def validate_username(self, username):
                if username.data != current_user.username:
                    user = User.query.filter_by(username=username.data).first()
                    if user:
                        raise ValidationError('Este Nome de Utilizador já existe. Escolha outro diferente.')

            def validate_email(self, email):
                if email.data != current_user.email:
                    user = User.query.filter_by(email=email.data).first()
                    if user:
                        raise ValidationError('Este Email já existe. Escolha outro diferente.')

class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired()])
    content = TextAreaField('Conteúdo', validators=[DataRequired()])
    submit = SubmitField('Post')
