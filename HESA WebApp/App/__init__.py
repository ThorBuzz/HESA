import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_wtf import CSRFProtect

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key='Something_secret'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
loginManager=LoginManager(app)
loginManager.login_view='login'
loginManager.login_message='Please log in to access this page'
loginManager.login_message_category='info'

csrf = CSRFProtect(app)

from . import routes
