# -*- encoding: utf-8 -*-
# Date: 11/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: Flask test
Start server with flask cmd:
1. open cmd
2. $ set FLASK_APP=main.py
   $ set FLASK_DEBUG=1
3. $ flask run

Start server with Python:
$ python main.py

Reference courses:
https://www.youtube.com/watch?v=UIJKdCIEXUQ&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3

"""

import json
from posts_db import posts
from flask import Flask, render_template, url_for, flash, redirect
import secrets
from forms import RegistrationForm, LoginForm

print('__name__=', __name__)
app = Flask(__name__)

# secrets.token_hex(16)
app.config['SECRET_KEY'] = 'e7c794326ea87a59b2cf616809e1efcd'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@t.com' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/test/')
def test():
    return '<h1> This is just a test! </h1>'


# def to_pretty_json(value):
#     return json.dumps(value, sort_keys=True,
#                       indent=2, separators=(',', ': '))


def main():
    # app.jinja_env.filters['tojson_pretty'] = to_pretty_json
    app.run(debug=True)


if __name__ == "__main__":
    main()
