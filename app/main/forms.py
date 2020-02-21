from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class SignupForm( FlaskForm ):
    username = StringField( 'Username', validators=[DataRequired()] )
    email = StringField( 'Email address', validators=[DataRequired(), Email( message='Valid email address required' )] )
    password = PasswordField( 'Password',
                              validators=[DataRequired(), EqualTo( 'confirm', message='Passwords must match' )] )
    confirm = PasswordField( 'Repeat Password' )
    submit = SubmitField( 'Sign Up' )


class SearchForm( FlaskForm ):
    term = StringField( 'Search', validators=[DataRequired(), Length( min=2, max=60 )] )
