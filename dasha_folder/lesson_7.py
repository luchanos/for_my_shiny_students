"""ДЗ - всё что не успела за прошлые уроки (6 урок)

УЧИТЬ ДЕЛЕНИЕ И ЕГО ВИДЫ! ЕЩЕ РАЗ ВСЕ ПОВТОРИТЬ!
БУДЕТ ЭКЗАМЕН ПО УСТНОМУ СЧЕТУ!

my_func() и my_func понимать разницу!

Разобраться с прокидыванием функций внутрь функций!!!!!
"""
# c = print
# print(c)
# print(type(c))


# просто цикл
# cnt = 0
# limit = 10
# while cnt < limit:
#     print(cnt)
#     cnt += 1

# c = 1  # какая-то константа


# а теперь упакуем его логику в функцию
# def cycle_func(cnt, limit):
#     b = 1  # эта переменная видна только из функции (изнутри наружу можно, но не наоборот)
#     print(c)  # эта переменная будет видна
#     while cnt < limit:
#         print(cnt)
#         cnt += 1


# cnt = 0
# limit = 30
# cycle_func(cnt, limit)

# print(b)  # тут упадёт ошибка

# def another_func():
#     print("Реклама")
#     print("Реклама")
#     print("Реклама")

# another_func()

# print(another_func)

# def multiplyer(lst):
#     if len(lst) == 0:
#         print("пустой лист!")
#     else:
#         res = 1
#         for el in lst:
#             res *= el
#         # print(res)
#         return res


# def informator(value):
#     print("Результат равен: %d" % value)


# lst = [1, 2, 3, 4, 5]
# multiplyer([])
# res = multiplyer(lst)
# res = informator(res)
# print(res)


# def cycle_func(cnt, limit, a, n):
#     b = 1  # эта переменная видна только из функции (изнутри наружу можно, но не наоборот)
#     # print(c)  # эта переменная будет видна
#     while cnt < limit:
#         print(cnt)
#         cnt += 1
#
#
# cycle_func(1, 2, 1, 1)  # прокидываем аргументы по позиции
# cycle_func(1, 3, n=5, a=1)  # прокидываем аргументы по имени

# def make_list(n):
#     res = []
#     cnt = 0
#     while cnt < n:
#         res.append(cnt)
#         cnt += 1
#     return res
#
#
# res = make_list(10)


# comprehensions их ещё называют генераторами коллекций, но не рекомендую использовать этот термин! потому что
# есть еще и генераторы-итераторы и это вызывает путаницу

# for el in res:
#     print(el)
# print(res)
# print(1 % 2)
# res1 = [el for el in res if (el * 100) % 2]
# res1 = [(str(el) + "*") * 3 for el in res if el % 2]
# res2 = [el for el in res if el % 2 == 0]
# res3 = [((str(el) + "*") * 3, 1000000000) for el in res if el % 2]
# res4 = [((str(el) + "*") * 3, chr(el)) for el in res if el % 2]  # chr переводит число в его эквивалент символа ASCII
# s1 = {el for el in res}
# print(res1, res2)
# print(res3)
# print(res4)

# выводит Дашу из себя (на самом деле просто берет сивол из таблицы ASCII с порядковым номером el)
# for el in range(1000):
#     print(chr(el))

# как правило константы пишут большими буквами. Это ни на что не влияет, кроме человеческого восприятия
# SOME_CONST = 0


# def my_func():
#     global SOME_CONST
#     SOME_CONST += 1
#     print(SOME_CONST)
#
#
# def my_func1():
#     global SOME_CONST
#     SOME_CONST += 1
#     print(SOME_CONST)
#
#
# def my_func2():
#     global SOME_CONST
#     SOME_CONST += 1
#     print(SOME_CONST)


# print(my_func())
# print(my_func)
# my_func()
# my_func1()
# my_func2()
# print(SOME_CONST)


SOME_CONST = 0


def my_func():
    global SOME_CONST
    SOME_CONST += 1
    print(SOME_CONST)


def func(fasdvadifjb):
    print("щас как запущу функцию, которую мне прокинули в качестве параметра!")
    fasdvadifjb()


# func(f'{my_func}')
# print(my_func)
func(my_func)
