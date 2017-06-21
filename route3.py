#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug=True)

# 结果是 404 Not Found
# URL 后面跟着的参数斜线只可以少写，不可多写。URL 会保持唯一。有助于避免搜索引擎索引同一个页面两次
