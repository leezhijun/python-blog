import sys
import os
import json
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_site, blog_user
from untils.encryption import base_64, hmac_sha256, jm_md5
from sqlalchemy.sql import and_, or_, not_
from untils.formatDate import formatDate
from aiohttp import web

class loginHandle:
    def __init__(self):
        pass

    async def login(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        param = json.loads(request._payload._buffer[0])["data"]
        username = param['username']
        password = jm_md5('blog',param['password'])
        Header = {
            "alg": "HS256",
            "typ": "JWT"
        }
        timenow = datetime.now().timestamp()
        Payload = {
            'username': None, # 用户名
            'user_id': None, #用户id
            'over_time': None #过期时间
        }
        timenow = datetime.now().timestamp()
        overtime = timenow + 60*60*2 # JWT过期时间
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            querysql = blog_user.select().where(and_(blog_user.c.user_name == username,blog_user.c.user_password == password))# sql 语句
            print(querysql)
            result = await SQL.querySql(querysql) # sql执行
            res = await result.first()
            print(res)
            # data['data'] = {'user_id':i[0],'user_name':i[1],'user_registered_time':formatDate(i[7],'Y-m-d H-M-S')} for i in res]
            if res: # 有结果
                data['data'] = {'user_id':res[0],'user_name':res[1],'user_registered_time':formatDate(res[7],'Y-m-d H-M-S')}
                Payload['username'] = res[1]
                Payload['user_id'] = res[0]
                Payload['over_time'] = overtime
            else: # 无结果
                data['code'] = -100
                data['msg'] = '账号或密码错误!'
        except Exception as e : # 异常
            print(e)
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            secret = 'pyblog'
            Signature = hmac_sha256(
            base_64(json.dumps(Header, indent=2)) + "." +
            base_64(json.dumps(Payload, indent=2)),
            secret)
            JWT = base_64(json.dumps(Header, indent=2))+'.'+base_64(json.dumps(Payload, indent=2))+'.'+Signature
            headers = {
                'Authorization': JWT
            }
            print(data)
            if data['code']==0:
                print(web.json_response(data,headers=headers))
                return web.json_response(data,headers=headers)
            else:
                return web.json_response(data)
            
    async def loginOut(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :'退出登陆成功!'
        }
        return web.json_response(data)