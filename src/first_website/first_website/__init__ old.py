# -*- encoding: utf-8 -*-
# Date: 14/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: start
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from first_website.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

# from first_website import routes

from first_website.main.routes import main
from first_website.users.routes import users
from first_website.posts.routes import posts

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(posts)
