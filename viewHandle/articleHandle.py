import sys
import os
import json
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from untils.dataHandle import retutnObj
from model import blog_article
from sqlalchemy.sql import and_, or_, not_
from untils.formatDate import formatDate
from aiohttp import web

class articleHandle:
    def __init__(self):
        pass
    # 增
    async def addArticle(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            print(param)
            timenow = datetime.now().timestamp() # 当前时间戳
            SQL = SQLcontroller() # 创建sql操作对象
            cate_id = param['cate_id'] if param['cate_id'] else None
            # sql 语句
            sql = blog_article.insert(None).\
                values(
                    user_id=payload['user_id'],
                    cate_id=cate_id,
                    article_title=param['article_title'],
                    article_keywords=param['article_keywords'],
                    article_description=param['article_description'],
                    article_is_hot=param['article_is_hot'],
                    article_is_push=param['article_is_push'],
                    # article_img=param['article_img'],
                    article_content=param['article_content'],
                    # article_publish_time=formatDate(timenow,'Y-m-d H-M-S'),
                    # article_update_time=formatDate(timenow,'Y-m-d H-M-S'),
                    article_publish_time=timenow,
                    article_update_time=timenow,
                    article_browse_count=0,
                    article_like_count=0,
                    article_status=param['article_status'],
                    article_comment_status=0,
                    article_order=param['article_order'],
                    article_type=param['article_type'],
                )
            print(sql)
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
    async def articleDelete(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_article.delete(None).where(blog_article.c.article_id == param['article_id'])
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
    async def articleUpdate(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            param = json.loads(request._payload._buffer[0])["data"]
            SQL = SQLcontroller() # 创建sql操作对象
            # sql 语句
            sql = blog_article.update(None).where(blog_article.c.article_id == param['article_id'])\
                .values(
                    article_title=param['article_title'],
                    article_keywords=param['article_keywords'],
                    article_description=param['article_description'],
                    article_img=param['article_img'],
                    article_show=param['article_show'],
                    article_order=param['article_order']
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
    async def articleSelect(self,request,payload):
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
            sql = blog_article.select().limit(limit).offset(offset)
            sql2 = blog_article.select()
            if param['article_id']:
                sql = blog_article.select().where(blog_article.c.article_id == param['article_id']).limit(limit).offset(offset)
                sql2 = blog_article.select().where(blog_article.c.article_id == param['article_id'])
            if param['article_title']:
                sql = blog_article.select().where(blog_article.c.article_title == param['article_title']).limit(limit).offset(offset)
                sql2 = blog_article.select().where(blog_article.c.article_title == param['article_title'])
            if param['article_id'] and param['article_title']: 
                sql = blog_article.select().\
                    where(and_(blog_article.c.article_title == param['article_title'],blog_article.c.article_id == param['article_id'])).\
                    limit(limit).offset(offset)
                sql2 = blog_article.select().\
                    where(and_(blog_article.c.article_title == param['article_title'],blog_article.c.article_id == param['article_id']))
            print(sql)
            result = await SQL.querySql(sql) # sql执行
            # print(result)
            res = await result.fetchall() # fetchall()/fetchone()/fetchmany()/first()
            result2 = await SQL.querySql(sql2) # sql执行
            # print(res)
            tuple1 = (
                'article_id',
                'user_id',
                'cate_id',
                'article_title',
                'article_keywords',
                'article_description',
                'article_is_hot',
                'article_is_push',
                'article_img',
                'article_content',
                'article_publish_time',
                'article_update_time',
                'article_browse_count',
                'article_like_count',
                'article_status',
                'article_comment_status',
                'article_password',
                'article_order',
                'article_type',
            )
            # print(res)
            data['data']['data'] = [retutnObj(tuple1,i) for i in res] if res else []
            data['data']['total'] = result2.rowcount
            # print(data['data'])
        except Exception as e:
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            return web.json_response(data)
