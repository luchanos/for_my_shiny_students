"""ДЗ - всё что не успела за прошлые уроки (6 урок)

Разобраться с прокидыванием функций внутрь функций!!!!!

Разобраться в разнице между объявлением функции, вызовом функции, печати функции и печати резутата работы функции.

Разобраться в разнице между тем, что функция ДЕЛАЕТ и тем, что она ВОЗВРАЩАЕТ (что является результатом её работы).

УЧИТЬ ДЕЛЕНИЕ И ЕГО ВИДЫ! ЕЩЕ РАЗ ВСЕ ПОВТОРИТЬ!
БУДЕТ ЭКЗАМЕН ПО УСТНОМУ СЧЕТУ!

УЧИТЬ ДЕЛЕНИЕ И ЕГО ВИДЫ! ЕЩЕ РАЗ ВСЕ ПОВТОРИТЬ!
БУДЕТ ЭКЗАМЕН ПО УСТНОМУ СЧЕТУ!

codewars прорешать несколько простых задач:
https://www.codewars.com/kata/5966e33c4e686b508700002d
https://www.codewars.com/kata/51c8991dee245d7ddf00000e
https://www.codewars.com/kata/57a083a57cb1f31db7000028

https://www.lucidchart.com/pages/ru/%D0%B1%D0%BB%D0%BE%D0%BA-%D1%81%D1%85%D0%B5%D0%BC%D0%B0 - прочитать про блок-схемы

Задачи из ДЗ начинать решать именно с них
"""

# снова о циклах:
# while дословно "до тех пор, пока выполняется какое-то условие" или же "до тех пор, пока то, что написано после while
# имеет значение True"
from time import sleep

# while True:  # бесконечный цикл
#     print('kek')
#     sleep(.5)

# способы выхода из цикла
# cnt = 0
# while True:
#     cnt += 1
#     print(cnt)
#     if cnt == 10:
#         break

# либо
# cnt = 0
# while cnt < 10:
#     cnt += 1
#     print(cnt)


# хочу выводить только четные числа
# while cnt < 10:
#     cnt += 1
#     if cnt % 2 == 0:
#         print(cnt)


# хочу выводить только четные числа v2
# while cnt < 10:
#     cnt += 1
#     if cnt % 2:
#         continue
#     print(cnt)


# Секрет успеха в решении задач:
# 1. Чтобы научиться решать задачи, нужно прежде всего РЕШАТЬ ЗАДАЧИ.
# 2. Решение задачи начинается с листочка и ручки или карандаша.
# 3. Необходимо проработать идею сначала на бумаге, разбить её на логические блоки.
# 4. Дальше можно начинать писать код.
# 5. Тестирование кода на тестовых кейсах.

# l = [0, 1, 2, 3, 4, 5]
# print(l[0])

# cnt = 0
# while cnt < len(l):
#     print(l[cnt])
#     cnt += 1

# cnt = 0
# while cnt < 10:
#     print(cnt)
#     cnt += 1

# l = [0, 1, 2, 3, 4, 5]

# ДОСЛОВНО: возьми итерируемый объект l, достань оттуда очередной элемент, который ты ещё не доставал, сохрани в
# переменную и проделай с ним то, что я тебе скажу
# for el in l:  # не путать с [el for el in l if el % 2 == 0]
#     if el % 2 == 0:
#         print(el)
#         print("Реклама")

# s = "hello world!"
# s1 = "The greatest victory is that which requires no battle"

# word_list = s.split()
# res = word_list[::-1]
# print(res)
# # st = {"asdad", "sfdasdfsdf"}
# res = " ".join(res)
# print(res)

# res = " ".join(s.split()[::-1])
# print(res)

# print(list(reversed(word_list)))

# s = "hello world!"
# s1 = "The greatest victory is that which requires no battle"


# def reverse_words(s):
#     return " ".join(s.split()[::-1])
#
#
# print(reverse_words(s))
# print(reverse_words(s1))

# "4",  "5" --> "9"
# "34", "5" --> "39"

# def sum_str(a, b):
#     if a != "":
#         a = int(a)
#     else:
#         a = 0
#     if b != "":
#         b = int(b)
#     else:
#         b = 0
#     return str(a + b)

# def sum_str(a, b):
#     return str(int(a) + int(b))


# print(sum_str("4", "5"))
# print(sum_str("4", ""))

# n = 0  ==> [1]           # [2^0]
# n = 1  ==> [1, 2]        # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]     # [2^0, 2^1, 2^2]
# n = 3  ==> [1, 2, 4, 8]  # [2^0, 2^1, 2^2, 2^3]

# def powers_of_two(n):
#     return [2 ** res for res in range(n + 1)]


# print(powers_of_two(0))
# print(powers_of_two(1))
# print(powers_of_two(2))
# print(powers_of_two(3))
# print(powers_of_two(4))
# print(list(range(6)))
