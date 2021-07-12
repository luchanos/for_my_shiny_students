# кастомные итераторы
from datetime import datetime

"""ДЗ сделать метод тумбочки таким, чтобы он мог работать принимая на вход как единичное значение, так и коллекцию:
множество, список или кортеж и выполнять то же самое действиве - добавление всех элементов в content.

Пример:
content = []

хочу добавить [1, 2, 3, 4, 5, 6] - все, что в списке сразу

Результат добавления:
content = [1, 2, 3, 4, 5, 6], а не [[1, 2, 3, 4, 5, 6], ]
"""


class Tumbochka:
    def __init__(self):
        self.created_dt = datetime.now()
        self.content = []  # изначально тумбочка будет создаваться всегда пустая

    def add_into(self, subject):
        # print("Отправляю метрику")
        self.content.append(subject)

    def __str__(self):
        return f"{self.content}"

    def some_info(self):
        return 'abc'

    def __iter__(self):  # итератор - это то, что вернет этот метод. генератор - частный случай итератора.
        for el in self.content:
            yield el



# l = [1, 2, 3, 4]
#
# for el in l:
#     print(el)
#
# list_it = iter(l)
# print(list_it)
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))
# print(next(list_it))


# tumbochka = Tumbochka()
# tumb_iter = iter(tumbochka)
# print(tumb_iter)

# for el in tumbochka:
#     pass

# try:
#     tumb_iter = iter(tumbochka)
#     while True:
#         print(next(tumb_iter))
# except StopIteration:
#     pass

"""Как работает цикл for: он вызывает метод iter от объекта, который мы хотим проитерировать. Получает итератор, либо
падает с ошибкой, если наш объект не является итерируемым. Дальше происходит вызов функции next от нашего итератора
для получения очередных значений, до тех пор, пока не будет поймано исключение StopIteration."""

tumbochka = Tumbochka()
a = 1
b = 2
c = 3
d = "TEST"
total = [a, b, c, d]
tumbochka.add_into(a)
tumbochka.add_into(b)
tumbochka.add_into(c)
tumbochka.add_into(d)
tumbochka.add_into(total)
print(tumbochka.content)

for el in tumbochka:
    print(el)


# def func():
#     yield
#
#
# c = func()
# for el in c:
#     print(el)
