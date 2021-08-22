import asyncio
import time
from asyncio import Semaphore

num = 0


async def sleepy(semaphore: Semaphore):
    await semaphore.acquire()  # мы пытается зайти в примерочную. Если свободных примерочных нет - ждём.
    global num
    start = time.time()
    num += 1
    sleep_time = 1 - (time.time() - start)
    print(f"Выполнил увеличение каунтера! Теперь он = {num}. Спать будем - {sleep_time}")
    await asyncio.sleep(sleep_time if sleep_time > 0 else 1)
    await semaphore.release()  # мы вышли из примерочной


async def make_by_semaphore():
    semaphore = asyncio.Semaphore(value=3)
    await asyncio.wait([sleepy(semaphore) for _ in range(100)])


loop = asyncio.get_event_loop()
loop.run_until_complete(make_by_semaphore())
