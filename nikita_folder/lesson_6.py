from sys import getsizeof

# l = [0, 1, 2, 3, 4, 5, 6]
# l1 = []
# for el in range(10_000_000):
#     l1.append(el)
#
# print(getsizeof(l1))
# print(getsizeof(range(10_000_000)))


def my_range(start, finish):
    print("какая-то логика 0")
    yield 1
    print("какая-то логика 1")
    yield 2
    print("какая-то логика 2")
    yield 3
    print("какая-то логика 3")
    yield 4
    print("какая-то логика 4")


def my_counter(start, finish):
    while start <= finish:
        yield start
        start += 1

# res = my_range(1, 20)
# c = my_counter(0, 10)
# for el in c:
#     print(el)
# print(5 in c)
# print(list(c))

# print(res)

# for el in res:
#     print(el)
#     print("ЧЕБУРЕК")

# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


l = (chr(el) for el in range(100) if el % 2 == 0)
print(list(l))


