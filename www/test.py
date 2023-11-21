#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sql_model
import sql_orm
import asyncio


@asyncio.coroutine 
def test(loop):
    yield from sql_orm.create_pool(loop, user='www-data', password='www-data', db='awesome')

    u = sql_model.User(name='Test', email='test@example.com2', passwd='1234567890', image='about:blank')

    yield from u.save()



loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
