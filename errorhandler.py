#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
# 定制错误页面，可以使用 errorhandler() 装饰器
# 404 是在 render_template() 调用之后存在的。用于告诉 Flask 该页的错误代码应该是404，即没有找到。
