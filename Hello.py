#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/Hello/')
@app.route('/Hello/<name>')
def Hello(name=None):
    return render_template("Hello.html", name=name)
# 模块引用模板，是在模块的旁边 template 文件夹里面

if __name__ == '__main__':
    app.run()
