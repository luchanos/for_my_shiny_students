# простая функция прямой y = 3x + 1

# y = 3 * 2 + 1
# y = y / 2
# print(y)
# y = 3 * 4 + 1
# y = y / 2
# print(y)
# y = 3 * 6 + 1
# y = y / 2
# print(y)

VAL = 1


def y(k, x, c, *args, **kwargs):
    """
    Эта функция нужна для
     обучения студентов на примерах)))
    """
    marker = False

    def mock(a, b):
        nonlocal marker
        marker = True

    print(VAL)
    return (k * x + c) / 2


l = [1, 2, 4, 5]

y(*l)
g = 1


# d = 2
# a, b, c, d, e, f, g, h, i, j = tup

# d = {'1': 3, '2': 3, '3': 4, '4': 5, '5': 6, '6': 7, '7': 3, '8': 100}
# # print((lambda k, x, c, *args, **kwargs: (k * x + c) / 2)(1, *l, **d))
#
# new_func = lambda k, x, c, *args, **kwargs: (k * x + c) / 2
# print(new_func)
# print(new_func(1, *l, **d))
# print(new_func(1, *l, **d))

# c = y(1, *l, **d)
# print(c)















# def sum_two(arg2, arg3, arg4):
#     flag = False
#
#     def another_func():
#         nonlocal flag
#         flag = True
#
#
#
#     return arg2 + arg3 + arg4
#
#
# print(list(range(3, 100, 3)))
# # print(sum_two(1, 2, 3))
#
#
# def recursion_ex():
#     recursion_ex()
#
# recursion_ex()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def user_info(name, surname, age, gender, address='Russia', **kwargs):
#     """
#     Функция для получения информации о пользователе
#     """
#     cookies = kwargs.get('cookies')
#     # todo luchanos не забыть рассказать об этом ребятам
#     if cookies:
#         print(cookies)
#     c = 1
#     print(f"Hello, {name} {surname} {age} y.o. and u r {gender}. I'm from {address}")
#
#
# l = [1, 2, 4, 10]
# a, b, c, d = l
# # print(a, b, c, d)
#
# user = {
#     'age': 29,
#     'name': 'Nikolai',
#     'surname': 'Sviridov',
#     'gender': 'male',
#     'address': 'Spain'
# }
#
# # print(user['age'])
#
# def breakfast():
#     print('завтракать')
#
# def dinner():
#     print('обед')
#
# def supper():
#     print('ужин')
#
#
# slovar = {
#     'morning': breakfast,
#     'afternoon': dinner,
#     'evening': supper
# }
#
# # slovar[input('введите время дня ')]()
#
# # if vs == 'morning':
# #     breakfast()
# # elif vs == 'afternoon':
# #     dinner()
# # elif vs == 'evening':
# #     supper()
# # else:
# #     raise ValueError("неправильно задано время дня")
#
# # print(d(**user))
#
# def sort_key(t):
#     return t[1]
#
# c = lambda arg1, arg2, arg3, arg4: arg1 + arg2 + arg3 + arg4
# # print(c(1, 2, 3, 4))
#
# # d = sort_key
#
#
# def func(another_func):
#     print("Hello")
#     another_func()
# #
# # func(another_func=breakfast)
#


# def second_el(t):
#     return t[-1]


# l = [(1, 2), (6, -100), (4, 0), (5, 500)]
# print(sorted(l, key=lambda t: t[-1]))
#
# for x in range(1, 10, 3):
#     print(x)






# l.sort(key=sort_key)
# l.sort(key=lambda t: t[1])
# print(l)




#
#
#
# # def ext_func():
# #     my_var = 0
# #     def int_func():
# #         # nonlocal my_var
# #         my_var += 1
# #         return my_var
# #     return int_func

