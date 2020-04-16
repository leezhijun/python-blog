import asyncio
from conf.config import sqlConfig
from aiomysql.sa import create_engine

class SQLcontroller:
    __engine=None
    __isinstance = False
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:  # 如果被实例化了
            return cls.__isinstance  # 返回实例化对象
        print('连接到数据库...')
        # asyncio.get_event_loop().run_until_complete(SQLcontroller.connect())
        cls.__isinstance = object.__new__(cls)  # 否则实例化
        return cls.__isinstance  # 返回实例化的对象
 
    @staticmethod
    async def connect():
        try:
            __engine = await create_engine(
                host=sqlConfig['host'],
                port=sqlConfig['port'],
                user=sqlConfig['user'],
                password=sqlConfig['password'],
                db=sqlConfig['db'],
                minsize=1,
                maxsize=10,
                autocommit=True)
            if __engine:
                SQLcontroller.__engine = __engine
                SQLcontroller.connectStatue =True
                print('连接数据库成功!')
            else:
                raise ("连接数据库失败!")
        except:
            print('连接错误.', exc_info=True)
 
    # 查询所有
    # def selectAll(self,sql):
    #     data = {
    #         'code': 0,
    #         'data': None,
    #         'msg': ''
    #     }
    #     async def select():
    #         conn = await SQLcontroller.__engine.acquire()
    #         try:
    #             result = await conn.execute(sql)
    #             res = await result.fetchall()
    #             data.data = res
    #             return data
    #         except Exception as e :
    #             # return e
    #             data.code = 100
    #             data.msg = e
    #             return data
    #         finally:
    #             pass
    #     res = await select()
    #     return res

    async def selectAll(self,sql):
        data = {
            'code': 0,
            'data': None,
            'msg': ''
        }
        conn = await SQLcontroller.__engine.acquire()
        try:
            result = await conn.execute(sql)
            res = await result.fetchall()
            data.data = res
            return data
        except Exception as e :
            # return e
            data.code = 100
            data.msg = e
            return data
        finally:
            pass

    # 查询一条
    # def selectOne(self,sql):
    #     async def first():
    #         conn = await SQLcontroller.__engine.acquire()
    #         try:
    #             result = await conn.execute(sql)
    #             res = await result.fetchone()
    #             return res
    #         except Exception as e :
    #             print(e)
    #         finally:
    #             # SQLcontroller.__engine.release(conn)
    #             pass
    #     # asyncio.get_event_loop().run_until_complete(first())
    
    # # 增加数据
    # def addData(self,sql):
    #     async def add():
    #         conn = await SQLcontroller.__engine.acquire()
    #         try:
    #             result = await conn.execute(sql)
    #             # res = await result.fetchone()
    #             return result
    #         except Exception as e :
    #             print(e)
    #         finally:
    #             # SQLcontroller.__engine.release(conn)
    #             pass
    #     # asyncio.get_event_loop().run_until_complete(add())

    # # 修改数据
    # def updateData(self,sql):
    #     async def update():
    #         conn = await SQLcontroller.__engine.acquire()
    #         try:
    #             result = await conn.execute(sql)
    #             # res = await result.fetchone()
    #             return result
    #         except Exception as e :
    #             print(e)
    #         finally:
    #             # SQLcontroller.__engine.release(conn)
    #             pass
    #     # asyncio.get_event_loop().run_until_complete(update())

    # # 删除数据
    # def delData(self,sql):
        # async def delete():
        #     conn = await SQLcontroller.__engine.acquire()
        #     try:
        #         result = await conn.execute(sql)
        #         # res = await result.fetchone()
        #         return result
        #     except Exception as e :
        #         print(e)
        #     finally:
        #         # SQLcontroller.__engine.release(conn)
        #         pass
        # asyncio.get_event_loop().run_until_complete(delete())