# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# n = int(input("Enter number with 3 digits: "))
# if n == 0:
#     print(0, 0)
# else:
#     summ = 0
#     mult = 1
#     while n != 0:
#         k = n % 10
#         summ += k
#         mult *= k
#         n = n // 10
#     print(summ, mult)

# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
from typing import overload


def to_bin(n):
    final = 0
    razr = 0
    while True:
        d = n // 2
        os = n % 2
        if d == 0 and os == 0:
            break
        n = d
        final = final + 10 ** razr * os
        razr += 1
    return final


def bitovoe_and(n1, n2):
    bin_n1 = to_bin(n1)
    bin_n2 = to_bin(n2)
    res = 0
    razr = 0

    while bin_n1 != 0 or bin_n2 != 0:
        a = bin_n1 % 10
        b = bin_n2 % 10
        res += 10 ** razr * int(a == b == 1)
        bin_n1 = bin_n1 // 10
        bin_n2 = bin_n2 // 10
        razr += 1

    return res


def bitovoe_or(n1, n2):
    bin_n1 = to_bin(n1)
    bin_n2 = to_bin(n2)
    res = 0
    razr = 0

    while bin_n1 != 0 or bin_n2 != 0:
        a = bin_n1 % 10
        b = bin_n2 % 10
        res += 10 ** razr * int(a == 1 or b == 1)
        bin_n1 = bin_n1 // 10
        bin_n2 = bin_n2 // 10
        razr += 1

    return res


def sdvig_vpravo(n, n_znak):
    n = to_bin(n)
    while n_znak > 0:
        n = n // 10
        n_znak -= 1
    return n


def sdvig_vlevo(n, n_znak):
    n = to_bin(n)
    while n_znak > 0:
        n = n * 10
        n_znak -= 1
    return n

# По введенным пользователем координатам двух точек вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.

point_a = {"x": 1, "y": 2}
point_b = {"x": 2, "y": 2}


def make_line(point_a, point_b):
    return f"{point_b['x'] - point_a['x']}y = {point_a['y'] - point_b['y']}x + " \
           f"{point_b['x'] * point_a['y'] - point_a['x'] * point_b['y']}"

# Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ
# алфавита от 'a' до 'f' включительно.

from random import randint


def rand_sym(a, b):
    return chr(randint(ord(a), ord(b)))

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
def sym_counter(a, b):
    pos_a = ord(a)
    pos_b = ord(b)
    delta = 0 if pos_a == pos_b else abs(pos_a - pos_b) - 1
    return {"pos_a": pos_a,
            "pos_b": pos_b,
            "diap": delta}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def alphabet_searcher(sym):
    sym = sym.lower()
    for let in range(len(alphabet)):
        if alphabet[let] == sym:
            return let + 1


# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

def treangle_type_checker(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or a == c or b == c:
        return "равнобедренный"
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        return "прямоугольный"
    return "самый обыкновенный"


def treangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b > c or b + c > a or c + a > b:
        return True, treangle_type_checker(a, b, c)
    return False


# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
def check_middle(a, b, c):
    if a > b > c or c > b > a:
        return b
    elif a > c > b or b > c > a:
        return c
    elif c > a > b or b > a > c:
        return a


# Определить, является ли год, который ввел пользователем, високосным или не високосным.
def check_visokos(year):
    if year % 4 == 0:
        return False
    if year % 100 != 0:
        return True
    else:
        if year % 400 == 0:
            return True
    return False
