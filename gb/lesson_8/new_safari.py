from abc import ABC, abstractmethod
from random import choice, randrange


class LifeObject(ABC):
    def __del__(self):
        c = 1
        print(f"УДАЛЯЮ ХИЩНИКА КЛАССА {self.__class__}")
        self.__class__.cnt -= 1


class Animal(LifeObject):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def voice(self):
        pass


class PlantEater(Animal):
    pass


class Predator(Animal):
    def eat_somebody(self, other):
        print(f"Я {self} только что скушал кото-то: {other}")
        # del other


class Lion(Predator):
    cnt = 0

    def __init__(self, color, height, weight, sex):
        self.color = color
        self.height = height
        self.weight = weight
        if sex.lower() not in {"male", "female", "m", "f"}:
            raise ValueError("Wrong sex setting!!!")
        self.sex = sex.lower()
        Lion.cnt += 1

    def voice(self):
        print("RAAAAAAAWR")

    def move(self):
        print("Лев резво погнал вперед")

    def create_new_lions(self):
        if self.sex in {"f", "female"}:
            count_new_lions = randrange(1, 7)
            for i in range(count_new_lions):
                print("Новый лев родился!")
                yield Lion(color=choice(["red", "black", "orange"]),
                           height=randrange(10, 15),
                           weight=randrange(4),
                           sex=choice(["male", "female"]))
        else:
            raise ValueError("Мужчина не может рожать, вы делаете что-то не то")


lion = Lion("red", 144, 150, "female")
new_lions = lion.create_new_lions()
lions_list = [lion for lion in new_lions]
c = 1