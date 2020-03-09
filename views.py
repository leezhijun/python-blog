from aiohttp import web
import asyncio
import aiomysql

loop = asyncio.get_event_loop() #返回当前 OS 线程中正在运行的事件循环
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
    conn = await aiomysql.connect(
        host='127.0.0.1', 
        port=3306,
        user='root',
        password='newpassword',
        db='demo',
        loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT title,author FROM tbl")
    # print(cur.description)
    r = await cur.fetchall()
    # print(r)
    await cur.close()
    conn.close()
    data = {
        'data':r,
        'code':0,
        'message': '请求成功'
    }
    return web.json_response(data)
