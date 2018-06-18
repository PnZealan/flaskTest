#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-17 20:47:49
# @Author  : zap ()
# @Link    : 
# @Version : $Id$
# filename: factory_method 

from flask import Flask 
from flask_bootstrap import Boostrap 
from flask_login import LoginMananger
from flask_sqlalchemy import SQLAlchemy 

bootstrap = Boostrap()
db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	bootstrap.__init__app(app)
	db.__init__app(app)

	from .main import main as main_buleprint

	