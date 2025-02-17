from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.simple import FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

class AddItemForm(FlaskForm):
    name = StringField('Product name', validators=[DataRequired()])
    price = StringField('Product price', validators=[DataRequired()])
    img = FileField('Product Picture', validators=[FileAllowed(['jpg','png'])])
    description = StringField('Product description ', validators=[DataRequired()])

class AccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Update')
    img = FileField('Profile Picture', validators=[FileAllowed(['jpg','png'])])
    role = BooleanField('Become a seller')
