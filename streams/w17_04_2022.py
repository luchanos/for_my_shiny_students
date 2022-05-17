from sys import getsizeof

# l = [x for x in range(10)]
# print(l)


fig = [x for x in range(100)]

# for some_fig in fig:
#     print("Протираю фигурку:", some_fig)
# print("Памяти затрачено на хранение", getsizeof(fig))


# генераторная функция
def fig_gen_func():  # результат - это объект-генератор
    cnt = 0
    while cnt < 10:
        yield cnt
        cnt += 1


def simple_func():
    return 1


# print(simple_func())
# print(fig_gen_func())

# f = print
# print(f)

gen = fig_gen_func()

# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)
# some_figure = next(gen)
# print(some_figure)

# for fig in gen:
#     print(fig)

# print(next(gen))

# try:
#     while True:
#         print(next(gen))
# except StopIteration:
#     pass

# print()
# print(getsizeof(fig))
# print(getsizeof(gen))


# def skat(n):
#     """Функция, которая возвращает последовательность от 0 до n"""
#     # сознательно не используем тут range, потому как range является объектом-итератором.
#     res = []
#     cnt = 0
#     while cnt < n:
#         res.append(cnt)
#         cnt += 1
#     return res
#
#
# def first_eater(eda_list):
#     """Первый подопытный"""
#     for eda in eda_list:
#         print(f"Первый подопытный съел {eda} и написал: ", str(eda))
#
#
# def second_eater(eda_list):
#     """Второй подопытный"""
#     for eda in eda_list:
#         print(f"Второй подопытный съел {eda} и написал: ", str(eda) * 4)
#
#
# def third_eater(eda_list):
#     """Третий подопытный"""
#     for eda in eda_list:
#         print(f"Третий подопытный съел {eda} и написал: ", str(eda) * 10)
#
#
# # заряжаем скатерть
# eda_list = skat(100_000_000)
# # задаём параметры голода
# golod_1 = 2
# golod_2 = 3
# golod_3 = 4
# # кормим
# first_eater(eda_list[:golod_1])
# second_eater(eda_list[golod_1:golod_2 + golod_1])
# third_eater(eda_list[golod_2 + golod_1:golod_2 + golod_1 + golod_3])


def skat(n):
    """Функция, которая возвращает объект-генератор, способный предоставить нам
    элементы по запросу от 0 до n"""
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


def first_eater(golod, skat):
    """Первый подопытный"""
    while golod > 0:
        eda = next(skat)
        print(f"Первый подопытный съел {eda} и в результате написал: ", eda)
        golod -= 1


def second_eater(golod, skat):
    """Второй подопытный"""
    while golod > 0:
        eda = next(skat)
        print(f"Второй подопытный съел {eda} и в результате написал: ", str(eda) * 4)
        golod -= 1


def third_eater(golod, skat):
    """Третий подопытный"""
    eda = next(skat)
    while golod > 0:
        print(f"Третий подопытный съел {eda} и в результате написал: ", str(eda) * 10)
        golod -= 1


skat_gen_obj = skat(3)
golod_1 = 1
golod_2 = 20
golod_3 = 4

try:
    first_eater(golod_1, skat_gen_obj)
    second_eater(golod_2, skat_gen_obj)
    third_eater(golod_3, skat_gen_obj)
except StopIteration:
    print("Заряды в скатерти кончились!")


# https://habr.com/ru/company/domclick/blog/560300/
# livecoding