#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, make_response
app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

