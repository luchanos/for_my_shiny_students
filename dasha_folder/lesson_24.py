# кастомные итераторы
# модификаторы доступа
from datetime import datetime


class Tumbochka:
    def __init__(self):
        self.created_dt = datetime.now()
        self.__content = []  # изначально тумбочка будет создаваться всегда пустая

    def add_into(self, *args):
        print("Отправляю смс владельцу тумбочки")
        self.__content.extend(args)
        c = 1

    def get_content(self):
        return self.__content

    def clear_content(self):
        self.__content.clear()

    def __str__(self):
        return f"{self.__content}"

    def __iter__(self):  # итератор - это то, что вернет этот метод. генератор - частный случай итератора.
        # for el in self.content:
        #     yield el
        return iter(self.__content)


l1 = (1, 2, 3)
l0 = ('a', 'b', 'c')
a = 1
b = 2

tumbochka = Tumbochka()
# tumbochka.content.extend([l1, l0, a, b])
# tumbochka.content = tumbochka.content + [l1, l0, a, b]
# print(tumbochka.content)
# tumbochka.add_into(l1, l0, a, b)
# print(tumbochka.content)

# итерируем тумбочку
# for el in tumbochka:
#     print(el)

# итерируем список
# for el in tumbochka.content:
#     print(el)

# new_list = [[1, 2, 3], {'a', 'b', 'c'}, tumbochka]
# for col in new_list:
#     for el in col:
#         print(el)

# print(tumbochka.__content)
# tumbochka.__content.reverse()
# print(tumbochka.__content)

# print(tumbochka.get_content())
# tumbochka.clear_content()
# print(tumbochka.get_content())


class MiniTumbochka(Tumbochka):
    def __init__(self):
        super().__init__()
        self.__content = []  # изначально тумбочка будет создаваться всегда пустая

    def show_mini_content(self):
        return self.__content


mini = MiniTumbochka()
mini.add_into(1, 2, 3)
# print(mini.get_content())
# print(mini.show_mini_content())
print(mini._MiniTumbochka__content)
print(mini._Tumbochka__content)
