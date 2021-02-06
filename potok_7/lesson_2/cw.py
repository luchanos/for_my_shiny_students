"""ТИПЫ ДАННЫХ"""
from copy import deepcopy


tseloe = 1
with_point = 1.2
complex_num = complex(1, 2)  # зачем? для специфических задач, конечно же)
# вдруг вы захотите посчтитать вольт-амперную характеристику?)


"""ПОБИТОВЫЕ ОПЕРАЦИИ
https://www.math.spbu.ru/user/nlebedin/bit_operat_2017.pdf - годная методичка

ПРИМЕНЕНИЕ:
- проверка, сброс и установка отдельных битов в составе целого
числа
- экономия памяти (упаковка нескольких логических значений в
одну целую переменную)
- повышение производительности программ (битовые операции
могут выполняться одновременно над всеми разрядами в отличие
от арифметических операций, где нужно учитывать перенос)
- работа с регистрами аппаратуры

ИЛИ:
0101 - это число 5
1001  - это число 9 в 10ной с.с.
1101 - это число 13

True or False = True

"""
# print(5 | 9)
# a_d = int('1101', 2)
# print(a_d)
# print(13 >> 1)
# _______1101
# ______11010
# рекомендую прочитать книгу КОД

# print(bin(8))
# print(int(bin(8), 2))
# print(int(bin(8), 2))
# a = hex(14)
# b = oct(14)
# print(a, b)
# a_d = int('0100', 2)
# print(a_d)
# print(a_d)


# a = 9999999
# print("Number in dec: ", a)
# print("Number in bin: ", bin(a))
# print("Number in oct: ", oct(a))
# print("Number in hex: ", hex(a))
# print(int((hex(a)), 16))
# print(int((oct(a)), 8))

"""101"""
# СДВИГ
# a = 5
# a = a << 10
# print(a)
# a = a >> 1
# print(a)

"""
БАЙТЫ И BYTEARRAY.
ПЕРВЫЕ НЕИЗМЕНЯЕМЫЕ, ВТОРЫЕ - ДА
БОЛЬШЕ ИНФО - https://pythonworld.ru/tipy-dannyx-v-python/bajty-bytes-i-bytearray.html"""
# b = "Пример".encode("UTF-8")
# print(b)
# print(chr(123), chr(124), chr(125))  # берем символ из таблицы ASCII
# print(ord("{"), ord("|"), ord("}"))  # получаем порядок числа по таблице ASCII
# print("123"  "adfsadfa")
# """СТРОКИ - НЕИЗМЕНЯЕМЫЙ ТИП
# ПОЛНЫЙ СПИСОК МЕТОДОВ - https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html"""
# test_string = "приВет, Андрей! Ну обними меня скорей!"
# print("Make all letter in uppercase", test_string.upper(), test_string)
# print("Make all letter in lowercase", test_string.lower())
# print("Make first letter in uppercase", test_string.capitalize())
# print("Is digit:", test_string.isdigit())

# # ЧТО МОЖЕМ СДЕЛАТЬ:
# s = "first" + "second"
# print(s)
# print(s * 3)
# print(s[0], s[1], s[2], s[3], s[4])

"""СРЕЗЫ - ЭТО КРАЕУГОЛЬНЫЙ КАМЕНЬ ПИТОНА
Общая формула среза: [start:finish:step]"""
# s = '0123456789'
# print(s[1::2])
# print(s[::2])
# print(s[1:200000000000000:20])

# # БЫСТРЫЙ РЕВЕРС
# print(s[-1])
# print(s[::-1])
# print(list(reversed(s)))


# """ЦИКЛ FOR ДЛЯ ОБХОДА ПОСЛЕДОВАТЕЛЬНОСТЕЙ"""
# s = "SOME TEST STRING"
# for x in s[3:10:2].lower():
#     print(x)
# print(x * 10)
# print("Вы великолепны")

# аналог
# cnt = 0
# print(len(s))
# while cnt < len(s):
#     print(s[cnt])
#     cnt += 1
#
# РАЗБИЕНИЕ СТРОКИ НА ЭЛЕМЕНТЫ СПИСКА
# s = "some test string"
# l = s.split()
# print(l)

# print(list("listr"))
# s = "some, test - string"
# l = s.split(",")
# print(l)
#
# # ОБРАТНАЯ ОПЕРАЦИЯ
# l = ["aha", "ha", "haha"]
# print("".join(l))

# """
# КОЛЛЕКЦИИ.
# СПИСКИ - ИЗМЕНЯЕМЫЕ
# ПОЛНЫЙ СПИСОК МЕТОДОВ - https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html"""
l1 = [1, 2, 3, 4, 5]
l2 = [True, False]
l3 = ['t', 'e', 's', 't']
# print('t' in l3)
# print(True in l1)
# print(l3.count('t'))
# print('tes' in 'test')
# print(l1[2])

# l4 = [l1, l2, l3]
# print(l4)

# l4[1] = 'ANOTHER VAL'
# l2[1] = 'SOME VALUE'
# l4[1][0] = 'XXX'
# print(l4)
# print(l2)

# # ОБЪЕДИНЕНИЕ СПИСКОВ
# l5 = l1 + l2 + l3
# print(l5)
# print(l5.index(0))  # ВАЖНЫЙ МОМЕНТ: False/True и 0 - это одно и то же для index
# print(l2.index(3))
#
# # ДОБАВЛЕНИЕ В СПИСОК
# l2.insert(1, "SOME VALUE")  # ДОБАВЛЕНИЕ В ПОЗИЦИЮ
# print(l2)
# l2.append("ONE MORE ELEMENT")
# print(l2)
# # # ПОЛУЧИТЬ ЭЛЕМЕНТ ИЗ СПИСКА С ЕГО УДАЛЕНИЕМ ИЗ НЕГО
# elem = l2.pop(1)
# print(l2)
# print(elem, l2)
#
#
# """
# КОЛЛЕКЦИИ.
# КОРТЕЖИ - НЕИЗМЕНЯЕМЫЕ
# ПОДРОБНЕЕ - https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html"""
# a = 1
# b = 2
# a, b = b, a
# print(a, b)
#
# t = ([1, 2], 3, 4)
# t[0][0] = 'dfdsfgdfg'
# print(t)
#
# # ЗАЧЕМ??? ДЛЯ БЕЗОПАСНОСТИ.
#
# # ПЕРЕСТАВИТЬ ЭЛЕМЕНТЫ В ЛИСТЕ
# l = [1, 2, 3, 4]
# print(l.index(3), l.index(4))
# l[2], l[3] = l[3], l[2]
# print(l)
#
# """
# КОЛЛЕКЦИИ.
# МНОЖЕСТВА - ИЗМЕНЯЕМЫЕ
# МЕТОДЫ - https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html"""
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# a = {1, 2, 3, 4, 5, 5, 5, 5}
# b = {'s', 'd', 'e'}
# print(a.update(b))
# s = set()  # пустое множество! ТАК И ТОЛЬКО ТАК! {} - это пустой словарь!
# print(a)
# # ЗАЧЕМ? ЕСЛИ НУЖНО ДЕРЖАТЬ УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ И НЕ ВАЖЕН ПОРЯДОК
# # для неизменяемости нужно использовать frozenset
#
# # УНИКАЛИЗАТОР
# l = (1, 1, 1, 2, 2, 2)
# print(tuple(set(l)))  # на собеседовании в Яндекс не прокатит))
#
#
# """
# КОЛЛЕКЦИИ.
# СЛОВАРИ - ИЗМЕНЯЕМЫЕ
# МЕТОДЫ - https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html"""
# # ЗАЧЕМ??? ЭТО ОЧЕНЬ СИЛЬНЫЙ ИНСТРУМЕНТ ДЛЯ ХРАНЕНИЯ ИНФОРМАЦИИ, А ТАКЖЕ МОЖЕТ ИСПОЛЬЗОВАТЬСЯ В НЕКОТОРЫХ
# # СЛУЧАЯХ, КАК АЛЬТЕРНАТИВА УСЛОВНЫМ ОПЕРАТОРАМ
#
some_dict = {"name": "Nikolai",
             "surname": "Sviridov",
             "position": "developer"}


# print(some_dict["name"])
# print(len(some_dict))

# # БОГАТЫРСКИЙ КАМЕНЬ
# decision = input("Enter direction: ").lower()
# if decision == "left":
#     print("Lose horse")
# elif decision == "right":
#     print("Lose life")
# elif decision == "straight":
#     print("Lose mind")


# story_stone = {
#     "left": "Lose horse",
#     "right": "Lose life",
#     "straight": "Lose mind"
# }
# decision = input("Enter direction: ").lower()
# print(story_stone[decision])
# print(story_stone.get(decision))  # ВАЖНО ПОНИМАТЬ РАЗНИЦУ
# print(story_stone.keys())
# print(story_stone.values())
# print(story_stone.items())
#
# """NoneType"""
# c = None
# print(print(c, type(c)))
#
# """Exceptions - исключение. Нужны для обработки внештатных ситуаций"""
# try:
#     1 / 0
# except (TypeError, ZeroDivisionError) as err:
#     print("Error!!!", err)
#
#
# a = 1
# b = 2
# ТЕРНАРНЫЙ ОПЕРАТОР
# if a == 3:
#     result = 123
# else:
#     result = 5
#
#
# result = 123 if a == 3 else 5
# print(result)
#
# """
# 1. ВСЕ КОЛЛЕКЦИИ ЯВЛЯЮТСЯ ИТЕРИРУЕМЫМИ ОБЪЕКТАМИ. ТО ЕСТЬ МОЖНО ИХ ПЕРЕБИРАТЬ В ЦИКЛЕ for.
# 2. ВСЕ КОЛЛЕКЦИИ ИМЕЮТ ИНТЕРФЕЙС МЕТОДОВ len
# """
