import flask 
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,SubmitField)
from wtforms.validators import InputRequired, Length

class add_user(FlaskForm):
	name                  = StringField('name? ', validators=[InputRequired()])
	street                = StringField('street',validators = [InputRequired()])
	city    			  = StringField('city',validators = [InputRequired()])
	zipcode               = StringField('zipcode',validators = [InputRequired()])
	submit                = SubmitField('Submit') 

    
class login(FlaskForm):
	name                  = StringField('name? ', validators=[InputRequired()])
	city    			  = StringField('city',validators = [InputRequired()])
	submit                = SubmitField('Submit') 

    

  
  