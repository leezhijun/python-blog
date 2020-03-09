from views import index,json

def set_routers(app):
    app.router.add_get("/", index)
    app.router.add_get("/json", json)