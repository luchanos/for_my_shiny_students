# a = TypeError
# c = 1
# g = "sdfsdfd"
# h = [1, 2, 3, 4]
# print(a, c, g, h)

#### ОБЪЕКТ
# while True:
#     data = input("Введите данные: ")
#     data.title()
#     print(data)

def my_func(data: str) -> str:
    return data.upper()


# some_data = input("Введите данные: ")
# res = my_func(some_data)
# print(res)
# print(my_func)

# f_1 = my_func
# print(f_1, my_func)
# some_data = input("Введите данные: ")
# res = f_1(some_data)
# print(res)

# print(print("ABC"))
# print(print)

# def my_print(s: str) -> str:
#     print(s)
#     return s

# f_2 = print
# f_2(f_2("ABC"))
# f_2(f_2)


# my_print(my_print("ABC"))


def my_print(s: str, a: int, b: int, n: int = 1, *args, **kwargs) -> str:
    print(s * n)
    return s


my_print("ABC", 1, 2, 3, 4, 5, 6, 7, 8, 9, k=10, l=100)






