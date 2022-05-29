# a = 1
# b = [1, 2, 3]
# e = Exception
# print(a, b, e)


c = 1


def greeting():
    a = input("Введите имя: ")
    print("Hello,", a)


def mul_0(a, b):
    return a * b


def capitalize_name(s: str):
    return s.capitalize()


def capitalize_name_bad():
    s = input("Введите имя: ")
    print(s.capitalize())
    return


# print((lambda a, b: a * b)(1, 2))
# print(mul(1, 2))

# print(lambda x: x, greeting)

# mul_0(1, b=2)

# s = input("Введите имя: ")
# print(capitalize_name(s))

# print(print())
# f_1 = print
# f_1(f_1("ABC"))

def func(a, b, c=0, d=0, e=0, f=0, g=0, *args, **kwargs):
    return sum([a, b, c, d, e, f, g])


print(func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, a=100))









