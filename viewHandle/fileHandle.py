import sys
import os
import json
import random
from datetime import datetime
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from sqlcontroller import SQLcontroller
from aiohttp import web

class fileHandle:
    def __init__(self):
        pass
    
    async def store_file_handler(self,request,payload):
        data = {
            'code': 0,
            'data': '',
            'msg' :''
        }
        try:
            reader = await request.multipart()
            # /!\ 不要忘了这步。（至于为什么请搜索 Python 生成器/异步）/!\
            fileContent = await reader.next()
            filename_extension = os.path.splitext(fileContent.filename)[1]
            # 如果是分块传输的，别用Content-Length做判断。
            size = 0
            uploadPath = rootPath + '/uploads/'
            nowDay = datetime.now().strftime('%Y%m%d')
            print(filename_extension)
            filename = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000,9999)) + filename_extension
            # 判断是否存在对应日期的文件夹，没有则新建一个
            if not os.path.exists(uploadPath+nowDay):
                os.makedirs(uploadPath + nowDay)

            with open(uploadPath + nowDay + '/' + filename, 'wb') as f:
                while True:
                    chunk = await fileContent.read_chunk()  # 默认是8192个字节。
                    if not chunk:
                        break
                    size += len(chunk)
                    f.write(chunk)
            
            data['data'] = uploadPath + nowDay + '/' + filename
        except Exception as e : # 异常
            data['code'] = -100
            data['msg'] = str(e)
        finally:
            web.json_response(data)
