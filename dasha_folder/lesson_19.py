"""
Класс - это чертеж, по которому мы будем изготавливать экземпляры этого чертежа. Например есть чертеж автомобиля и мы
по нему можем наклепать сколько угодно автомобилей.

Поле класса - это характеристика, которая присуща чертежу, а также может быть доступна всем экземплярам, которые созданы
по этому самому чертежу.

ДЗ:
1. Что такое класс?
2. Что такое экземпляр?
3. Что такое поле класса?
4. Что такое поле экземпляра?
"""

# ООП держится на 3х классических постулатах: инкапсуляция, наследование, полиморфизм

# простой класс (чертеж)
# class SomeClass:
#     # поле класса (характеристика самого класса (чертежа))
#     class_field = "some class field value"
#
#     # поля экземпляров, они характерны для конкретного экземпляра, который был создан по чертежу
#     def __init__(self, sample_field_1, sample_field_2, sample_field_3):
#         self.sample_field_1 = sample_field_1
#         self.sample_field_2 = sample_field_2
#         self.sample_field_3 = sample_field_3


# # создаю 3 экземпляра
# ex_1 = SomeClass("sample_field_1_1", "sample_field_2_1", "sample_field_3_1")
# ex_2 = SomeClass("sample_field_1_1", "sample_field_2_2", "sample_field_3_3")
# ex_3 = SomeClass("sample_field_1_3", "sample_field_2_3", "sample_field_3_3")
#
# # к полю класса у меня есть доступ через любой из его экземпляров
# print(SomeClass.class_field)
# print(ex_1.class_field)
# # print(SomeClass.sample_field_1)


# class SomeChildClass(SomeClass):
#     class_filed_2 = "some class field 2 value"
#
#     def __init__(self, sample_field_1, sample_field_2, sample_field_3, sample_field_4):
#         super().__init__(sample_field_1, sample_field_2, sample_field_3)
#         self.sample_field_4 = sample_field_4
#
#
# class SomeChildChildClass(SomeChildClass):
#     class_filed_2 = "some class field 2 new value"
#
#
# print(SomeChildClass.class_field)
# print(SomeChildClass.class_filed_2)
# print(SomeChildChildClass.class_filed_2)

# Задача 1: хочу всех разрабов подписать на контракт о том, что они должны будут обязательно реализовать
# определенные методы в своем классе, если хотят отнаследоваться от какого-то моего базового.

# Задача 2: я не хочу, чтобы мой базовый класс имел конкретную реализацию в виде экземпляров. То есть, я знаю, что
# такое автомобиль, как он должен выглядеть, как он должен себя вести и какими характеристиками обладать в целом,
# но я не могу создать экземпляр автомобиля в общем! То есть я должен знать конкретно, что он должен уметь делать
# по-существу.


from abc import ABC, abstractmethod

# абстрактный класс - это класс, который имеет хотя бы 1 абстрактный метод
# как узнать, является ли класс абстрактным?
# есть ли в нашем классе не переопределенные абстрактные методы, которые перетекают от какого-либо из родителей или
# которые прописаны в нём явно?
# Если да, то это абстрактный класс. Если нет, то он не абстрактный.


class AbstractWeapon(ABC):
    @abstractmethod
    def shoot(self):
        pass


class AbstractTransport(ABC):
    """Абстрактный базовый класс транспорта"""
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def beep(self):
        pass


class MilitaryTransport(AbstractWeapon, AbstractTransport):
    pass


class WeaponTransport(MilitaryTransport):
    def __init__(self, color):
        self.color = color

    def shoot(self):
        print("Транспорт-оружие стреляет")

    def move(self):
        print("Транспорт-оружие двигается")

    def beep(self):
        print("Транспорт-оружие сигналит")


class Car(AbstractTransport):
    """Класс-прослойка. Тоже является абстрактным"""
    def __init__(self, color, power):
        self.color = color
        self.power = power


class Horse(AbstractTransport):
    """Класс-прослойка. Тоже является абстрактным"""
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age


class WorkHorse(Horse):
    def move(self):
        print("Лошадь поехала")

    def beep(self):
        print("Лошадь ржёт")

    def work(self):
        print("Лошадь работает")


class WorkCar(Car):
    def move(self):
        print("Рабочая машина поехала")

    def beep(self):
        print("Рабочая машина сигналит")

    def work(self):
        print("Рабочая машина работает")


class SportCar(Car):
    # переопределение метода родителя
    def move(self):
        print("Спортивная машина поехала")

    # переопределение метода родителя
    def beep(self):
        print("Спортивная машина сигналит")

    def ride(self):
        print("Спортивная машина участвует в заезде")


class Pistol(AbstractWeapon):
    def shoot(self):
        print("Пистолет стреляет")


# work_car = WorkCar(color='red', power=120)
# work_car.move()
# work_car.beep()

class A:
    def a_method(self):
        print("метод a")

    def d_method(self):
        print("метод d из класса A")


class B:
    def b_method(self) -> None:
        print("метод b")

    def d_method(self):
        print("метод d из класса B")


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
c.a_method()
c.b_method()
c.d_method()

d = D()
d.a_method()
d.b_method()
d.d_method()

# MRO - method resolution order (порядок разрешения методов)

# Инкапсуляция - механизм связывания данных с методами и классами, которые с этими данными работают, а также способы
# сокрытия деталей реализации всего этого хозяйства.
