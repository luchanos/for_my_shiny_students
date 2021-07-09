# Рассказать про for, итераторы и next
# посмотреть тудуху из 20го урока
"""ДЗ Грокаем алгоритмы - читать про стек вызовов. Уметь рассказать что это такое и как работает."""
from time import sleep


# def outer(func):
#     def inner(*args, **kwargs):
#         if type(args[0]) == type(args[1]):
#             # return args[0].__class__(args[0].field_a + args[1].field_a)
#             # return args[0] + args[1]
#             return func(args[0], args[1])
#         raise TypeError(f"Несовместимый для сложения тип: {type(args[0])}")
#     return inner


def type_checker(func):
    def inner(first, second):
        if type(first) == type(second):
            return func(first, second)  # прямой вызов __add__ :
        raise TypeError(f"Несовместимые типы для выполнения указанной операции: {type(first)}, {type(second)}")
    return inner


def type_checker_many(func):
    def inner(*args):
        for el in args:
            # if not isinstance(args[0], type(el)):
            if type(args[0]) != type(el):
                raise TypeError(f"MANY Несовместимые типы для выполнения указанной "
                                f"операции: {type(args[0])}, {type(el)}")
        return func(*args)
    return inner


# постановка задачи: хотим, чтобы складывать можно было только объекты одного и того же типа
class SimpleClass:
    def __init__(self, field_a):
        self.field_a = field_a

    # old version
    # def __add__(self, other):
    #     if type(self) == type(other):
    #         return SimpleClass(self.field_a + other.field_a)
    #     raise TypeError(f"Несовместимый для сложения тип: {type(other)}")

    # @type_checker
    @type_checker_many
    def __add__(self, other):
        return SimpleClass(self.field_a + other.field_a)

    @type_checker
    def __sub__(self, other):
        return SimpleClass(self.field_a - other.field_a)

    def __str__(self):
        return f"{self.field_a}"


# s1 = SimpleClass(1)
# s2 = SimpleClass(2)
# s3 = s1 + s2
# print(s3)

# @type_checker_many
# def func_many_args(a, b, c, d):
#     return a + b + c + d
#
#
# a = SimpleClass(1)
# b = SimpleClass(1)
# c = SimpleClass(1)
# d = SimpleClass(1)
# e = func_many_args(a, b, c, 1)
# print(e)


def func():  # это генераторная функция
    yield


# res_f = func()  # а вот это генератор! генератор - результат работы генераторной функции!
# print(res_f)
# print(next(res_f))
# print(next(res_f))


from datetime import datetime


class Tumbochka:
    def __init__(self):
        self.created_dt = datetime.now()
        self.content = []  # изначально тумбочка будет создаваться всегда пустая

    def add_into(self, subject):
        self.content.append(subject)

    def __str__(self):
        return f"{self.content}"

    def __iter__(self):  # итератор - это то, что вернет этот метод. генератор - частный случай итератора.
        yield


tumbochka = Tumbochka()
tumbochka.add_into(1)
tumbochka.add_into(False)
it = iter(tumbochka)
print(it)
print(next(it))
print(next(it))
# print(tumbochka)

col_1 = [1, 2, 3, 4]
col_2 = "abcd"
col_3 = {6, 7, 8, 9}

# for el in col_1:
#     print(el)

# while True:
#     print(next(col_1))

# total_spisok = [col_1, col_2, col_3, tumbochka]

# Лютый говнокод
# for collection in total_spisok:
#     if type(collection) == Tumbochka:
#         iterable_obj = collection.content
#     else:
#         iterable_obj = collection
#         for predmet in iterable_obj:
#             print(predmet)

# for col in total_spisok:
#     for predmet in col:
#         print(predmet)
