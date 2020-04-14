# import asyncio
# import aiomysql
# loop = asyncio.get_event_loop() #返回当前 OS 线程中正在运行的事件循环
# async def test_example():
#     conn = await aiomysql.connect(
#         host='127.0.0.1', 
#         port=3306,
#         user='root',
#         password='newpassword',
#         db='demo',
#         loop=loop)

#     cur = await conn.cursor()
#     await cur.execute("SELECT title,author FROM tbl")
#     print(cur.description)
#     r = await cur.fetchall()
#     print(r)
#     await cur.close()
#     conn.close()

# loop.run_until_complete(test_example())

import asyncio
import sqlalchemy as sa

from aiomysql.sa import create_engine

loop = asyncio.get_event_loop() #返回当前 OS 线程中正在运行的事件循环

metadata = sa.MetaData()
tbl = sa.Table('tbl', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String(100)),
    sa.Column('author', sa.String(40)),
    sa.Column('date', sa.DateTime),
)

## 插入查询
async def go():
    engine = await create_engine(
        host='127.0.0.1', 
        port=3306,
        user='root',
        password='newpassword',
        db='demo',
        loop=loop)
    async with engine.acquire() as conn:
        # await conn.execute(tbl.insert().values(val='abc'))  # 插入
        # await conn.execute(tbl.insert().values(val='xyz'))
        
        # res = await conn.execute(tbl.select(tbl.c.id == 5))  # 条件查询
        # await conn.execute(tbl.update().where(tbl.c.id==5).values(val='update'))
        # await conn._commit_impl()  # commit https://github.com/aio-libs/aiomysql/issues/473
        try:
            result = await conn.execute(tbl.select())
            res = await result.fetchall()
            for row in res:
                print(row)
        except Exception as e :
            print(e)
            
    engine.close()
    await engine.wait_closed()

loop.run_until_complete(go())