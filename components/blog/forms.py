from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):

	email = StringField('E-Mail', validators=[DataRequired(), Email()])
	inquiry = TextField('Inquiry', validators=[DataRequired()])

	submit = SubmitField('Submit')