from aiohttp import web
from datetime import datetime
from untils.encryption import debase_64, base_64, hmac_sha256, jm_md5
import json
@web.middleware
async def middleware1(request, handler):
    # print('Middleware开始')
    # print(request.raw_headers)
    headers = {}
    for (key,value) in request.raw_headers:
        headers[str(key, "utf-8")] = str(value, "utf-8")
    # print(headers.get('authorization',None))
    authorization = headers.get('authorization',None)
    data = {
        'code': 0,
        'data': '',
        'msg' :''
    }
    if authorization: # 验证JWT
        YZ = checkJWT(authorization)
        # print(YZ)
        if YZ['isTrue']: # jwt 正确
            # print('jwt正确')
            if YZ['isOver']: # jwt过期
                # print('jwt过期')
                data['code'] = 100
                data['msg'] = '用户登陆过期!'
                return web.json_response(data)
            else:
                # print('jwt正常进入处理请求函数')
                response = await handler(request,YZ['payload'])
                if YZ['newJWT']: # 有新的jwt
                    # print(YZ['newJWT'])
                    response.headers['Authorization'] = YZ['newJWT']
                    return response
                else:
                    return response
        else : #jwt 错误
            # print('jwt 错误')
            data['code'] = 101
            data['msg'] = 'token验证失败!'
            return web.json_response(data)

    else :
        # Payload = None
        response = await handler(request)
        # print('Middleware结束')
        return response

def checkJWT(authorization):
    """
    判断JWT是否正确
    """
    arr = authorization.split('.')
    Payload =json.loads(debase_64(arr[1])) 
    # print(Payload)
    data = {
        'isTrue': False, # jwt是否正确
        'isOver': False, # jwt是否过期
        'newJWT': None, # 新的jwt
        'payload': None 
    }
    Header = {
        "alg": "HS256",
        "typ": "JWT"
    }
    secret = 'pyblog'
    Signature = hmac_sha256(base_64(json.dumps(Header, indent=2)) + "." +base_64(json.dumps(Payload, indent=2)),secret)
    timenow = datetime.now().timestamp() # 当前时间戳
    overtime = timenow + 60*60*2 # JWT过期时间
    if Signature==arr[2]: # jwt是否正确
        data['isTrue'] = True
    oldovertime = debase_64(arr[3])   
    if oldovertime < oldovertime: # 是否过期
        if oldovertime and ((timenow - float(oldovertime)) > 10*60*60): # 当前时间-过期时间10分钟
            data['isOver'] = True
        else: # 如果没有超过10分钟，生成一个新的JWT
            # Payload['over_time'] = overtime
            data['newJWT'] = base_64(json.dumps(Header, indent=2))+'.'+base_64(json.dumps(Payload, indent=2))+'.'+Signature+'.'+base_64(str(overtime))
        
    data['payload'] = Payload
    return data