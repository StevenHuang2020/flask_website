# -*- encoding: utf-8 -*-
# Date: 13/Jan/2022
# Author: Steven Huang, Auckland, NZ
# License: MIT License
"""
Description: web forms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField('Post')
