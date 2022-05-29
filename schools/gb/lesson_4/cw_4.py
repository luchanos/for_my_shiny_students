# from lesson_5.cw_importer import my_func
import sys
from sys import argv
from datetime import datetime as dt

from functools import reduce, partial
from itertools import count, cycle
from asyncio import sleep as asleep

from time import sleep
from datetime import *

"""ВРЕМЯ РАБОТЫ ПРОГРАММЫ"""
# start = dt.now()
# print(f"Start working at: {start}")
# sleep(3)
# finish = datetime.now()
# print(f"Finish at: {finish}. Working time: {finish - start}")

"""РАНДОМНЫЕ ЧИСЛА"""
# from random import random, randint, randrange
#
# print(random())
# print(randint(1, 2))
# print(randrange(1, 10, 2))  # начало конец шаг


"""ПРОКИДЫАНИЕ ПАРАМЕТРОВ В ФУНКЦИЮ"""
from sys import argv


def my_shiny_func(a, b):
    return a / b

# _, a, b = argv

# try:
#     a = int(a)
#     b = int(b)
# except ValueError as err:
#     print(f"Ошибка: {err}")
#     a = 1
#     b = 1

# print(my_shiny_func(int(a), int(b)))

"""ГЕНЕРАТОРЫ СПИСКОВ (LIST COMPREHENSION)"""

# def my_shiny_func(a, b):
#     return a / b
#     print(123)
#
#
# my_shiny_func(1, 2)
# my_shiny_func(1, 2)
# my_shiny_func(1, 2)
# my_shiny_func(1, 2)


# если бы их не было мы бы получали списки вот так:
# a = []
# cnt = 10
# buf = 0
#
# while buf < cnt:
#     a.append(buf)
#     buf += 1
#
# print(a)
# a = []
# for el in range(10):
#     a.append(el)

# a = [str(el / 2 * 100)[1:-1] for el in range(10) if el % 2 == 0]
# print(a)
# b = {str(el / 2 * 100)[1:-1] for el in range(10) if el % 2 == 0}
# print(b)

# # а можно вот так
# a = [x for x in range(10)]
# print(a)
# # и ещё и условие указать
# a = [x for x in range(10, 100, 2) if x > 5]
# print(a)
# и даже вложенные циклы

# f = []
# for a in range(5):
#     if a % 2 == 1:
#         for b in range(12):
#             for c in range(13):
#                 f.append(a + b + c)

# a = [a[0] + b + c for a in [[1, 2], [3, 4]] for b in range(12) for c in range(13)]
# print(a)
# print(len(a))
# print(5 * 12 * 13)

"""УДИВИТЕЛЬНО! НО ЭТО РАБОТАЕТ И НА МНОЖЕСТВАХ И НА СЛОВАРЯХ!!!"""
# s = {x for x in range(10)}
# print(s)

# d = {}
# for k in range(10):
#     for v in range(10):
#         d[k] = v
#
# print(d)

# d = {}
# for k in range(10):
#     for v in range(10):
#         d[k] = v

# for k, v in [(0, 0), (1, 1), (2, 2), (3, 3)]:
#     print(k, v)


# l = [(k, v) for k in range(3) for v in range(3)]
# print(l)
# d = {k: v for k in range(3) for v in range(3)}
# d = {k: v for k, v in [(0, 0), (1, 1), (2, 2), (3, 3)]}
# d = {k: v for k, v in ((1, 'a'), (2, 'b'))}
# print(d)

# создаётся генератор!
# t = (x for x in range(5))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))


# def gen_f():
#     print("до первого")
#     yield 0
#     print("до второго")
#     yield 1
#     print("fdbfdsgbfs")
#     yield 2
#     print("fdbfdsgbfs")
#     yield 3
#     print("fdbfdsgbfs")
#     yield 4


# t = gen_f()
# print(t)
# for el in t:
#     print(el)

# a = {1: 10, 2: 20, 3: 30}
# b = [[i, a[i]] for i in a]
# # print(b)
# print([j for i in b for j in i])

"""А ТЕПЕРЬ САМОЕ ГЛАВНОЕ - КОНСТРУКЦИЯ YIELD"""
# def simple_pistolet():
#     return 1
#     return 1
#     return 1
#     return 1
#     return 1


# print(simple_pistolet())


# def simple_pistolet():
#     yield 1
#     print("Между 1 и 2")
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# c = simple_pistolet()
# print(next(c))
# print("Привет, ребята!")
# print(next(c))
# print("Как дела???!")
# print(next(c))


# for el in c:
#     print(el)

# g = simple_pistolet()
# print(type(g))
# for el in g:
#     print(el)

# def simple_pistolet_new(cnt):
#     shoots = 0
#     while shoots < cnt:
#         shoots += 1
#         yield shoots


# t = simple_pistolet_new(5)
# for el in t:
#     print(el)

# glock = simple_pistolet_new(5)
#
# aim = {bullet for bullet in glock if bullet % 2 == 0}
# print(aim)
# print(type(glock), glock)
# print(glock)

# def oboyma(ammo_capacity):
#     shoot_cnt = 0
#     while True:
#         shoot_cnt += 1
#         yield f"{shoot_cnt} bullet!"
#         if shoot_cnt == ammo_capacity:
#             return "chik! Ammo is empty"


# aim = []
# glock = oboyma(3)
# print(glock)
# shoot = next(glock)
# print(shoot)
# aim.append(shoot)
#
# try:
#     while True:
#         print(next(glock))
# except Exception as err:
#     print("ERROR:", err)

# def ranger(start, finish):
#     while start <= finish:
#         yield start
#         start += 1

# a = ranger(0, 9)
# print(a)
# print(2 in a)
# # print(2 in a)
# print([x for x in a])



# def list_ranger(start, finish):
#     res = []
#     while start <= finish:
#         res.append(start)
#         start += 1
#     return res



# print(type(simple_pistolet), simple_pistolet)
# print(type(simple_pistolet_new), simple_pistolet_new)
# res1 = simple_pistolet()
# res2 = simple_pistolet_new()
# print(type(res1), res1)
# print(type(res2), res2)

# ЯВЛЯЕТСЯ ИТЕРАТОРОМ
# ЗАЧЕМ????

# def yelder(limit):
#     cnt = 0
#     while cnt <= limit:
#         yield cnt
#         cnt += 1

# start = dt.now()
# print(f"Start working at: {start}")
# # a = [x for x in range(100_000_000)]
# a = yelder(100_000_000)
# print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
# print(f"Size of object: {sys.getsizeof(a)}")
# a = range(100)
# print(sys.getsizeof(a))


# def list_ranger(start, finish):
#     while start <= finish:
#         # print(start)
#         yield start
#         start += 1


# start = datetime.now()
# print(f"Start working at: {start}")
# r_list = list_ranger(0, 3)
# r_list = ranger(0, 10)
# print(f"size of object: {sys.getsizeof(r_list)}")
# print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
# for el in r_list:
#     print(el)
# print(3 in r_list)



# 859724472 0:00:26.216637

# cnt = 0
# r_list = list_ranger(0, 10)
# res = []

# for el in r_list:
#     res.append(el)

# res = {el * 100 for el in r_list if el % 2 == 1 and el > 5}
# print(res)

# while cnt < 10:
#     res.append(next(r_list))
#     cnt += 1
#
# print(res)



"""МОДУЛЬ FUNCTOOLS"""
# def one_func(partial_obj):
#     arg = 2
#     return partial(partial_obj, a=arg)
#
#
# def another_func(partial_obj):
#     arg = 300
#     return partial(partial_obj, c=arg)
#
#
# def division(a, b, c):
#     return a / b + c
#
#
# p_o = partial(division, b=100)
# p_o = partial(p_o, a=10)
# p_o = partial(p_o, c=100)
# print(p_o())
# можем указать, какой из аргументов прокинуть
# p_o = one_func(p_o)
# p_o = another_func(p_o)
# print(p_o)
# print(p_o())

# p_o = partial(division, b=100)
# p_o = partial(p_o, a=3)
# # p_o = partial(p_o, c=400)
# print(p_o(c=400))

# def summarize(a, b):
#     return a + b
#
#
# res = 0
# a = [0, 1, 2, 3, 4, 5]
# print(reduce(summarize, a))


# for x in count(4):
#     print(x)
#     sleep(.5)

# a = [0, 1, 2, 3]
# for x in cycle(a):
#     print(x)
#     sleep(.5)

def f():
    print(123)


def n():
    print(23564)
