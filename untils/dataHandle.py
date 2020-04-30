def retutnObj(obj1,obj2):
    data = {}
    for i in range(len(obj1)):
        data[obj1[i]] = obj2[i]
    return data
    # return dict(zip(obj1, obj2))

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


    