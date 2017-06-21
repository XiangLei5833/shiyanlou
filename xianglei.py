#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/shiyanlou')
def shiyanlou():
    return 'XiangLei'


if __name__ == '__main__':
    app.run()
