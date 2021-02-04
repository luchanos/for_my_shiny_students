# c = "test strTnG"
# print(id(c))
# print(id(c.capitalize()))
# print(c.title())
# print(c)

# l = [1, 2, 3, [ValueError, TypeError, True], "asas"]
# print(id(l))
# l[0] = "TEST"
# print(id(l))

# print(sorted(l))
# l.sort()
# print(l)

# s = {1, 2, 0, -1, 4}
# s1 = {1, 2, 0, TypeError}
# print(sorted(s))
# print(s.intersection(s1))

# t = (1, 2, 3, -1, 0, 1, 1, 1, 1, 1)
# print(sorted(t))
# print(set(t))
from functools import partial

user_data = {'name': 'Nikita', 'surname': 'Belikoff', 'second_name': 'Vladimirovich'}

user_act = {'плохое': partial(print, "Иду домой"),
            'хорошее': partial(print, "Иду к Косорукову"),
            'нормальное': partial(print, "Иду к Карпухину")
            }

user_act['не пойму'] = 'Иду в столовую'
print(user_act)

# answer = 'нормальное'
# user_act[answer]()

# if answer == 'плохое':
#     print("Иду домой")
# elif answer == 'хорошее':
#     print("Иду к Косорукову")
# elif answer == 'нормальное':
#     print("Иду к Карпухину")
