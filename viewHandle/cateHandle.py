import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_cate
from sqlalchemy.sql import and_, or_, not_
# from untils.formatDate import formatDate
from aiohttp import web

class cateHandle:
    def __init__(self):
        pass
    # 增
    async def addCate(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select()
            result = await SQL.querySql(sql) # sql执行
            print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 删
    async def cateDelete(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select()
            result = await SQL.querySql(sql) # sql执行
            print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 改
    async def cateUpdate(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select()
            result = await SQL.querySql(sql) # sql执行
            print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 查
    async def cateSelect(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select()
            result = await SQL.querySql(sql) # sql执行
            print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            data['data'] = res if res else []
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)