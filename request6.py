#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Flask
app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    # 注意这里引用 cookies 字典的键值对是使用cookies.get(key)
    # 而不是 cookies[key], 这是防止该字典不存在时报错“keyerror”
