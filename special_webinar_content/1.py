from functools import partial

# a = 1
# b = True
# c = 'sdsadfas'
#
# t = (a, b, c)
# l = [a, b, c]
# s = {a, b, c}
# d = {a: b, b: c}
#
# l1 = [6, 7, 8]
# l = [l1, l1]

# print(l)
# l1[0] = 'test_string'
# print(l)
# l[0][0] = 'test_string'
# print(l)
# print(l1)

from copy import deepcopy

# l1 = l3 = [6, 7, 8]
# t = (l1, l1)
# t1 = deepcopy(t)
#
# print(id(t), id(t1))
# t[0] = 1
# t[0][0] = 'test_string'
# print(t)
# l1[0] = 'test_string'
# print(t)

# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}


# l = [1, 2, 3, 4, 100, 6, 7, 8, 9, 0]
# l.sort()
# print(l)
# print(sorted(l))
# print(l)

# s = "test_string"
# print(s.title())
# print(s)

# s1 = "123"
# s2 = "456"
# s3 = "789"
# s4 = s1 + s2 + s3 + " " + "."
# s4 = f"{s1}{s2}{s3} ."
# s4 = "%d%s%s ." % (s1, s2, s3)
# s4 = "{1}{2}{0} .".format(s1, s2, s3)

# todo добить и показать
# cnt = 0
# for el in s:
#     prev = el
#     print(el)
#     cnt += 1

# d = {"name": "Nikolai",
#      "position": "developer / tech lead",
#      "company": "Domclick"}
#
# l = ["Nikolai", "developer / tech lead", "Domclick"]

# if answer == "left":
#     print("lose horse")
# elif answer == "right":
#     print("lose mind")
# else:
#     print("lose life")


def lose_horse(name):
    print(f"{name} lose horse")

# Пожалуйста, не пишите так:
# lose_horse = lambda name: print(f"{name} lose horse")


def lose_mind(name):
    print(f"{name} lose mind")

# Пожалуйста, не пишите так:
# lose_mind = lambda name: print(f"{name} lose mind")


def lose_life(name):
    print(f"{name} lose life")

# Пожалуйста, не пишите так:
# lose_life = lambda name: print(f"{name} lose life")

answers = ["left", "right", "straight"]
name = "Ivan"

# story_stone = {"left": partial(lose_horse, name),
#                "right": partial(lose_mind, name),
#                "straight": partial(lose_life, name)}
#
# for answer in answers:
#     story_stone[answer]()


class MyShinyPartial:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.func(*self.args, **self.kwargs)

# Использовали кастомный лкасс partial
# story_stone = {"left": MyShinyPartial(lose_horse, name=name),
#                "right": MyShinyPartial(lose_mind, name),
#                "straight": MyShinyPartial(lose_life, name)}
#
# for answer in answers:
#     story_stone[answer]()

SOME_CONST = 123


def outer():
    a = 5

    def some_func(c, g, *args, **kwargs):

        def inner_func():
            nonlocal a
            a += 1
            print(f"a равно {a}")

        inner_func()
        print("РАБОТАЮ!")
        global SOME_CONST
        print(SOME_CONST)
        SOME_CONST += 1
        print(a)

    some_func(1, 2, 3, b=4, e=6)


outer()
# print(SOME_CONST)
