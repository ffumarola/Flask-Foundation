from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators


class SignupForm(Form):
    username = TextField(u'Email', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.required()])
    password_confirm = PasswordField(u'Repeat Password', 
    	validators=[validators.required(), validators.EqualTo('password')])
