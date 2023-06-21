from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flaskblog.models import User


# from wtforms.validators import DataRequired, Length, email_validator, EqualTo

class Registrationform(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=2, max=20)], )
    email = StringField("Email",
                        validators=[DataRequired(), ])
    # validators=[DataRequired(), email_validator()])
    password = PasswordField("Password",
                             validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose different one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please choose different one.")


class Loginform(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), ])
    # validators = [DataRequired(), email_validator()])
    password = PasswordField("Password",
                             validators=[DataRequired()])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")
