from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    role = SelectField('What is your role?', choices=[
        ('user', 'User'),
        ('admin', 'Administrator'),
        ('moderator', 'Moderator')
    ])
    submit = SubmitField('Submit')
