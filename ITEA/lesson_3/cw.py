"""Doc strings
Meta-классы
Abstract Bases-классы
__new__
__init__
Context-managers
Использованием декораторов с классами
Контейнеры, созданные путем наследования (UserList, UserDict, UserString)
Контейнеры, созданные путем агрегации
Методы доступа к элементам контейнера
Iterators, Generators"""

#############################################################
######################## Doc strings ########################
#############################################################


#############################################################
################### Abstract Bases-классы ###################
#############################################################

# Абстрактный класс - класс у которого нельзя создать экземпляр и который содержит хотя бы 1 абстрактный метод.
# По сути абстрактный класс - это контракт, на который подписывается каждый разработчик, который желает
# наследоваться от данного класса. Нужны для того, чтобы было удобнее управлять наследованием - мы ОБЯЗЫВАЕМ
# разработчиков называть методы одинаково.
from abc import ABC, abstractmethod


class Figure(ABC):  # нужно обязательно наследоваться от ABC (Abstract Based Class)
    @abstractmethod  # декоратор абстрактного метода
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


# а теперь создадим 2 конкретных класса для наших фигур
class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def square(self):
        return self.height * self.width


class Treangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        """Площадь треугольника по формуле Герона"""
        p = 0.5 * self.perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# Если хотя бы 1 абстрактный метод родителя не будет реализован в наследнике конкретно, то при попытке создать
# экземпляр упадёт ошибка!


treangle = Treangle(1, 2, 3)


#############################################################
################ подробнее про метод __new__ ################
#############################################################
class SimpleClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __new__(cls, *args, **kwargs):  # cls - ссылка на класс!!!
        """Создаёт объект в памяти!
        В этом методе мы можем провалидировать имена прокидываемых переменных"""
        for arg in args + tuple(kwargs.values()):
            if not isinstance(arg, int):
                raise ValueError("Параметр - не целое число!")
        return super().__new__(cls)  # вызывает метод родительского класса object!

    @property  # позволяет работать с методом класса, как с полем
    def some_calculating_value(self):
        """Этот метод будет отображаться как поле класса, но значение будет подсчитывать только по запросу!"""
        return [(self.param_1 * self.param_2) ** 100 for _ in range(100_000_00)]


simple_class_ex = SimpleClass(1, param_2=2)  # если попробуем прокинуть не целое число, а к примеру строку - упадём

# ХОЗЯЙКЕ НА ЗАМЕТКУ: если мы в __new__ вернем не объект класса, а что-то другое, то __init__ не запустится вообще.
