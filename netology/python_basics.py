# # int
# # float
# # bool  # True False
# # str
# # set, tuple, list, dict
#
# a = 1.34
# b = 10
# c = 111
# # type(a)
# # type("test text")
# # d = a + b + c
# # print(d)
# b_1 = True
# b_2 = False
# # print(type(b_1))
#
# # print(bool(0))
#
# g = 'a'
# f = 'test string'  # нумерация эл-в идет с нулевого!
# # print(f[0], f[1], f[5], f[70])
#
# # t = (a, b, c, c, c)
# # l = [a, b, c]
# # l[0] = 555
# # print(t)
# # print(l)
# # s = {a, a, a, c, c}
# # print(s)
#
# # l = [1, 2, 2, 2, 3, 3]
# # s_buf = set(l)
# # res_l = list(s_buf)
# # print(res_l)
#
# l = ["1991", "Nikolai", "Sviridov", "Backend Dev"]
# name = l[0]
# sur = l[1]
# born = l[2]
# pos = l[3]
#
# # d = {} # это пустой словарь! не множество!
# # s = set() # а вот это пустое множество
# # []  # list() пустой список
# # tuple()  # пустой кортеж
#
# d = {
#     "surname": "Sviridov",
#     "name": "Nikolai",
#     "born": 1991,
#     "position": "Backend Dev"
# }
#
# l_1 = [
#     {
#         "surname": "Sviridov",
#         "name": "Nikolai",
#         "born": 1991,
#         "position": "Backend Dev"
#     },
#     {
#         "surname": "Ivanov",
#         "name": "Ivan",
#         "born": 1992,
#         "position": "Frontend Dev"
#     }
# ]
#
# print(l_1[0]["name"])

# import sys

# a = sys.argv
# print(a)
# res = int(sys.argv[1]) + int(sys.argv[2]) + int(sys.argv[3])
# print("Результат", res)


# a = input("Хочешь пирожок? ")
# restart = "да"
#
# while restart == "да":
#     if a == "да":
#         nachinka = input("С какой начинкой? ")
#         num = input("Сколько? ")
#         num = int(num)
#
#         if nachinka == "вишня":
#             print("Держи пирожок с вишней")
#         elif nachinka == "творог":
#             print("Держи пирожок с творогом")
#         elif nachinka == "грибы":
#             print("Держи пирожок с грибами")
#         else:
#             print("Прости, такой начинки у нас нет")
#     else:
#         print("Ну как хочешь")
#
#     restart = input("Желаешь повторить все с начала? ")
#
# print("Программа завершена")

# cnt = 0
# l = [1, 2, 3, 4, 5, 6]
# while cnt != len(l):
#     print(l[cnt])
#     cnt = cnt + 1
#
# for el in l:
#     print(el)


a = input("Хочешь пирожок? ")
restart = "да"

while restart == "да":
    try:

        if a == "да":
            nachinka = input("С какой начинкой? ")
            num = input("Сколько? ")
            num = int(num)
            nach_dict = {
                "грибы": "грибами",
                "вишня": "вишней",
                "творог": "творогом"
            }

            msg = "Держи пирожок с " + nach_dict[nachinka]

            while num != 0:
                print(msg)
                num = num - 1

        else:
            print("Ну как хочешь")

        restart = input("Желаешь повторить все с начала? ")

    except ValueError:
        print("Произошла ошибка! Вы ввели что-то не то! Скорее всего не число!")
    except KeyError:
        print("Произошла ошибка! Вы ввели что-то не то! Скорее всего нет такой начинки!")


print("Программа завершена")