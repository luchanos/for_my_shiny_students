"""
УЧИТЬ ДЕЛЕНИЕ И ЕГО ВИДЫ! ЕЩЕ РАЗ ВСЕ ПОВТОРИТЬ!

a % b - вернуть остаток от деление числа a на число b
a / b - классическое деление
a // b - целочисленное деление
"""
from time import sleep
from datetime import datetime

# декоратор - паттерн проектирования, который позволяет изменить поведение функции без изменения самой функции


def make_calculation(a, b):
    sleep(1)
    return a % b


# хочу посчитать время работы функции
# start = datetime.now()
# print(make_calculation(3, 2))
# print(datetime.now() - start)


# def make_calculation():
#     print("Сплю")
#     sleep(1)
#     return "Результат"


# def func(a, b=100, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)


# сначала забираю позионные (сначала обязательные, а потом нет), потом беру по ключу
# func(1, 2, 3, 4, 5, 6, d=123, c=789, e=67890)


def outer(f):  # мужик, а f - наш ящик
    print(f"Я - мужик, вы принесли мне свой ящик {f}")

    def time_calculator(*args, **kwargs):  # это ящик-заготовка, куда мужик вставляет наш ящик
        start = datetime.now()
        res = f(*args, **kwargs)
        print(datetime.now() - start)
        return res

    print(f"Я - мужик, я укомплектовал свой ящик вашим ящиком {f} и возвращаю вам обратно. Удачного использования!")
    return time_calculator  # вернул укомплектованный ящик


@outer  # аналог outer(make_calculation)
def make_calculation(a, b):
    sleep(1)
    return a / b


@outer  # outer(make_mult)
def make_mult(a, b):
    sleep(2)
    return a * b


@outer  # outer(simple)
def simple():
    print("Реклама!")


print(make_calculation(1, 2))
print(make_mult(3, 4))
simple()


# yashik_1 = outer(make_calculation)
# yashik_2 = outer(make_mult)
# yashik_3 = outer(simple)
# print(yashik_1)
# print(yashik_2)
# print(yashik_3)
# print(yashik_1(3, 2))
# print(yashik_2(3, 2))
# print(yashik_3())


# def shitty_func(a, b):
#     return a + b
#
# def outer(f):
#
#     def time_calculator(a, b):
#         return f(a, b)
#
#     return time_calculator
#
# print(outer(shitty_func)(1, 2))

"""История о черный ящиках. Есть мужик, у которого производство черных ящиков с кнопкой, которые измеряют время работы
других черных ящиков с кнопкой. У нас тоже есть несколько чёрных ящиков, каждый из которых выполняет свою собственную
логику работы. Мы хотим сделать так, чтобы наши ящики были модернизированы и теперь при запуске всегда показывали
время своей работы и возвращали результат. Мы несем свои ящики к этому мужику, а он кладёт их в свои заготовки и
возвращает нам. То есть по факту мы будем пользоваться ящиками мужика, внутри которых будут лежать наши исходные
ящики, которые мы ему отнесли."""


# def outer(f):
#
#     def time_calculator():
#         return f + 1
#
#     return time_calculator
#
#
# print(outer(1)())
