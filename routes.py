from views import index,json,sql
from viewHandle.loginHandle import loginHandle
from viewHandle.siteHandle import siteHandle
from viewHandle.userHandle import userHandle
from viewHandle.cateHandle import cateHandle
from viewHandle.tagHandle import tagHandle
from viewHandle.articleHandle import articleHandle

login_Handle = loginHandle() # 登陆处理
siteHandle = siteHandle() # 站点信息
userHandle = userHandle() # 用户
cateHandle = cateHandle() # 类目
tagHandle = tagHandle() # 标签
articleHandle = articleHandle() # 文章

def set_routers(app):
    app.router.add_get("/", index)
    app.router.add_get("/json", json)
    app.router.add_get("/sql", sql)
    app.router.add_post('/login', login_Handle.login)
    app.router.add_post('/loginOut', login_Handle.loginOut)
    app.router.add_post('/siteIndex', siteHandle.siteIndex)
    app.router.add_post('/updateSiteIndex', siteHandle.updateSiteIndex)
    app.router.add_post('/addCate', cateHandle.addCate)
    app.router.add_post('/cateDelete', cateHandle.cateDelete)
    app.router.add_post('/cateUpdate', cateHandle.cateUpdate)
    app.router.add_post('/cateSelect', cateHandle.cateSelect)