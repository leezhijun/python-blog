from aiohttp import web
from routes import set_routers

app = web.Application() #创建应用
set_routers(app) #添加路由
web.run_app(app,host='127.0.0.1',port=8090) #启动应用