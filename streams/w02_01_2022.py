# l = []  # list
# s = set()
# d = {}  # dict
# t = tuple()
#
# l_1 = [1, 2, 3, 4, 5]
# t_1 = ('a', 'b', 'c', 'd', 'c')
#
# print(l_1[0], t_1[0])
# l_1[0] = 11
# print(l_1[0], t_1[0])
# t_1[0] = 'aa'

# t_2 = (([1, 2], 2, 3), ['a', 'b', 'c'])
# print(t_2)
# t_2[0][0][0] = 11
# print(t_2)

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [a, b]
# print(c)
# a[1] = 222
# print(a)
# print(c)

# c[1][0] = 444
# print(c)
# print(b)

# s = set()
# print(s)

# s = {1, 2, 3, 4, 5}
# print(s)
# s = {[1, 2, 3], 2, 3}

# l = [1, 1, 2, 1, 3, 4, 4, 4, 4]
# print(list(set(l)))

# d = {
#     'name': 'Nikolai',
#     'surname': 'Sviridov'
# }

s = "abdsfsdfbseweveverv"

# d = {"a": 1,
#      "s": 10}

# d = {}

# for sym in s:
#     if sym not in d:
#         d[sym] = 1
#     else:
#         d[sym] += 1

# print(d)


def my_func(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    print(a, b)
    return a + b


a_dict = {
    "a": 1,
    "b": 2
}

my_func(**a_dict)
