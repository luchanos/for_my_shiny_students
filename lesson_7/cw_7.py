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
