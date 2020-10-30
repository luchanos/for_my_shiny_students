from abc import abstractmethod, ABC
from random import random


class Food(ABC):
    pass


class Peenut(Food):
    give_energy = 1

    def __str__(self):
        return "орех"


class Meat(Food):
    give_energy = 3

    def __str__(self):
        return "мясо"


class AbstractAnimal(ABC):
    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def main_action(self):
        pass


class Animal(AbstractAnimal):
    max_energy: int
    spent_energy: int
    approved_food_type: [Food]

    def __init__(self):
        self.energy = self.max_energy

    def feed(self, food):
        if type(food) == self.approved_food_type:
            self.energy = self.energy + food.give_energy
        else:
            raise WrongTypeFoodError

    def _method_to_spent_energy(self):
        self.energy -= self.spent_energy


class WrongTypeFoodError(Exception):
    def __init__(self):
        self.txt = "Неверный тип еды для данного животного!"


class Tiger(Animal):
    total_tiger_cnt = 0
    max_energy = 100
    spent_energy = 30
    approved_food_type = Meat

    def __init__(self):
        super().__init__()
        Tiger.total_tiger_cnt += 1

    def voice(self):
        return "Wraaaarrrrrrr!!!"

    def main_action(self):
        print("is hunting")
        if random() > 0.5:
            self.energy = self.energy + (self.energy + 20) % self.max_energy
        else:
            self.energy -= 20

    def run(self):
        super()._method_to_spent_energy()


class Parrot(Animal):
    max_energy = 30
    spent_energy = 1
    total_parrot_cnt = 0
    approved_food_type = Peenut

    def __init__(self):
        super().__init__()
        Parrot.total_parrot_cnt += 1

    def voice(self):
        return "AAaaaaaAAA!!!"

    def main_action(self):
        print("is sleeping")
        self.energy += self.energy + (self.energy + 1) % self.max_energy

    def fly(self):
        super()._method_to_spent_energy()


# отличие метода type от isinstance
# c = Peenut()
# print(isinstance(c, Food))
# print(type(c) == Peenut)
# print(type(c) == Food)

peenut = Peenut()
meat = Meat()
tiger = Tiger()
parrot = Parrot()
tiger.run()
c = 1
tiger.feed(meat)
c = 1