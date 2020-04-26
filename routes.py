from views import index,json,sql
from viewHandle.loginHandle import loginHandle

login_Handle = loginHandle()

def set_routers(app):
    app.router.add_get("/", index)
    app.router.add_get("/json", json)
    app.router.add_get("/sql", sql)
    app.router.add_post('/login', login_Handle.login)