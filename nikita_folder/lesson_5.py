# пример без функций с повторным кодом
# for x in range(10):
#     c = 1
#     print(c)
#     c += 1
#
# print("блок кода")
# c = 1
# print(c)
# c += 1
# print("блок кода")
# print("блок кода")
# c = 1
# print(c)
# c += 1

# прямая
# y = kx + b
# y = 2 * x + 3
SOME_CONST_VALUE = 100500
G = 10


# def outer_func():
#     n = 1
#
#     def line_func(x):
#         def inner_func():
#             global SOME_CONST_VALUE
#             SOME_CONST_VALUE += SOME_CONST_VALUE
#
#             nonlocal n
#             n *= 100
#
#         global G
#         G += 1
#         y = 2 * x + 3
#         inner_func()
#         return y
#
#     line_func(100)
#     print(f"n = {n}")


# def line_func_2(x):
#     print(SOME_CONST_VALUE)
#     y = 10 * x + 30
#     return y


# a = 100
# print(line_func(line_func(a)))
# outer_func()
# print(G)
# print(SOME_CONST_VALUE)

def a_func(a, b, c, d, e=0, *args, **kwargs):
    print(f"Я РАБОТАЮ C АРГУМЕНТАМИ a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")


a_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, l=5, u=7, r=100)
