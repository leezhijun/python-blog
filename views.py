from aiohttp import web
from sqlcontroller import SQLcontroller
from model import blog_site, blog_user

async def index(request):
    return web.Response(text='hello aiohttp')

async def json(request):
    data = {
        'a': 123,
        'b': 'hello world'
    }
    return web.json_response(data)

async def hello(request):
    name = request.match_info.get('name','test')
    text = 'hello '+ name
    return web.Response(text=text)

async def sql(request):
    data = {
        'code': 0,
        'data': None,
        'msg' :''
    }
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
        return web.json_response(data)