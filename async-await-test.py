# 
# Created by 付博文 on 2017/10/10.
#

# async和await是针对coroutine的新语法
import asyncio


@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")


async def hello2():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


loop = asyncio.get_event_loop()
tasks=[hello(),hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
