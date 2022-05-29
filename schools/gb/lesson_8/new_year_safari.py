from abc import ABC, abstractmethod

to_be_cleaned = []

from random import randrange, choice


class Animal(ABC):
    max_health: int
    cnt: int
    approved_food_types: []

    def __init__(self, age: int, gender: str, weight: float):
        self.age = age
        self.gender = gender
        self.weight = weight
        self.is_alive = True
        self.current_health = self.__class__.max_health

    def eat(self, food):
        if food.__class__ in self.approved_food_types:
            print("Я съел", food)
            food.is_alive = False
            self.current_health = self.current_health + food.give_energy \
                if self.current_health + food.give_energy <= self.max_health else self.max_health
        else:
            print("Я не могу это есть")

    def make_damage(self, other):
        other.current_health -= self.damage_power

    @abstractmethod
    def voice(self):
        pass

    @property
    def damage_power(self):
        return self.weight / 10

    def create_new_animal(self, other):
        if self.gender != other.gender:
            return self.__class__(0, choice(['male', 'female']), randrange(100, 200) / 100)


class Food(ABC):
    @abstractmethod
    def give_energy(self):
        pass


class Bush(Food):
    cnt = 0

    def __init__(self, color, height, density):
        self.color = color
        self.height = height
        self.density = density
        self.is_alive = True

    @property
    def give_energy(self):
        return self.height * self.density * 0.2


class Zebra(Animal, Food):
    max_health = 100
    cnt = 0
    approved_food_types = [Bush]

    def voice(self):
        return "Igogo!!!"

    @property
    def give_energy(self):
        return self.weight * 0.5


class Tiger(Animal):
    max_health = 200
    cnt = 0
    approved_food_types = [Zebra]

    def voice(self):
        return "Wrawrrr!!!"


tiger_1 = Tiger(12, 'male', 500)
tiger_2 = Tiger(12, 'female', 400)
zebra_1 = Zebra(12, 'male', 501)
zebra_2 = Zebra(12, 'female', 501)

new_zebra = zebra_1.create_new_animal(zebra_2)
c = 1
