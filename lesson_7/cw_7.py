from typing import List
from time import sleep
from datetime import datetime
import requests
from abc import ABC, abstractmethod


class Point2D:
    """Двумерная точка"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"координата x: {self.x}, координата y: {self.y}"

    def __repr__(self):
        return f"координата x: {self.x}, координата y: {self.y}"

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)


    def __mul__(self, other):
        return Point2D(self.x * other.x, self.y * other.y)

    def __iter__(self):
        return (el for el in [1, 2])

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    @property
    def get_very_hard_evaluation(self):
        return self.y + self.x

    def test(self, *args, **kwargs):
        pass


class AllPointHeap:
    def __init__(self, point_1: Point2D, point_2: Point2D):
        self.point_1 = point_1
        self.point_2 = point_2

    def get_sum_sum_coor(self):
        return self.point_1.get_very_hard_evaluation + self.point_2.get_very_hard_evaluation


class Test:
    def __init__(self):
        self.field = None

    def test_method(self):
        self.field = Point2D(1, 2)

# tobj = Test()
# tobj.test_method()
# c = 1


class Point3D(Point2D):
    """Трёхмерная точка"""
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"{super().__str__()}, координата z: {self.z}"

    def __eq__(self, other):
        if not super().__eq__(other):
            return False
        return True if self.z == other.z else False

    def __add__(self, other):
        c = 1
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)


# point_3 = AllPointHeap(point_2d, point_1d)

# print(point_3.get_sum_sum_coor())
#
#
# point_3d = Point3D(1, 2, 3)
# point_3d2 = Point3D(4, 2, 3)
# new_p = point_3d + point_3d2 + point_3d2 + point_3d2 + point_3d2 + point_3d2 + point_3d2
# c = 1
# point_3d = Point3D(1, 2, 3)
# print(point_2d)

# print(point_3d == point_3d2)


class Animal(ABC):
    @abstractmethod
    def feed(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def feed(self):
        print("Меня кормят")


class Oter(Dog):
    def voice(self):
        print("Гав")

    def dance(self):
        print("Я танцую")


class User:
    def __init__(self, field):
        self.field = field

    @property
    def get_discount_status(self):
        return requests.get("https://google.com")



###################################
############ ИТЕРАТОРЫ ############
###################################

import sys
from itertools import repeat, count

# Итерируемые объекты (iterable) — это любые объекты, предоставляющий возможность поочерёдного прохода по циклу.
from time import sleep

my_list = [1, 2, 3]
my_dict = {1: "a", 2: "b", 3: "c"}
my_set = {"lol", "kek", "cheburek"}


# простая петля
# for element in my_set:
#     print(element)

# for element in my_dict:
#     print(element)

# iterator = iter(my_list)
# print(next(my_list))  # упадёт ошибка
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# numbers = [1, 2, 3, 4, 5, 6]
# squares = (n**2 for n in numbers)
# print(9 in squares)
# print(9 in squares)
# print(next(squares))


def simple_gen(start, finish=5):
    while start <= finish:
        yield start
        start += 1


class MyShinyIterator:
    def __init__(self, start):
        self.i = start
        # self.buf = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration("Итерация окончена")

    # def to_start(self):
    #     self.i = self.buf

    def __iter__(self):
        c = 1
        return self


class TumbCollection:
    """
    Объект, поддерживающий интерфейс итерации (итерируемый объект)
    """
    def __init__(self, start):
        self.start = start - 1

    def __iter__(self):
        c = 1
        # Метод __iter__ должен возвращать объект-итератор (генератор - это подвид итератора)
        return simple_gen(self.start)


# Ключевой вопрос - что можно итерировать? Ответ - то, что реализует интерфейс итерации.
# obj = TumbCollection(start=1)
# for el in obj:
#     print(el)
# print("тумб второй проход")
# for el in obj:
#     print(el)

# print("************")
# it = MyShinyIterator(start=2)
# for el in it:
#     print(el)
# print("второй проход")
# for el in it:
#     print(el)
# print("третий проход")
# for el in it:
#     print(el)

# gen = simple_gen(5, 7)
# for x in gen:
#     print(x)
# for x in gen:
#     print(x)
# for x in gen:
#     print(x)
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())


class SquareAll:
    def __init__(self, numbers):
        self.numbers = iter(numbers)

    def __next__(self):
        return next(self.numbers) ** 2

    def __iter__(self):
        return self


numbers = [1, 2, 3, 4, 5]


def square_all(numbers):
    for n in numbers:
        yield n**2


square_all_ex = (n**2 for n in numbers)
print(9 in square_all_ex)
print([x for x in square_all_ex])
print(9 in square_all_ex)


# как мы экономим память
# lots_of_fours = repeat(4, times=100_000_000)
# print(type(lots_of_fours))
# print(f"lots_of_fours занимает в памяти {sys.getsizeof(lots_of_fours)} байт")

# lots_of_fours_via_list = [4] * 100_000_000
# print(f"lots_of_fours занимает в памяти {sys.getsizeof(lots_of_fours_via_list)} байт")

# бесконечно длинный итератор
# for n in count():
#     print(n)
#     sleep(1)
