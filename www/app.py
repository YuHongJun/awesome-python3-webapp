#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Demi Yu'

'''
async web application.
'''

import logging;

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init(loop): #Web app服务器初始化
    app = web.Application(loop=loop) #制作响应函数集合
    app.router.add_route(method='GET',path='/',handler=index) #把响应函数添加到响应函数集合
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop() #创建事件
loop.run_until_complete(init(loop)) #运行
loop.run_forever() #服务器不关闭
