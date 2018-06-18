#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-18 15:04:13
# @Author  : zap ()
# @Link    : 
# @Version : $Id$

from . import db



class User(db.Model):
	__tablename__ = 'user'
	