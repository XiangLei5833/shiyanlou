#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404) # make_response()封装并返回表达式，获取结果对象并修改
    resp.headers['X-Something'] = 'A value'
    return resp


if __name__ == '__main__':
    app.run()

