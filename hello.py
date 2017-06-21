#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template    # flask 自动配置好了 jinja2 模板，可以使用render_template() 来渲染模板，提供模板的名称以及想要作为关键字参数传入模板的变量
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)    # Flask将在 templates 文件夹中寻找模板，如果应用是个模块，这个文件夹在模块的旁边；如果是一个包，这个文件夹在包里面。


if __name__ == '__main__':
    app.run()
