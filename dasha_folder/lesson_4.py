"""ДЗ Глава 5
можно читать не очень внимательно: 190-195

ВЫУЧИТЬ НАИЗУСТЬ ТАБЛИЦУ ПРИОРИТЕТОВ ОПЕРАЦИЙ

ВЫУЧИТЬ ТАБЛИЦУ ИСТИННОСТИ ЛОГИЧЕСКИХ ОПЕРАЦИЙ
https://www.math.spbu.ru/user/nlebedin/bit_operat_2017.pdf - годная методичка

Термины которые изучим потом:
- списковое включение
- включение множеств
- включение словарей

ЗАДАЧИ:
Принимаем на вход строку произвольного текста. Нужно заменить каждый третий символ на *.
"""

# s = {1, 2, 3}
# s1 = {3, 4}
# print(s ^ s1)
#
# s2 = {1, 2, 3, (1, 2)}

# 0101 - это число 5
# 1001  - это число 9 в 10ной с.с.
# 1101 - это число 13

# False or True = True
# print(False or True)
# print(False and True and True and True and True and True and True and True and True)
# print(150 or 0)
# print(150 and 0)
# print(bool(150))

# для перевода в другие с.с.
# print(bin(5))
# print(oct(5))
# print(hex(5))

# five = oct(5)
# print(five, 'asfasdf', 'asdgafgwrgbwr', 123)
# print(int(five, 2))
# print(int(five, 16))
# print(int(five, 8))

# y = 100 * x + 10 * z


# def y_calculation(x, z):
#     print(100 * x + 10 * z)

# print(len)
# print(y_calculation)

# y_calculation(10, 20)

# print("5avsafvsf" or 9)
# print(0 or 9)
# print(5 | 9)


# t = 'test'
# print(t.upper())
# print(t)
# t = t + ' some string'
# print(t[0])
# # t[0] = 'sdfvsdfvsdfv'
# print(t.replace('t', '1'))
# print(t)
#
# ls = [0, 'test', 1, 7.5, 2, 'stertbetbr', 3, len, 4, print, 5, 6, 7]
# empty_list = []  # пустой лист

data_string = 'abcevwrvrrvrtvvrtgbryhbvsdhv'
# print(data_string[61])

cnt = 0
result = ''

# num = 1239741745632458984598237341
# print(num % 10)
# print(num // 10)

# while cnt < len(data_string):
#     if cnt % 2 == 0:
#         result += "*"
#     else:
#         result += data_string[cnt]
#     cnt += 1
# print(result)
# print(result)

while cnt < len(data_string):
    if cnt % 2 == 1:
        result += "*"
    else:
        result += data_string[cnt]
    cnt += 1
print(result)
