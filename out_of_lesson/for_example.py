import asyncio
import asyncpg
from datetime import datetime
from asyncio import sleep

simple_query = "select * from some_test_table limit $1"
insert_query = "insert into some_test_table values ($1, $2, $3)"

# синхронная работа - 0:00:17.145996


async def make_request_model(db_pool):
    await sleep(.1)
    await db_pool.fetch(insert_query, 100, 'test_data', 101)


async def make_request_to_db():
    db_pool = await asyncpg.create_pool(host="127.0.0.1", port=5432, database="postgres")
    start = datetime.now()

    batch_size = 200
    pended = 0
    tasks = []
    for x in range(10_000):
        tasks.append(asyncio.create_task(make_request_model(db_pool)))
        pended += 1
        if len(tasks) == batch_size or pended == 10_000:
            await asyncio.gather(*tasks)
            tasks = []
            print(f"I've done {pended} requests")
    finish = datetime.now() - start
    print(finish)

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request_to_db())
