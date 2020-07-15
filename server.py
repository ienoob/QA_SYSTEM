#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    @Time : 2020/7/15 20:15
    @Author  : jack.li
    @Site    : 
    @File    : server.py

"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


from tornado.options import define
from tornado.options import options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from routers import router_urls

