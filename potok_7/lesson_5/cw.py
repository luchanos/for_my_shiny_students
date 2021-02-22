from io import TextIOWrapper

# l = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
l = ["Первая строка", "Вторая строка", "Третья строка"]


f_o = open("my_shiny_file.txt", "w", encoding='UTF-8')
print("hhtyhthty", file=f_o)
# f_o = open("sample.pdf", "rb")
# print(f_o.read())

# [open("testfile.txt", "w") for _ in range(102300)]

# print(f_o)
# for el in l:
#     print(f_o.write(el))
# f_o.writelines(l)
# res = f_o.read()
# res = f_o.readlines()
# print(res)
# res = f_o.readline()

# print(f_o.tell())
# f_o.seek(6)
# print(f_o.tell())
# for el in f_o:
#     c = 1
#     print(el, end='')

# print(f_o.closed)
# f_o.close()
# print(f_o.closed)


# class MyPirozhok:
#     def __enter__(self):
#         print("начинаю работу с пирожком в менеджере контекста")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("заканчиваю работу с пирожком в менеджере контекста")
#
#
# pirozhok = MyPirozhok()
#
# print("начало работы")
# with pirozhok:
#     raise ZeroDivisionError
#     print("работаю")
#
# print("конец")


import json
#
# # получаем данные из json
with open("json_example.json", "r") as json_obj:
    data = json.load(json_obj)
    print(data)
    print(type(data))
    # some_data = {"user_id": 123123,
    #              "position": "devloper",
    #              "city": "Moscow",
    #              "l": [1, 2, 3, {"fd": 123}]
    #              }
    # s = json.dump(some_data, json_obj)
    # print(s)

import sys