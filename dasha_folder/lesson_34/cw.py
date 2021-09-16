"""ДЗ linked list (связанный список), классический массив, хэшмап, бинарный поиск, графики сложности алгоритмов (знать
какой предпочтительнее), логарифмы и их графики.

Знать сложности извлечения элементов из списка и словаря"""

# 3 (8)
# хэш-функция - она пересчитывает входное значение в хэш


def hash_func(s):
    return s[-2:]


# print(hash_func("Петров"))
# print(hash_func("Иванов"))

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = [1, 'a', 1, -100, 3, True, ValueError, Exception]
# n = len(l)
# print(10 in l)
# O(n) - перебор
# log2_10

# 2 ^ 10 = 1024 -> log_2_1024 = 10
# 2 ^ 9 = 512 -> log_2_512 = 9
# 2 ^ 8 = 256 -> log_2_256 = 8
# 2 ^ 7 = 128 -> log_2_128 = 7
# 2 ^ 6 = 64 -> log_2_64 = 6
# 2 ^ 5 = 32 -> log_2_32 = 5
# 2 ^ 4 = 16 -> log_2_16 = 4
# 2 ^ 3 = 8 -> log_2_8 = 3
# 2 ^ 2 = 4 -> log_2_4 = 2
# 2 ^ 1 = 2 -> log_2_2 = 1
# 2 ^ 0 = 1 -> log_2_1 = 0

d = {
    'a': 1,
    'b': 2,
    'c': 3
}