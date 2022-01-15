# -*- encoding: utf-8 -*-
# Date: 13/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Install db before first run website
The default database is sqlite. If you want to use
other database such as Mysql, PosgreSQL, etc,
you need to install first.

Database configuration(__init__.py):
app.config['SQLALCHEMY_DATABASE_URI'] = ''
"""

import os
from first_website import db, bcrypt  # __init__.py
from first_website.models import User, Post


def main():
    # clear all tables
    db.drop_all()
    # create all tables defined in models
    db.create_all()

    # add a default user to db
    # Email: test@gmail.com
    # Password: 123
    hashed_password = bcrypt.generate_password_hash('123').decode('utf-8')
    user = User(username='test', password=hashed_password, email='test@gmail.com')
    db.session.add(user)

    # add a first post of user
    post = Post(title='First post', content='Content of first post', author=user)
    db.session.add(post)
    db.session.commit()


if __name__ == "__main__":
    main()
