from wtforms import StringField, DecimalField, PasswordField, SubmitField, Form, validators, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from fitness.database import User, Post

min_name = 2
max_name = 20
min_pw = 10
max_pw = 100

#SignUp class validation form for input fields
class SignUpForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired(), Length(min=min_name, max=max_name)])
    last_name = StringField('Last name', validators=[DataRequired(), Length(min=min_name, max=max_name)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=min_pw, max=max_pw)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #Searching email on database and validate email of user input in
    #if the email has already registered, it will prompt a validation error
    #otherwise, it will put the user info to database
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already used, please choose another email')


#Signin class validation for user log in
class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

#Item class validation for user input nutrition for calories output
class itemForm(FlaskForm):
    item = StringField("Food Item",validators = [DataRequired()])
    submit = SubmitField('Search')

#Item class validation for user input calories for output calories info
class calorieForm(FlaskForm):
    consumed = DecimalField("Calories consumed", validators = [])
    burned = DecimalField("Calories burned", validators = [])
    submit = SubmitField("Submit")
