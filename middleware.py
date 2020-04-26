from aiohttp import web

@web.middleware
async def middleware1(request, handler):
    print('Middleware 1 called')
    print(handler)
    response = await handler(request)
    print('Middleware 1 finished')
    return response
