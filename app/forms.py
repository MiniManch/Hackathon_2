import flask 
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,SubmitField,PasswordField,validators)
from wtforms.validators import InputRequired

class add_user(FlaskForm):
	name                  = StringField('Name', validators=[InputRequired()])
	password              = PasswordField('Password',validators=[validators.Length(min=8, message='Too short')])
	submit                = SubmitField('Submit')


# class login(FlaskForm):
# 	name                  = StringField('Name ', validators=[InputRequired()])
# 	password    		  = PasswordField(validators=[validators.Length(min=8, message='Too short')])
# 	submit                = SubmitField('Submit')
