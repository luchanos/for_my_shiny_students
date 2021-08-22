# примерочная. Всего их 10 штук
# Semaphore - распорядитель торгового зала, который следит за загрузкой примерочных
# acquire - мы заняли примерочную
# release - мы освободили примерочную
import asyncio
from asyncio import Semaphore
import time
from random import random

num = 0


async def main_task():
    global num
    await asyncio.sleep(random())
    num += 1
    print(f"Производится примерка чего либо. На сегодня это уже {num} клиент")


async def get_some_dress(semaphore: Semaphore):
    await semaphore.acquire()  # занимаем примерочную, счетчик свободных примерочных уменьшится на 1
    start = time.time()
    await main_task()
    time_of_work = time.time() - start
    print("ВРЕМЯ РАБОТЫ:", time_of_work)
    await asyncio.sleep(1 - time_of_work)
    semaphore.release()  # освобождаем примерочную, счетчик свободных примерочных увеличится на 1


async def main():
    semaphore = Semaphore(1)  # распорядитель торгового зала и количество примерочных
    tasks_from_customers = [get_some_dress(semaphore) for _ in range(100)]
    await asyncio.wait(tasks_from_customers)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
