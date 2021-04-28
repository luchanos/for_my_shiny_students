# a = 1
# print(type(a))

# 1.1
# True

# print(True in [1, 2, 3, 4])
# print(False in [1, 1, 2])
# print(1 in [True, 2, 3, 4])

# l = [1, 2, 3, ValueError, "test_str", "asd"]

#  начало : конец : шаг
# print(l[1:4])
# print(l[::-1])

# l = [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[::2])
#
# print(id(l))
# l.sort()
# print(id(l))
# print(l)

# s = "test_string"
# print(id(s))
# s = s + "1111" + "123123" + "dfgsdfgsdfg" + "dsfgsdfg"

# a = "1111"
# b = "123123"
# c = "dfgsdfgsdfg"
# d = "dsfgsdfg"
# res = f"Результат: {s}{a}{b}{c}{d}"
# res = "Результат: {4}{3}{1}{2}{0}".format(s, a, b, c, d)
# print(id(s))
# print(res)

# res = 123
# st = "stroka"
# template = "Результат: %d"
# print(template % st)

# l = [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[5])
# l[5] = "test"
# print(l)


# t = (100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# t[5] = "test"

# a = 1
# b = a
# print(id(a), id(b))
# l = [a, 1, 2, 3, 4]
# a = 0
# print(l, b)


# a = ['a', 'b', 'c', 'd']
# print(id(a))
# l = [a, 1, 2, 3, 4]
# # a = 0
# # print(id(l[0]))
# a[0] = "чебурек"
# print(l)


# a = ['a', 'b', 'c', 'd']
# print(id(a))
# # работает в том числе и с кортежами
# l = (a, 1, 2, 3, 4)
# # a[0] = "чебурек"
# l[0][3] = 500
# print(l)
# print(a)

# st = set()
# st = {1, 2, 3, 4, (5, ((([]))))}
# print(st)
# l = [1, 2, 2, 2, 2, 3, 3, 1, 1]
# print(list(set(l)))

# d = dict() or {}
# print(type({}))
# ["Николай", "Свиридов", "Developer", 29]

# d = {"name": "Николай",
#      "surname": "Свиридов",
#      "position": "Developer",
#      "age": 29}
#
# print(d["name"])
# d["name"] = "Пётр"
# print(d)
# d["address"] = "Tenerife"
# print(d)

# answer = input("Будешь ли ты кушать? ")
# if answer == "да":
#     print("Бабушка предлагает выбрать начинку")
#     answer = input("Какую хочешь? ")
#     if answer == "грибы":
#         print("Кушаю пирожок с грибами")
#     elif answer == "повидло":
#         print("Кушаю пирожок с повидлом")
#     elif answer == "мясо":
#         print("Кушаю пирожок с мясом")
#     elif answer == "яйца":
#         print("Кушаю пирожок с яйцами")
#     else:
#         print("Такой начинки нет")


# обработка ошибок
# f = open('1.txt', 'w')
# res = []
# try:
#     line = int(input("Введите число: "))
#     s = "Число %d" % line
#     f.write(s)
# except (ValueError, KeyError) as err:
#     print(f'Это не число. Выходим. {err}')
# except ZeroDivisionError as err:
#     print('Это что ещё такое?')
# else:
#     print('Всё хорошо.')
# finally:
#     f.close()
#     print('Я закрыл файл.')
# Именно в таком порядке:
# try, группа except,
# затем else, и только потом finally.

# d = {}
# try:
#     d['name']
#     1 / 0
# except ZeroDivisionError as err:
#     print(f"Ошибка {err}")


from time import sleep

condition = True
break_condition = False
continue_condition = False
cnt = 0

# while condition:  # какое-то условие
#     sleep(.5)
#     print("Это")
#     print("Блок")
#     print("Кода")
#     print("В цикле")
#     if break_condition:
#         print("Выходим из цикла")
#         break
#     cnt += 1
#     # if cnt == 10:
#     #     break_condition = True
#     # if cnt > 6:
#     #     continue_condition = True
#     # if continue_condition:
#     #     print("Сразу идем на новую итерацию")
#     #     continue
#     # print("И кое-что в конце!")
# else:
#     print("Если вышли из цикла штатно")


# condition = True
# cnt = 0
# while condition:
#     cnt += 1
#     if cnt % 2 == 0:
#         print(f'{cnt} ухожу на след итерацию')
#         continue  # означает бросить всё и уйти на следующую итерацию цикла
#     print(f'message {cnt}')
#     # if cnt == 3:
#     #     condition = False
#     if cnt == 5:
#         break  # внештатный выход из цикла
# else:  # штука, которая будет запускаться ТОЛЬКО в том случае, если вышли из цикла благодаря под-while-овому условию.
#     print("Пришли в else")
# print("Закончили")

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l)

# шаг 1 - получить итератор от объекта который нужно проитерировать
# шаг 2 - запускать функцию next от этого итератора
# i = iter(l)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for el in l:
#     print(el)
#     break
# else:
#     print("Вышли штатно")

# l = [str(x) * 3 for x in range(100) if x % 2 == 0]
# print(l)
# d = {k: str(v) * 3 for k, v in enumerate(range(10))}
# print(d)

# def bogatyr_choice(direction="left"):
#     if direction == "left":
#         return "Horse loss!"
#     elif direction == "right":
#         return "Mind loss!"
#     elif direction == "straight":
#         return "Life loss!"


# print(bogatyr_choice())

# def some_f(a, l=[]):
#     # if not l:
#     #     l = []
#     l.append(a)
#     return l

# def summarize(*args, **kwargs):
#     return sum(args)

def get_key(t):
    return t[1]


# l = [(1, 0), (4, 5), (-100, -1000000)]
# rst = summarize
# lambda a, b: a + b
# print(sorted(l, key=lambda t: t[1]))




# [1, [...], [...]] - вот что будет при выводе
# print(some_f(some_f(some_f(1))))
# print(some_f(1))
# print(some_f(1))
# print(some_f(1))


def outer(a):
    def other_func(f):
        print("Рекламное сообщение")
        f(a)
    return other_func


@outer
def my_shiny_func(a):
    print(f"Я функция my_shiny_func с параметром {a}")


# res = outer(2)(my_shiny_func)
# my_shiny_func(2)


def param_wrapper(*args, **kwargs):




    def outer(f):
        def inner(*fargs, **fkwargs):
            print("Рекламное сообщение")
            f(*fargs, **fkwargs)
        return inner




    return outer


@param_wrapper(1, 2, 3)
def my_shiny_func(a):
    print(f"Я функция my_shiny_func с параметром {a}")

my_shiny_func('тест')
