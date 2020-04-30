import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_cate
from sqlalchemy.sql import and_, or_, not_
from untils.dataHandle import catelevelHandle
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
            print(param)
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.insert(None).values(cate_name=param['cate_name'],cate_order=10,cate_show=1,cate_parent_id=param['cate_parent_id'])
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
            sql = blog_cate.delete(None).where(blog_cate.c.cate_id == param['cate_id'])
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
            sql = blog_cate.update(None).where(blog_cate.c.cate_id == param['cate_id'])\
                .values(
                    cate_name=param['cate_name'],
                    cate_title=param['cate_title'],
                    cate_keywords=param['cate_keywords'],
                    cate_description=param['cate_description'],
                    cate_img=param['cate_img'],
                    cate_show=param['cate_show'],
                    cate_order=param['cate_order']
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
    # 改-默认菜单
    async def cateUpdateShow(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.update(None).where(blog_cate.c.cate_id == param['cate_id'])\
                .values(
                    cate_show=param['cate_show']
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
    async def cateSelect(self,request,payload):
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
            sql = blog_cate.select().limit(limit).offset(offset)
            sql2 = blog_cate.select()
            if param['cate_id']:
                sql = blog_cate.select().where(blog_cate.c.cate_id == param['cate_id']).limit(limit).offset(offset)
                sql2 = blog_cate.select().where(blog_cate.c.cate_id == param['cate_id'])
            if param['cate_name']:
                sql = blog_cate.select().where(blog_cate.c.cate_name == param['cate_name']).limit(limit).offset(offset)
                sql2 = blog_cate.select().where(blog_cate.c.cate_name == param['cate_name'])
            if param['cate_id'] and param['cate_name']: 
                sql = blog_cate.select().\
                    where(and_(blog_cate.c.cate_name == param['cate_name'],blog_cate.c.cate_id == param['cate_id'])).\
                    limit(limit).offset(offset)
                sql2 = blog_cate.select().\
                    where(and_(blog_cate.c.cate_name == param['cate_name'],blog_cate.c.cate_id == param['cate_id']))
            # print(sql)
            # print(sql2)
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            result2 = await SQL.querySql(sql2) # sql执行
            # print(res)
            data['data']['data'] = [{'cate_id':i[0],'cate_name':i[1],'cate_title':i[2],'cate_keywords':i[3],'cate_description':i[4],'cate_img':i[5],'cate_order':i[6],'cate_show':i[7],'cate_parent_id':i[8]} for i in res] if res else []
            data['data']['total'] = result2.rowcount
            # print(data['data'])
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    # 查-1级类目
    async def cateMenuAll(self,request,payload):
        data = {
            'code': 0,
            'data': None,
            'msg' :''
        }
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select().where(blog_cate.c.cate_parent_id == 0)
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            # print(res)
            data['data'] = [{'cate_id':i[0],'cate_name':i[1],'cate_title':i[2],'cate_keywords':i[3],'cate_description':i[4],'cate_img':i[5],'cate_order':i[6],'cate_show':i[7],'cate_parent_id':i[8]} for i in res] if res else []
            # print(data['data'])
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    
    # 返回级联
    async def catelevels(self,request,payload):
        data = {
            'code': 0,
            'data': None,
            'msg' :''
        }
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_cate.select()
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            # print(res)
            catelist = [{'cate_id':i[0],'cate_name':i[1],'cate_title':i[2],'cate_keywords':i[3],'cate_description':i[4],'cate_img':i[5],'cate_order':i[6],'cate_show':i[7],'cate_parent_id':i[8]} for i in res] if res else []
            data['data'] = catelevelHandle(catelist)
            # print(data['data'])
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)