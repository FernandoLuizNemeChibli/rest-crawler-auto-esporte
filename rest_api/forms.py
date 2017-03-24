from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length

class RegisterForm(Form):
	nickname=StringField('nickname',validators=[DataRequired()])
	email=StringField('email',validators=[DataRequired(),Email()])
	password=PasswordField('password',validators=[Length(min=5),DataRequired(),EqualTo('confirm',message='Password must match')])
	confirm=PasswordField('confirm')
