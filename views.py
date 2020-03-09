from aiohttp import web

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
