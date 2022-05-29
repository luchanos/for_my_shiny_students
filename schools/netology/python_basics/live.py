# a = 1  # int - целое число
# b = 1.5  # float - число с плавающей точкой
# c = True  # bool - логический тип
# n = None  # none объект или "ничто"
#
# l = [0, 1, 2, 3, "string", True]  # list - список
# s = {"a", "b", "c"}  # set - множество
# t = (123, 456, 789)  # tuple - кортеж
# d = {
#     "name": "Nikolai",
#     "surname": "Sviridov"
# }  # dict - словарь
# st = "Nikolai"  # str - строка

# print(st[::-1])

# print(d)
# print(d["name"])
# print(d["surname"])
# print(d.get("fasdasdv"))
# d["fasdasdv"] = 123
# print(d)
# print(d.get("fasdasdv"))



# print(s)
# s.pop()
# print(s)
# s = {(1, 2, 3), 1, 2}
# print(s)

# print(l)
# l.append(123123123123)
# print(l[1])
# l[1] = 123
# print(l)

# print(t)
# print(t[1])
# t[1] = 123
# print(t)

# print(121321231231)
# print(a, b, c, l, s, t, d)

# арифметические операции
# a = 1000
# a_1 = a * 100
# print(a_1, type(a_1))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(a + b)

# a = 12345
# print(a // 10)  # целочисленное
# print(a % 10)  # остаток
# print(a / 10)  # классическое

# st = "123"
# st_2 = "456"
# # print(st + st_2 + st + st)  # конкатенация
# # s_res = f"Результат нашей программы: {st}, {st_2}, {d}, а ещё и {a}."
# # print(s_res)
# res = str(int(st) + st_2)
# # print(res, type(res))
# print(float(1))

# a = 1
# b = 1
# c = 1
# d = 2
# print(a == b and c == d)

# answer_3 = "Да"
# while True:
#     answer = input("Хочешь пирожок? ")
#     if answer == "Да":
#         answer_2 = input("С какой начинкой? (вишня/малина) ")
#         nach = None
#         if answer_2 == "вишня":
#             nach = "вишня"
#         elif answer_2 == "малина":
#             nach = "малина"
#         else:
#             print("Такой начинки нет! Будешь есть пустой!")
#         print(f"Держи пирожок с начинкой: {nach}!")
#     else:
#         print("Ну как хочешь!")
#     answer_3 = input("Хочешь повторить ввод? ")
#     if answer_3 != "Да":
#         break
# print("Программа завершена")

import sys

print(sys.argv)

a = float(sys.argv[1])
b = float(sys.argv[2])
try:
    print(a / b)
except (KeyError, ZeroDivisionError):
    print("Ошибка!")
print("Программа завершена")
