# import asyncio
# from asyncio import sleep
#
#
# async def simple_async_func(message):
#     print(message)
#     await sleep(1)
#     print(message)
#
#
# async def test():
#     tasks = []
#     tasks.append(asyncio.create_task(simple_async_func("ПЕРВЫЙ ЗАПУСК")))
#     tasks.append(asyncio.create_task(simple_async_func("ВТОРОЙ ЗАПУСК")))
#     tasks.append(asyncio.create_task(simple_async_func("ТРЕТИЙ ЗАПУСК")))
#     await asyncio.gather(*tasks)
#
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test())

# from requests import request
#
#
# while True:
#     request(method="GET", )
import asyncio
from asyncio import sleep


async def simple_func(message):
    print(message)
    await sleep(1)
    print(message)


loop = asyncio.get_event_loop()
loop.run_until_complete()
