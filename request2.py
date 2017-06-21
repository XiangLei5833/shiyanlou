#!/usr/bin/env python

from flask import Flask, request
app = Flask(__name__)

with app.request_context(environ):
    assert request.method == 'POST'
