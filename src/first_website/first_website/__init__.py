# -*- encoding: utf-8 -*-
# Date: 14/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: start
"""

# import json
# import secrets
# from posts_db import posts

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


print('__name__=', __name__)
app = Flask(__name__)

# secrets.token_hex(16)
app.config['SECRET_KEY'] = 'e7c794326ea87a59b2cf616809e1efcd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/my_website'
db = SQLAlchemy(app)

from first_website import routes