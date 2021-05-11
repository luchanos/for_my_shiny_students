"""Домашнее задание:

Рассказать про методы списков: index, pop, reverse, sort, append, insert.
Рассказать про методы строк: join, capitalize, title

Задача:
0. Для ВСЕХ нижеследующих задач нарисовать блок-схему!!!
1. Хотим получить список чисел от 0 до 1_000_000, но в конечном списке должно быть только каждое третье число из
этого диапазона.
2. Запрашиваем у пользователя числа, разделенных пробелом и записываем их в список, предварительно переведя каждое из
них в целочисленный тип. Пример пользовательского ввода: 1 2 3 100 -99.
Дальше нужно собрать из списка строку, в которой бы содержались только чётные числа из этого списка в порядке по
возрастанию и разделенные тем сообщением, которое введет пользователь.
3. Написать бинарный поиск для отсортированного листа.
4. Запрашиваем у пользователя произвольные строки до тех пор, пока он не введет СТОП. Строки складываем в файл с учетом
того, что каждую новую введенную пользователем строку нужно переносить. При этом перед открытием файла спрашивать у
пользователя, хочет ли он дозаписывать существующую инфу в файле или зачищать.
"""
from io import TextIOWrapper

# spisok = [1, -100, 10000, 0, 9, 1]
# res_position = []
# cnt = 0
#
# num = int(input("Введите число: "))

# Что бы я сделала? Проверила и записала бы (с) Даша
# for el in spisok:
#     if num == el:
#         res_position.append(cnt)
#     cnt += 1
#
# print(res_position)


# cnt = 0
# while cnt <= 10:
#     print(cnt)
#     cnt += 1


# range - функция для генерации последовательностей целых чисел
# print(list(range(10)))
# print(set(range(10)))
# print(tuple(range(10)))

# print(range(10))
# print(type(range(10)))

from datetime import datetime
import sys

# создать список из миллиона элементов:

res = []
cnt = 0

start_time = datetime.now()

# while cnt <= 10_000_000:
#     res.append(cnt)
#     cnt += 1
#
# print(sys.getsizeof(res))

# my_future_list = range(10_000_000)
# print(sys.getsizeof(res))
# print(datetime.now() - start_time)

# for el in my_future_list:
#     print(el)

# применимость range - генерация числовых последовательностей. Не нужно писать цикл и прочую обвязку.
# list(range(1_000_000))
# set(range(1_000_000))
# tuple(range(1_000_000))

# Снова про строки
# l = ['1', '2', '3', '4', '5', '6']

# Задача: собрать элементы списка в строку (если это возможно) с разделителем.
# pazdelitel = "  TEST  "
# print(pazdelitel.join(l))

# print("hello, world!".split())  # разделяет по разделителю (по умолчанию по пробелу)

# работа с файлами
# для того, чтобы начать работать с файлом, его надо открыть. При этом, если открываем на запись, а файла нет,
# то он будет создан автоматически

# Когда мы открываем файл, то надо указать не только его адрес, но и режим, в котором мы его открываем.
# dasha_first_file = open("dasha_first_file.txt", mode="a")  # w - запись, a - дозапись
# !!! режим w при открытии существующего файла полностью убьёт содержимое файла!
# print(dasha_first_file)

# давай запишем строчку
# test_string = "Какая-то строка\n"
# dasha_first_file.write(test_string)

# чтение из файла:
# dasha_first_file = open("dasha_first_file.txt", mode="r")
# one_string = dasha_first_file.read() # записывает весь файл в одну строчку
# print(one_string)

# lines = dasha_first_file.readlines()  # считает все в список, каждая строка будет на своем элементе списка
# print(lines)

# line = dasha_first_file.readline()  # прочитает очередну строчку из файла
# print(line, end='')
# line = dasha_first_file.readline()  # прочитает очередну строчку из файла
# print(line, end='')

# cnt = 0
# for line in dasha_first_file:
#     if cnt == 3:
#         print(line, end='')
#         break
#     cnt += 1
# print(sys.getsizeof(dasha_first_file))

# line = dasha_first_file.readline()  # прочитает очередну строчку из файла
# print(line)
# print(dasha_first_file.tell())  # tell говорит нам, где курсор сейчас в файле!
# важный момент! 1 символ латиницы = 1 байт, но 1 символ кириллицы - 2 байта

# можно задавать позицию курсора:
# dasha_first_file.seek(0)
# line = dasha_first_file.readline()
# print(line)

# еще один метод, который позволяет читать количество символов из файла!
# data = dasha_first_file.read(15)  # вычитает 15 симоволов из файла
# print(data)
# print(dasha_first_file.tell())  # вернули байт на котором находится указатель

# dasha_first_file.close()  # файл будет закрыт
# [open("dasha_first_file.txt", mode="r") for _ in range(100_000)]  # тут написано положи объект обертки вокруг
# файла в список сто тыщ раз
# dasha_first_file.write("blablabla")
