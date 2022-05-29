import sys
from functools import reduce
from itertools import cycle, count
from time import sleep
from datetime import datetime as dt

"""ВРЕМЯ РАБОТЫ ПРОГРАММЫ"""
# start = dt.now()
# print(f"Start working at: {start}")
# sleep(3)
# finish = dt.now()
# print(f"Finish at: {finish}. Working time: {finish - start}")

"""РАНДОМНЫЕ ЧИСЛА"""
# from random import random, randint, randrange
#
# print(random())
# print(randint(1, 20))
# print(randrange(1, 10, 2))  # начало конец шаг

# """ПРОКИДЫАНИЕ ПАРАМЕТРОВ В ФУНКЦИЮ"""
# from sys import argv
#
#
# def send_emails(*args, **kwargs):
#     for email in args:
#         print(f"Письмо на почту {email} отправлено")
#
# # если запуск из модуля
# # send_emails('lol@mail.ru', 'kek@mail.ru', 'cheburek@mail.ru')
#
# # если запуск из консольки
# send_emails(*argv[1:])

# надо сделать список с числами от 0 до 10
# l = []
# for el in range(11):
#     l.append(el)

# эквивалент через генератор списков (list comprehension)
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# l = [str(pow(el / 123, 3)) for el in a if el % 2 != 0]
# s = {str(pow(el / 123, 3)) for el in a if el % 2 != 0}
# t = tuple(str(pow(el / 123, 3)) for el in a if el % 2 != 0)
#
# print(l)
# print(s)
# print(t)

"""УДИВИТЕЛЬНО! НО ЭТО РАБОТАЕТ И НА МНОЖЕСТВАХ И НА СЛОВАРЯХ!!!"""
# d = {}
# for k in range(10):
#     d[k] = k
#
# print(d)
# l1 = [((1, 2), (1, 2, (1, 2, 3, 4))), (2, "some"), (3, "blabla")]

# d = {}
# for kort in l1:
#     d[kort[0]] = kort[1]

# print({el: el for el in range(10)})
# print({k: v for k, v in l1})

# for k, v, z in [(0, 0, 1), (1, 1, 6), (2, 2, 7), (3, 3, 9)]:
#     print(k, v, z)

# l = [(k, v) for k in range(3) for v in range(3)]
# print(l)
# d = {k: v for k in range(3) for v in range(3)}
# d = {k: v for k, v in [(0, 0), (1, 1), (2, 2), (3, 3)]}
# d = {k: v for k, v in ((1, 'a'), (2, 'b'))}
# print(d)

# from lesson_4.cw_4 import f
# f()

# проверяем, что наш модуль, который запускаем - основной!
# if __name__ == "__main__":
#     a = [x for x in range(100)]
#     print(a)

# print((x for x in range(10)))


def my_range(a):
    print("начинаю работу по генерации чисел")
    cnt = 0
    while cnt < a:
        yield cnt
        cnt += 1
    yield 'test'
    yield 'string'
    print("Закончили!!!")
#
#
# def my():
#     return 1


start = dt.now()
print(f"Start working at: {start}")
# a = [x for x in range(100_000_000)]
a = my_range(3)
print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
print(f"Size of object: {sys.getsizeof(a)}")

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# print(a)
# for el in a:
#     print(el)

# def summarize(a, b):
#     return a + b


# def f(a):
#     if a < 5:
#         return str(a) * 10


# a = [0, 1, 2, 3]
# res = reduce(summarize, a)
# print(res)

# print(list(map(f, a)))
# print(list(filter(f, a)))

# cycle, count

# for x in cycle(a):
#     print(x)
#     sleep(.5)

# for x in count(100, 105):
#     sleep(.5)
#     print(x)
