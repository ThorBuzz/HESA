from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from .models import User, Post


# REGISTER
class RegistrationForm(FlaskForm):
    id=IntegerField('Student ID', validators=[DataRequired(), Length(min=8, max=8)])
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(max=50), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
    # methods
    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken')
        
        
# LOGIN
class LoginForm(FlaskForm):
    # id = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    id=IntegerField('Student ID', validators=[DataRequired(), Length(min=8, max=8, message='Invalid ID')])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    
# CONTACT
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    id = StringField('ID', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    content = StringField('Message', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Send Message')
    
    
# POST/UPDATE
class PostForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired(), Length(max=100)])
    content=TextAreaField('Content', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Post')
    
    
# COMMENT
class CommentForm(FlaskForm):
    content=TextAreaField('Content', validators=[Length(max=1000)])
    submit = SubmitField('Comment')
    
    
# EDIT PROFILE
class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(max=50), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', 
                                                    validators=[DataRequired(), 
                                                    EqualTo('password', message='Passwords must match') ])
    submit = SubmitField('Update')
    # methods
    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken')
            
# CONTACT US
class ContactForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired(), Length(max=100)])
    content=TextAreaField('Content', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Send')
