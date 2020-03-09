from views import index,json,sql

def set_routers(app):
    app.router.add_get("/", index)
    app.router.add_get("/json", json)
    app.router.add_get("/sql", sql)