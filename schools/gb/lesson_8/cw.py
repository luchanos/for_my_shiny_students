from abc import ABC, abstractmethod


class Animal(ABC):
    all_amimals = []

    def __init__(self):
        self.all_amimals.append(self)

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def voice(self):
        pass

    @property
    @abstractmethod
    def koef_massa(self):
        pass

    @staticmethod
    def summ_m_koef(kletka) -> int:
        res = 0
        for animal in kletka:
            res += animal.koef_massa
        return res


class Mammals(Animal):
    @abstractmethod
    def feed_children_by_milk(self):
        pass


class Birds(Animal):
    has_feather = True
    has_kluv = True

    @abstractmethod
    def make_egg(self):
        pass


class Eagle(Birds):
    def __init__(self, weight, length, name):
        self.weight = weight
        self.length = length
        self.name = name
        super().__init__()

    def voice(self):
        return "Chirik!!!"


    def run(self):
        print("Я лечу")

    def feed(self):
        pass

    def sleep(self):
        pass

    @property
    def koef_massa(self):
        return self.weight * self.length - 100

    def make_egg(self):
        return EagleEgg()

    @classmethod
    def some_class_method(cls):
        cls.test_value = 1234
        return cls


class EagleEgg:
    def produce_eagle(self):
        return Eagle(100, 150, "some_name")


class Tiger(Mammals):
    def __init__(self, weight, length, name):
        self.weight = weight
        self.length = length
        self.name = name
        super().__init__()

    def voice(self):
        return "Wraaaarrrrrrr!!!"

    def run(self):
        pass

    def feed_children_by_milk(self):
        print("Кормлю детей")

    def feed(self):
        pass

    def sleep(self):
        pass

    @property
    def koef_massa(self):
        return self.weight * self.length - 100


eagle = Eagle(1, 2, 3)
print(eagle.__dict__)
print(eagle.__slots__)
print(type(eagle.__class__))

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def feature(self):
        pass


class Dog(Animal):
    pass
