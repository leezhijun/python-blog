import datetime
import time
# 生成字典
def retutnObj(obj1,obj2):
    data = {}
    for i in range(len(obj1)):
        # data[obj1[i]] = obj2[i]
        if isinstance(obj2[i], datetime.datetime):
            data[obj1[i]] =  obj2[i].strftime('%Y-%m-%d %H:%M:%S')
        else:
            data[obj1[i]] = obj2[i]
    return data
    # return dict(zip(obj1, obj2))
# 类目级联
def catelevelHandle(data):
    catelevel1 = [i for i in data if i['cate_parent_id']==0]
    def getchildren(cate,data):
        for i in cate:
            childrenList = [item for item in data if i['cate_id']==item['cate_parent_id']]
            if len(childrenList)>0:
                i['children'] = childrenList
                getchildren(childrenList,data)
        return cate
    return getchildren(catelevel1,data)
# 返回类目组
def returnCateArr(cate_id,cateList):
    cateArr = []
    def getParemt(id,cateList):
        for i in cateList:
            if(i['cate_id']==id) and i['cate_parent_id']==0:
                cateArr.append(i['cate_id'])
                return cateArr
            else:
                returnCateArr(i['cate_parent_id'],cateList)
    return getParemt(cate_id,cateList)



    