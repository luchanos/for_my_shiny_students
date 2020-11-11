# from lesson_5.cw_importer import my_func
import sys
from datetime import datetime as dt, datetime
from functools import reduce, partial
from itertools import count, cycle
from time import sleep

"""ВРЕМЯ РАБОТЫ ПРОГРАММЫ"""
# start = dt.now()
# print(f"Start working at: {start}")
# sleep(3)
# print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")




"""РАНДОМНЫЕ ЧИСЛА"""
# from random import random, randint, randrange
#
# print(random())
# print(random() + randint(1, 300))
# print(randrange(1, 10, 2))  # начало конец шаг












"""ПРОКИДЫАНИЕ ПАРАМЕТРОВ В ФУНКЦИЮ"""
# from sys import argv
#
#
# def my_shiny_func(a, b):
#     return a / b
#
#
# file_path, a, b = argv
# print(argv)
# print(my_shiny_func(int(a), int(b)))










"""ГЕНЕРАТОРЫ СПИСКОВ (LIST COMPREHENSION)"""
# если бы их не было мы бы получали списки вот так:
# a = []
# cnt = 10
# buf = 0
#
# while buf < 10:
#     a.append(buf)
#     buf += 1
#
# print(a)



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

# d = {k: v for k in range(10) for v in range(10)}
# d = {k: v for k, v in (enumerate('abcdefg'))}
# d = {k: v for k, v in ((1, 'a'), (2, 'b'))}
# print(d)

"""А ТЕПЕРЬ САМОЕ ГЛАВНОЕ - КОНСТРУКЦИЯ YIELD"""
# def simple_pistolet():
#     return 1
#     return 1
#     return 1
#     return 1
#     return 1
#
#
# print(simple_pistolet())


# def simple_pistolet_new(cnt):
#     shoots = 0
#     while shoots < cnt:
#         shoots += 1
#         yield shoots
#
#
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

def ranger(start, finish):
    while start <= finish:
        yield start
        start += 1

# a = ranger(0, 9)
# print(a)
# print(2 in a)
# # print(2 in a)
# print([x for x in a])



def list_ranger(start, finish):
    res = []
    while start <= finish:
        res.append(start)
        start += 1
    return res



# print(type(simple_pistolet), simple_pistolet)
# print(type(simple_pistolet_new), simple_pistolet_new)
# res1 = simple_pistolet()
# res2 = simple_pistolet_new()
# print(type(res1), res1)
# print(type(res2), res2)

# ЯВЛЯЕТСЯ ИТЕРАТОРОМ
# ЗАЧЕМ????
# a = [x for x in range(100_000_000_000)]




# start = datetime.now()
# print(f"Start working at: {start}")
# a = [x for x in range(100)]
# print(f"Finish at: {datetime.now()}. Working time: {datetime.now() - start}")
# print(f"Size of object: {sys.getsizeof(a)}")
# a = range(100)
# print(sys.getsizeof(a))






# start = datetime.now()
# print(f"Start working at: {start}")
# r_list = list_ranger(0, 100_000_000)
# r_list = ranger(0, 10)
# print(f"size of object: {sys.getsizeof(r_list)}")
# print(f"Finish at: {datetime.now()}. Working time: {datetime.now() - start}")
# print(3 in r_list)

# 859724472 0:00:26.216637







"""МОДУЛЬ FUNCTOOLS"""
def one_func(partial_obj, arg):
    return partial(partial_obj, a=arg)


def another_func(partial_obj, arg):
    return partial(partial_obj, c=arg)


def division(a, b, c):
    return a / b + c


# p_o = partial(division, b=100)  # можем указать, какой из аргументов прокинуть
# p_o_2 = one_func(p_o, 2)
# p_o_3 = another_func(p_o_2, 300)
# print(p_o_3)
# print(p_o_3())

# p_o = partial(division, b=100)
# p_o = partial(p_o, a=3)
# # p_o = partial(p_o, c=400)
# print(p_o(c=400))



# def summarize(a, b):
#     return a * b
#
# res = 0
# a = [0, 1, 2, 3, 4, 5]
# print(reduce(summarize, a))

# for x in count(4):
#     print(x)
#     sleep(1)

a = [0, 1, 2, 3]
for x in cycle(a):
    print(x)
    sleep(1)
