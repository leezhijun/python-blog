import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_tag
from sqlalchemy.sql import and_, or_, not_
# from untils.formatDate import formatDate
from aiohttp import web

class tagHandle:
    def __init__(self):
        pass
    # 增
    async def addTag(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            print(param)
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_tag.insert(None).values(tag_name=param['tag_name'],tag_order=10,tag_alias=param['tag_alias'])
            # print(sql)
            result = await SQL.querySql(sql) # sql执行
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            # print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 删
    async def tagDelete(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_tag.delete(None).where(blog_tag.c.tag_id == param['tag_id'])
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            # print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 改
    async def tagUpdate(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_tag.update(None).where(blog_tag.c.tag_id == param['tag_id'])\
                .values(
                    tag_name=param['tag_name'],
                    tag_alias=param['tag_alias'],
                    tag_img=param['tag_img'],
                    tag_description=param['tag_description'],
                    tag_order=param['tag_order']
                )
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            # print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 查-all
    async def tagSelect(self,request,payload):
        data = {
            'code': 0,
            'data': {},
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            limit = param['pageSize']
            offset = (param['pageIndex']-1)*param['pageSize']
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_tag.select().limit(limit).offset(offset)
            sql2 = blog_tag.select()
            if param['tag_id']:
                sql = blog_tag.select().where(blog_tag.c.tag_id == param['tag_id']).limit(limit).offset(offset)
                sql2 = blog_tag.select().where(blog_tag.c.tag_id == param['tag_id'])
            if param['tag_name']:
                sql = blog_tag.select().where(blog_tag.c.tag_name == param['tag_name']).limit(limit).offset(offset)
                sql2 = blog_tag.select().where(blog_tag.c.tag_name == param['tag_name'])
            if param['tag_id'] and param['tag_name']: 
                sql = blog_tag.select().\
                    where(and_(blog_tag.c.tag_name == param['tag_name'],blog_tag.c.tag_id == param['tag_id'])).\
                    limit(limit).offset(offset)
                sql2 = blog_tag.select().\
                    where(and_(blog_tag.c.tag_name == param['tag_name'],blog_tag.c.tag_id == param['tag_id']))
            print(sql)
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            result2 = await SQL.querySql(sql2) # sql执行
            # print(res)
            data['data']['data'] = [{'tag_id':i[0],'tag_name':i[1],'tag_alias':i[2],'tag_order':i[3],'tag_img':i[4],'tag_description':i[5]} for i in res] if res else []
            data['data']['total'] = result2.rowcount
            # print(data['data'])
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)