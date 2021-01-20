# from time import sleep
#
#
# def make_request(cnt):
#     print("Я делаю запрос в БД", cnt)
#     sleep(.1)
#
#
# cnt = 0
# for _ in range(10_000):
#     make_request(cnt)
#     cnt += 1
import asyncio
from asyncio import sleep
import asyncpg

QUERY = """INSERT INTO some_test_table VALUES ($1, $2, $3)"""


async def make_request(db_pool):
    await db_pool.fetch(QUERY, 1, "some string", 3)
    await sleep(.1)


async def main():
    chunk = 200
    tasks = []
    pended = 0

    db_pool = await asyncpg.create_pool("postgresql://127.0.0.1:5432/postgres")

    for x in range(10_000):
        tasks.append(asyncio.create_task(make_request(db_pool)))
        pended += 1
        if len(tasks) == chunk or pended == 10_000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
