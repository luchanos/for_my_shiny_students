"""Итераторы"""

# tumb = [1, 2, 3, 4]
# c = 1

# for el in tumb:
#     print(el)

# 1. проверить, является ли объект итерируемым: пытается получить итератор от перебираемого объекта!
# iterator_tumb = iter(tumb)  # получили перебиратель
# print(iterator_tumb)

# print(next(iterator_tumb))
# print(next(iterator_tumb))
# print(next(iterator_tumb))
# print(next(iterator_tumb))
# print(next(iterator_tumb))


# def simple_gen_func():
#     yield


# for el in simple_gen_func():
#     print(el)


# что на самом деле делает for под капотом:
# iterator_tumb = iter(tumb)
# while True:
#     try:
#         next_val = next(iterator_tumb)
#     except StopIteration as err:
#         break
#     print(next_val)


# Ситуация: нам нужно управлять процессом итерации нашего объекта

class IteratorForTumbochka:
    def __init__(self, col):
        self.col = col
        self.start_val = -1

    def to_start(self):
        self.start_val = 0

    def to_custom(self, some_val):
        self.start_val = some_val

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.start_val += 1
            break
        if self.start_val < len(self.col) and self.col[self.start_val] != "pencil":
            return self.col[self.start_val]
        raise StopIteration


class Tumbochka:
    def __init__(self, box: list):
        self.box = box

    def __iter__(self):  # создает и возвращает перебиратель нашей тумбочки!!! абсолютно произвольный, главное, чтобы был итератором!
        some_iterator = IteratorForTumbochka(self.box)
        return some_iterator


tumbochka = Tumbochka(["apple", "notebok", "pencil", "pen"])

it = iter(tumbochka)
print(it)


iterator_tumb = iter(tumbochka)
# while True:
#     try:
#         next_val = next(iterator_tumb)
#         if next_val == 5:
#             iterator_tumb.to_custom(1)
#     except StopIteration as err:
#         break
#     print(next_val)


iter_obj = IteratorForTumbochka([1, 2, 3, 4, 5])
for el in iter_obj:
    print(el)







# print(tumbochka.box)

# l = [[1, 2, 3, 4], {5, 6, 7, 8}, simple_gen_func(), tumbochka]
#
# for col in l:
#     for el in col:
#         print(el)
#     print("Collection has been iterated!")

# for el in tumbochka.box:
#     print(el)

# for el in tumbochka:
#     print(el)

# it = iter(tumbochka)
# print(it)
