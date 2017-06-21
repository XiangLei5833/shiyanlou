#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

# 上传的文件存储在内存或者文件系统上的一个临时位置。可以通过请求对象 files 属性访问这些文件。每个上传的文件都会储存在这个属性字典里
# save()，该方法允许你i存储文件在服务器的文件系统上
