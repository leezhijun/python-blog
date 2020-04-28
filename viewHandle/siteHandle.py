import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_site
from sqlalchemy.sql import and_, or_, not_, bindparam
# from untils.formatDate import formatDate
from aiohttp import web

class siteHandle:
    def __init__(self):
        pass

    async def siteIndex(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            querysql = blog_site.select()# sql 语句
            print(querysql)
            result = await SQL.querySql(querysql) # sql执行
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            obj = {}
            for i in res:
                obj[i[1]] = i[3]
            data['data'] = obj
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
    
    async def updateSiteIndex(self,request,payload={}):
        data = {
            'code': 0,
            'data':'',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            stmt = blog_site.update(None).where(blog_site.c.site_key == bindparam('oldname')).values(site_value=bindparam('newname'))
            sqldata = [
                {'oldname':'site_name', 'newname': param['site_name']},
                {'oldname':'site_url', 'newname': param['site_url']},
                {'oldname':'site_title', 'newname': param['site_title']},
                {'oldname':'site_keywords', 'newname': param['site_keywords']},
                {'oldname':'site_descript', 'newname': param['site_descript']},
                {'oldname':'site_email', 'newname': param['site_email']},
                {'oldname':'site_copy', 'newname': param['site_copy']},
            ]
            result = await SQL.queryManySql(stmt,sqldata) # sql执行
            print(result)
            res = result.rowcount # fetchall()/fetchone()/fetchmany()/first()
            print(res)
            data['data'] = res
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)