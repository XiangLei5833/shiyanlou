#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/layout/')
@app.route('/layout/<name>')
def layout(name=None):
    return render_template('layout_out.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
