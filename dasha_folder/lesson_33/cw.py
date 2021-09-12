"""
ДЗ
Уметь рассказать про хэшмап. Уметь рассказать про то, что такое коллизии и как с ними можно бороться
"""

# типы данных - изм, неизм +
# изм - множества, списки, словари
# неизм - строка, кортеж, числа, фикс множества
# sort / sorted +

# l = [100, 1, 2, 3, 4]
# list(sorted(l))
# l.sort()

# списки / кортежи ++-+-

# a = [1, 2, 3]
# l = [4, 5, a]
# a.append(10)
# print(l)
# l[2][0] = 0
# print(a)
# l[2] = 0
# print(a)

# a = [1, 2, 3]
# t = (4, 5, a)
# t[2][0] = 0
# print(t)

# l = [el for el in range(100) if el % 2 == 0]
# print(l)

# l = [1, 1, 2, 0, 1, 3]
# print(set(l))
# print(tuple(l))
# s = {l, l}  # тут будет ошибка
# print(s)

# a = {}
# print(type(a))


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return "abc"


# a = func(j=2, k=3)
# print(a)

# def func(a):
#     yield
#     yield
#     yield


# a = func(1)
# print(a)
# c = iter(a)
# print(c)
# for el in a:
#     print(el)

# class IteratorForDasha:
#     def __init__(self):
#         self.cnt = 0
#
#     def to_start(self):
#         self.cnt = 0
#
#     def __next__(self):
#         while self.cnt < 10:
#             self.cnt += 1
#             return 1
#         raise StopIteration
#
#     def __iter__(self):
#         return self


# class A:
#     def __iter__(self):
#         return IteratorForDasha()


# a = A()
# c = iter(a)
# for el in a:
#     print(el)

# class A:
#     def __enter__(self):
#         print('какая-то лолика до')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('какая-то лолика после')


# a = A()

# print(1)
# with a:
#     print(2)
#     print(2)
#     1 / 0
#     print(2)
#     print(2)
# print(3)
