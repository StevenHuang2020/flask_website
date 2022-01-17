# -*- encoding: utf-8 -*-
# Date: 16/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Web Configuration class
"""
import os


class Config:
    SECRET_KEY = 'e7c794326ea87a59b2cf616809e1efcd'  # secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite/website.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/my_website'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    # print('MAIL_USERNAME = ', MAIL_USERNAME)
    # print('MAIL_PASSWORD = ', MAIL_PASSWORD)
