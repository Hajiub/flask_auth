from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError, Regexp
import re
from .models import User


class LoginFrom:
    pass

class SigninForm(FlaskForm):
    def validate_username(self, username):
        if User.query.filter(User.username == username.data).first():
            raise ValidationError('Username already exists!')

    def validate_email(self, email):
        if User.query.filter(User.email == email.data).first():
            raise ValidationError('Email already exists')

    username = StringField('Username', validators=[DataRequired(), Length(min=4, message="Username must be at least 4 characters long!")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1   = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2   = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', message='Passwords must match'), DataRequired()])

