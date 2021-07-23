from abc import abstractmethod, ABC


class Furniture(ABC):
    def __init__(self, field):
        self.field = field

    @abstractmethod
    def open_door(self):
        pass

    def some_method(self, a, b, c):
        print("кокой-то результат")


class Tumb(Furniture):
    def open_door(self):
        print("дверца открыта")

# c = Furniture()
d = Tumb(123)
# d.open_door()
d.some_method(1, 2, 3)
