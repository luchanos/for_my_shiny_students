# def my_func(a, b, n=123, *args, **kwargs):
#     print(a, b, n)
#     print(args)
#     print(kwargs)


# my_func(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, k=100, n=888)

# SOME_CONST = 0
# a = 100
# b = 200


# def my_func(a, b, *args, **kwargs):
#     global SOME_CONST
#     print(SOME_CONST)
#     # print(a, b)
#     SOME_CONST += 1
#     print(SOME_CONST)


# my_func(1, 2)
# print(SOME_CONST)

# def my_func():
#     print("Это функция my_func")
#     return 123


# def my_another_func(func):
#     print("Это функция my_another_func")
#     print(func)
#     print("Результат работы переданной функции", func())


# f = my_func
# print(f)

# my_another_func(my_func)

# def my_func():
#     a = 1000
#
#     def my_another_func():
#
#         def inner():
#             nonlocal a
#             a += 1
#             print(a)
#             print("Это функция my_another_func")
#
#         inner()
#
#     my_another_func()
#     print("Это функция my_func")
#     print(a)
#
#     return my_another_func


# my_func()
# res = my_func()
# print(res)


def summarizer(a, b):
    print(f"Суммирую {a} и {b}")
    return a + b


def my_shiny_func():
    print("Ура!")


def deco(f):
    def inner(*args, **kwargs):
        print("Покупайте наших котят")
        return f(*args, **kwargs)

    return inner


# res_deco = deco(summarizer)
# print(res_deco)
# print(res_deco(1, 8))

# res_deco_2 = deco(my_shiny_func)
# print(res_deco_2)
# print(res_deco_2())

# my_shiny_func = deco(my_shiny_func)


@deco
def m_test_func():
    print("Это тестовая функция")


print(m_test_func)
