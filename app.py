from aiohttp import web
from routes import set_routers
from middleware import middleware1
import aiohttp_cors
app = web.Application(middlewares=[middleware1]) #创建应用
set_routers(app) #添加路由
# Configure default CORS settings.
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

# Configure CORS on all routes.
for route in list(app.router.routes()):
    cors.add(route)
web.run_app(app,host='127.0.0.1',port=8090) #启动应用