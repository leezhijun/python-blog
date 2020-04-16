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
    SQL = SQLcontroller() # 创建sql操作对象
    print(SQL)
    querysql = blog_site.select()
    print(querysql)
    res = await SQL.selectAll(querysql)
    return web.json_response(res)