# l = [1, 2, 3, 4, 5, 6, 7]

# for el in l:
#     print(el)

# сначала цикл for получает итератор от коллекции (выдача обоймы)
# it = iter(l)

# дальше, цикл for сам начинает скармливать наш итератор во встроенную ф-ю next для получения
# очредного значения (стрельба из пистолета, где next - это пистолет, а итератор - обойма)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# как только цикл for ловит StopIteration, то он прекращает свою работу (обойма пуста)
from time import sleep


class SomeCollection:
    """Коллекция, которая принимает число и до какого-то другого числа возвращает значения по запросу"""
    def __init__(self, start_val, fin_val):
        self.start_val = start_val
        self.fin_val = fin_val

    def __iter__(self):
        return MyShinyIterator(self.start_val, self.fin_val)


class MyShinyIterator:
    def __init__(self, start_val, fin_val):
        self.start_val = start_val
        self.buf = start_val
        self.fin_val = fin_val

    def __next__(self):
        if self.start_val >= self.fin_val:
            raise StopIteration
        self.start_val += 1
        return self.start_val

    def to_start(self):
        self.start_val = self.buf

    def __iter__(self):
        return self


# next(None)

my_iterator = MyShinyIterator(0, 5)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for el in my_iterator:
#     print(el)

# аналог на while:
# try:
#     while True:
#         print(next(my_iterator))
# except StopIteration:
#     pass


# some_col_ex = SomeCollection(0, 5)
# for el in some_col_ex:
#     print(el)

# это функция-генератор! она возвращает ОБЪЕКТ-ГЕНЕРАТОР!!!! ОБЪЕКТ-ГЕНЕРАТОР - частный случай ИТЕРАТОРА
def my_shiny_func():
    print("до первого yield")
    sleep(.5)
    yield 1
    print("между 1 и 2")
    sleep(.5)
    yield 'sdfgsdfgsdfg'
    print("между 2 и 3")
    sleep(.5)
    yield True
    print("после 3")
    sleep(.5)


    # pass

# g_o = my_shiny_func()
# print(g_o)
# print("ONE")
# print(next(g_o))
# print("TWO")
# print(next(g_o))
# print("THREE")
# print(next(g_o))
# print("FOUR")
#
# # как только не осталось yield, то само собой возникнет ошибка StopIteration
# print(next(g_o))
# print("AFTER ALL")

# for el in g_o:
#     print(el)

import sys
from datetime import datetime as dt


def talon_babina(limit):
    cnt = 0
    while cnt <= limit:
        yield cnt
        cnt += 1

# start = dt.now()
# print(f"Start working at: {start}")
# раскладывание талонов по столу
# a = [x for x in range(100_000_000)]

# раотаем с бабиной талонов по запросу. выдаем значение, только когда клиент прищёл
# a = talon_babina(100_000_000)
# print(f"Finish at: {dt.now()}. Working time: {dt.now() - start}")
# print(f"Size of object: {sys.getsizeof(a)}")
# print(sys.getsizeof(a))


# a = talon_babina(10)
# print(3 in a)
# print(3 in a)

# ТАКАЯ СТРУКТУРА НАЗЫВАЕТСЯ ГЕНЕРАТОРОМ СПИСКОВ (list comprehension)!!! ЭТО НЕ ТО ЖЕ САМОЕ, ЧТО ГЕНЕРАТОР-ИТЕРАТОР!!!
# a = [x for x in range(100_000_000)]

# СЛОВАРИ ИТЕРИРИУЮТСЯ ПО КЛЮЧАМ ТОЛЬКО ЛИШЬ ПОТОМУ, ЧТО ТАКОЕ ПРАВИЛО РЕАЛИЗОВАНО В ТОМ ИТЕРАТОРЕ, КОТОРЫЙ ИЗ НЕГО
# ВОЗВРАЩАЕТСЯ :)
# for el in {"key": "value", "a": "b", "c": "d"}:
#     print(el)

# МЕНЕДЖЕР КОНТЕКСТА
# print(open('test.txt', 'w'))
# получим ошибку:
# [open('test.txt', 'w') for _ in range(10_500)]

# f = open('test.txt', 'w')
# f.write("test stroka")
# f.close()


class IWannaUseYouInContMan:
    def __enter__(self):
        print("вошел в метод enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("вошел в метод exit")


# f = IWannaUseYouInContMan()

with IWannaUseYouInContMan() as f:
    print("выполняю контекст, о, Владыка!")
    raise ValueError("КАКОЙ УЖАС!!! ОШИБКА!", 1, 2, 3)
    print("доделал контекст!")

print("завершено")
