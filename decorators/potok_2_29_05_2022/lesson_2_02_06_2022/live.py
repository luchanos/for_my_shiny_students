# def my_print(s: str, a: int, b: int, n: int = 1, *args, **kwargs) -> str:
#     print(s * n)
#     print(args)
#     print(kwargs)
#     return s
#
#
# my_print("ABC", n=10, a=5, b=3, k=100)

GLOBAL_VARIABLE = 0
QUERY = """SELECT * FROM my_table"""


# def my_print():
#     global GLOBAL_VARIABLE
#     c = 1
#     print("Execute my function")
#     GLOBAL_VARIABLE += 1
#     # print(GLOBAL_VARIABLE)


# my_print()
# my_print()
# my_print()
# my_print()
# my_print()
# my_print()
# my_print()
# my_print()

# print(GLOBAL_VARIABLE)

# def func_outer():
#     c = 1
#     j = 1
#
#     def inner():
#         j = 1
#         c = 555
#
#         def inner_2():
#             j = 1
#
#             def inner_3():
#                 nonlocal c
#                 b = 2
#                 # print(GLOBAL_VARIABLE)
#                 # print(c)
#                 c = 123
#                 print(c, id(c))
#             j = 1
#             inner_3()
#         j = 1
#         inner_2()
#         print(c, id(c))
#     j = 1
#     inner()
#     print(c, id(c))
#
#
# func_outer()

def my_func():
    print("Моя функция my_func")
    return 1


def wrapper(f, *args, **kwargs):
    print("Моя функция wrapper")
    print("В качестве аргумента передана функция:", f)
    return f(*args, **kwargs)


# c = my_func
# c()

# wrapper(f=my_func)
# wrapper(f=print)
# wrapper(sum, [1, 2, 3, 4])

def wrapper_second(f):

    def inner(*args, **kwargs):
        print("Моя функция wrapper")
        print("В качестве аргумента передана функция:", f)
        return f(*args, **kwargs)

    return inner


res_1 = wrapper_second(print)
res_2 = wrapper_second(my_func)
res_3 = wrapper_second(sum)
print(res_1)
print(res_2)
print(res_3)
print(res_1())
print(res_2())
print(res_3([1, 2, 3, 4, 5]))
