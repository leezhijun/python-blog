from views import index,json,sql
from viewHandle.loginHandle import loginHandle
from viewHandle.siteHandle import siteHandle
from viewHandle.userHandle import userHandle
from viewHandle.cateHandle import cateHandle
from viewHandle.tagHandle import tagHandle
from viewHandle.articleHandle import articleHandle
from viewHandle.fileHandle import fileHandle

login_Handle = loginHandle() # 登陆处理
siteHandle = siteHandle() # 站点信息
userHandle = userHandle() # 用户
cateHandle = cateHandle() # 类目
tagHandle = tagHandle() # 标签
articleHandle = articleHandle() # 文章
fileHandle = fileHandle() # 文件

def set_routers(app):
    # app.router.add_get("/", index)
    # app.router.add_get("/json", json)
    # app.router.add_get("/sql", sql)
    app.router.add_post('/login', login_Handle.login) # 登陆
    app.router.add_post('/loginOut', login_Handle.loginOut) # 退出
    app.router.add_post('/siteIndex', siteHandle.siteIndex) # 网站基本信息
    app.router.add_post('/updateSiteIndex', siteHandle.updateSiteIndex) # 网站基本信息修改
    app.router.add_post('/addCate', cateHandle.addCate) # 添加类目
    app.router.add_post('/cateDelete', cateHandle.cateDelete) # 删除类目
    app.router.add_post('/cateUpdate', cateHandle.cateUpdate) # 修改类目
    app.router.add_post('/cateSelect', cateHandle.cateSelect) # 查询类目列表
    app.router.add_post('/cateMenuAll', cateHandle.cateMenuAll) # 查询一级类目
    app.router.add_post('/catelevels', cateHandle.catelevels) # 查询类目级联
    app.router.add_post('/cateUpdateShow', cateHandle.cateUpdateShow) # 修改类目是否默认菜单
    app.router.add_post('/addTag', tagHandle.addTag) # 添加标签
    app.router.add_post('/tagDelete', tagHandle.tagDelete) # 删除标签
    app.router.add_post('/tagUpdate', tagHandle.tagUpdate) # 修改标签
    app.router.add_post('/tagSelect', tagHandle.tagSelect) # 查询标签列表
    app.router.add_post('/tagSearchName', tagHandle.tagSearchName) # 查询标签id
    app.router.add_post('/addArticle', articleHandle.addArticle) # 添加文章
    app.router.add_post('/articleDelete', articleHandle.articleDelete) # 删除文章
    app.router.add_post('/articleUpdate', articleHandle.articleUpdate) # 修改文章
    app.router.add_post('/articleSelect', articleHandle.articleSelect) # 查询文章列表
    app.router.add_post('/articleSelectId', articleHandle.articleSelectId) # 查询文章列表ID
    app.router.add_post('/tagArticleDelete', articleHandle.tagArticleDelete) # 删除文章标签id
    app.router.add_post('/upload', fileHandle.store_file_handler) # 文件上传