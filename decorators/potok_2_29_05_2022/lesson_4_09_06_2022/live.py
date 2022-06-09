def wrapper_first(f):
    print(f"Отрабатывает wrapper_first с принятой функцией {f}")

    def inner_from_first(*args, **kwargs):
        print(f"Отрабатывает inner для функции {f}")
        return f(*args, **kwargs)
    return inner_from_first


def wrapper_second(f):
    print(f"Отрабатывает wrapper_second с принятой функцией {f}")

    def inner_from_second(*args, **kwargs):
        print(f"Отрабатывает inner для функции {f}")
        return f(*args, **kwargs)
    return inner_from_second


# @wrapper_first
# @wrapper_second
# def my_func(a, b):
#     return a + b
#
#
# print("\n\nМеняем порядок\n\n")
#
#
# @wrapper_second
# @wrapper_first
# def my_func(a, b):
#     return a + b


# print(my_func)
# print(my_func(1, 2))


def retry_deco(attempts):
    def middle(f):
        def inner(*args, **kwargs):
            att = attempts
            while att != 0:
                try:
                    return f(*args, **kwargs)
                except Exception as err:
                    att -= 1
                    print(err, f"Attempts left {att}. Total attemts: {attempts}")
        return inner
    return middle


def advertisement(msg):
    def middle(f):
        def inner_from_second(*args, **kwargs):
            print(msg)
            return f(*args, **kwargs)
        return inner_from_second
    return middle


# @advertisement
# @retry_deco
# def func():
#     1 / 0

# @advertisement("Моя реклама")  # middle
# @retry_deco(10)
# @advertisement("Ещё одна моя реклама")  # middle
# def func():
#     1 / 0


# func()

from functools import wraps, partial


def deco(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f()
    return inner


@deco
def my_func():
    return 1


def my_func_2(a, b, c):
    print("Я запустилась!")
    return 1


# print(my_func)
# print(my_func_2)

# o = partial(my_func_2, a=0)
# print(o)
# o = partial(o, b=2)
# o = partial(o, c=2)
# print(o())

class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, f):
        def inner_from_second(*args, **kwargs):
            print("Реклама", self.a, self.b, self.c)
            return f(*args, **kwargs)
        return inner_from_second

    def __str__(self):
        return "Это мой класс!"


# @MyClass(1, 2, 30)
# def my_func_2(a, b, c):
#     print("Я запустилась!")
#     return 1


# my_func_2(1, 2, 3)
# print(MyClass(1, 2, 30))


def adv(cls):
    def inner_from_second(*args, **kwargs):
        print("Реклама")
        cls.mad_func = lambda self, x: x ** 2
        return cls(*args, **kwargs)
    return inner_from_second


@adv
class A:
    def __init__(self):
        c = 1

    def sample_1(self):
        print("Это sample 1")


ex = A()
print(ex.mad_func(2))
