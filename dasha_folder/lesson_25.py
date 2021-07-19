from datetime import datetime
from time import sleep

"""
https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7

"""


class MyShinyIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.current = -1

    def __iter__(self):
        return self

    def to_start(self):
        self.current = -1

    def to_value(self, value):
        if value > len(self.my_list) - 1:
            raise ValueError("Слишком большой индекс!!!")
        self.current = value

    def __next__(self):
        if len(self.my_list) - 1 == self.current:
            raise StopIteration
        self.current += 1
        return self.my_list[self.current]


class Tumbochka:
    def __init__(self):
        self.created_dt = datetime.now()
        self.__content = []  # изначально тумбочка будет создаваться всегда пустая

    def add_into(self, *args):
        print("Отправляю смс владельцу тумбочки")
        self.__content.extend(args)

    def get_content(self):
        return self.__content

    def clear_content(self):
        self.__content.clear()

    def __str__(self):
        return f"{self.__content}"

    def __iter__(self):  # итератор - это то, что вернет этот метод. генератор - частный случай итератора.
        # for el in self.content:
        #     yield el

        # return iter(self.__content)

        return MyShinyIterator(self.__content)



# tumbochka = Tumbochka()
# tumbochka.add_into(1, 2, 3, 4, 5)
# for el in tumbochka:
#     print(el)

# my_shiny_iterator = MyShinyIterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# my_shiny_iterator.to_start()
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# print(next(my_shiny_iterator))
# my_shiny_iterator.to_value(9)
# print(next(my_shiny_iterator))


# for el in my_shiny_iterator:
#     print(el)


def over_the_road(address, n):
    l1 = [el for el in range(1, n * 2) if el % 2]
    l2 = [el for el in range(1, n * 2 + 1) if el % 2 == 0][::-1]
    if address % 2:
        pos = l1.index(address)
        res = l2[pos]
    else:
        pos = l2.index(address)
        res = l1[pos]
    return res


print(over_the_road(23633656673, 310027696726))
