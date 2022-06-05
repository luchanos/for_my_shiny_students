
# def deco(msg, *dargs, **dkwargs):
#     def wrapper_second(f):
#         def inner(*args, **kwargs):
#             print(msg, dargs, dkwargs)
#             print("Моя функция inner")
#             print("В качестве аргумента в исходный декоратор передана функция:", f)
#             print("Сейчас я буду запускаться с аргументами, которые переданы в inner:", args, kwargs)
#             print("########")
#             return f(*args, **kwargs)
#         return inner
#     return wrapper_second


# def wrapper_second(msg, f):
#     def inner(*args, **kwargs):
#         print(msg)
#         print("Моя функция inner")
#         print("В качестве аргумента в исходный декоратор передана функция:", f)
#         print("Сейчас я буду запускаться с аргументами, которые переданы в inner:", args, kwargs)
#         print("########")
#         return f(*args, **kwargs)
#     return inner


# @deco("Реклама", "ABC", a="test")
# def my_func():
#     print("Моя функция my_func")
#     return 1


# my_func()
# res = wrapper_second(msg="sdfsdfs", f=my_func)




# @deco("Реклама газировки")
# def my_func_2():
#     print("Моя функция my_func_2")
#     return 1


# print(my_func())
# print(my_func_2())


# res_1 = wrapper_second(print)
# res_2 = wrapper_second(my_func)
# res_3 = wrapper_second(sum)
# print(res_1)
# print(res_2)
# print(res_3)
# print(res_1())
# print(res_2())
# print(res_3(1, 2, 3, 4, 5))
# t = ([1, 2, 3, 4, 5], )
# print(type(t))

# my_func()


def wrapper_first(f):
    print(f"Отрабатывает wrapper_first с принятой функцией {f}")

    def inner(*args, **kwargs):
        print(f"Отрабатывает inner для функции {f}")
        return f(*args, **kwargs)
    return inner


def wrapper_second(f):
    print(f"Отрабатывает wrapper_second с принятой функцией {f}")

    def inner(*args, **kwargs):
        print(f"Отрабатывает inner для функции {f}")
        return f(*args, **kwargs)
    return inner


@wrapper_first
@wrapper_second
def my_func(a, b):
    return a + b


print(my_func)
print(my_func(1, 2))
