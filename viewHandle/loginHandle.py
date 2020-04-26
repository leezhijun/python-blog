import sys
import os
import json
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from model import blog_site, blog_user
from untils.encryption import base_64, hmac_sha256
from aiohttp import web

class loginHandle:
    def __init__(self):
        pass

    async def login(self,request):
        data = {
            'code': 0,
            'data': None,
            'msg' :''
        }
        param = json.loads(request._payload._buffer[0])['data']
        print(param)
        Header = {
            "alg": "HS256",
            "typ": "JWT"
        }
        Payload = {
            'username': None,
            'uid': None
        }
        secret = 'pyblog'
        Signature = hmac_sha256(
        base_64(json.dumps(Header, indent=2)) + "." +
        base_64(json.dumps(Payload, indent=2)),
        secret)
        JWT = Signature
        headers = {
            'Authorization': JWT
        }
        # return web.json_response(data,headers=headers)
        try:
            SQL = SQLcontroller() # 创建sql操作对象
            querysql = blog_site.select() # sql 语句
            result = await SQL.querySql(querysql) # sql执行
            res = await result.fetchall()
            data['data'] = [{'id':i[0],'site_key':i[1],'site_name':i[2],'site_value':i[3]} for i in res]
        except Exception as e :
            print(e)
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            print(data)
            return web.json_response(data,headers=headers)