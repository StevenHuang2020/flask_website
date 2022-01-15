# -*- encoding: utf-8 -*-
# Date: 14/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: start
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

# secrets.token_hex(16)
app.config['SECRET_KEY'] = 'e7c794326ea87a59b2cf616809e1efcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite/website.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/my_website'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

# print('MAIL_USERNAME, MAIL_PASSWORD = ',
#       app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
mail = Mail(app)


from first_website import routes
