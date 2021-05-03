"""Домашняя работа:

1. Написать декоратор, который подавляет определённый тип исключений. То есть пользователь передаёт
в декоратор список с типами исключений.

2. Написать декоратор, который подсчитывает время работы функции.

3. Написать декратор, который в зависимости от прокинутого аргумента либо логирует возникающие ошибки и не
прерывает выполнение программы, либо даёт ей упасть.
"""

# def outer(func):
#     def func_runner(a, b):
#         print("RUNNING PARAMETER!")
#         return func(a, b)
#     return func_runner


# @outer
# def my_func(a, b):
#     print(f"TEST MESSAGE WITH PARAMS {a, b}")
#     print("DONE")
#     return 100000000


# c = outer(my_func)
# print(c)
# print(c(1, 2))

# print(my_func)


# cnt = 0
# while cnt <= 10:
#     try:
#         divisor(1, 0)
#     except Exception as err:
#         print(err)
#         if cnt == 10:
#             raise
#     cnt += 1


def decorator_par(limit):
    c = 1
    def outer(func):
        c = 1
        def inner(*args, **kwargs):
            cnt = 0
            while cnt < limit:
                try:
                    func(*args, **kwargs)
                except Exception as err:
                    print(err)
                    if cnt == limit:
                        raise
                cnt += 1
        return inner
    return outer


def outer(func):
    c = 2
    def inner(*args, **kwargs):
        print("РЕКЛАМА!")
        return func(*args, **kwargs)
    return inner


@decorator_par(limit=10)
@decorator_par(limit=10)
@decorator_par(limit=10)
@outer
def divisor(a, b):
    return a / b

divisor(1, 0)
