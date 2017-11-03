#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User




class NameForm(FlaskForm):
    name = StringField('输入用户名', validators=[DataRequired()])
    submit = SubmitField('提交')

class EditProfileForm(FlaskForm):
    name = StringField('用户名', validators=[Length(0, 64)])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('我的介绍')
    submit = SubmitField('提交')

class PostForm(FlaskForm):
    body = PageDownField("输入一大段文字", validators=[DataRequired()])
    submit = SubmitField('提交')

class CommentForm(FlaskForm):
    body = StringField('输入你的评论', validators=[DataRequired()])
    submit = SubmitField('提交')
