#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request,Flask
app = Flask(__name__)

with app.test_request_context('/hello', method='POST'):    # 针对单元测试最早的解决方案。
    assert request.path == '/hello'
    assert request.method == 'POST'

# 依赖于请求对象的代码突然中断；解决反感就是自己创建一个请求并将它跟上下文绑定。

if __name__ == '__main__':
    app.run()
