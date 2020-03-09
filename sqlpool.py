import asyncio
import aiomysql
loop = asyncio.get_event_loop() #返回当前 OS 线程中正在运行的事件循环
async def test_example():
    conn = await aiomysql.connect(
        host='127.0.0.1', 
        port=3306,
        user='root',
        password='newpassword',
        db='demo',
        loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT title,author FROM tbl")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())