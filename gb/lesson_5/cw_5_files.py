from io import TextIOWrapper

l = ["Первая строка\n", "Первая строка\n", "Первая строка\n"]

# try:
#     some_io_wrapper = open("sample.pdf", "rb")
#     raise ValueError
#     some_io_wrapper.write(l[0])
# except Exception:
#     some_io_wrapper.close()
# some_io_wrapper.close()
#
# x = [open("testfile.txt", "w") for _ in range(102300)]
#
# while True:
#     with open("testfile.txt", "w") as f_o:
#
# while True:
#     open("testfile.txt", "w")







# with open("testfile.txt", "w") as file_obj:
#     # путь можно указывать как абсолютный, так и относительно указателя, на который смотрит наш интерпретатор.
#     file_obj.write("Первая строка\n")
#     file_obj.write("Вторая строка\n")
#     file_obj.write("Третья строка\n")
#     file_obj.write("Четвертая строка\n")

# with open("testfile.txt", "r") as file_obj:
#     # тут упадём с ошибкой
#     file_obj.write("Первая строка\n")



# some_io_wrapper = open("sample.pdf", "rb")
# print(type(some_io_wrapper))
# with some_io_wrapper:
#     some_io_wrapper.write("Первая строка\n")
#     some_io_wrapper.write("Вторая строка\n")
#     some_io_wrapper.write("Третья строка\n")
#     some_io_wrapper.write("Четвертая строка\n")
# print(some_io_wrapper.closed)

# f_o = open("testfile.txt", "r")
# print(f_o.tell())
# print(f_o.read(3))
# print(f_o.tell())
# for x in f_o:
#     print(x, f_o.tell())
from logging import getLogger

logger = getLogger(__name__)
logger.info("Программа запущена")
logger.debug("Программа работает уже х секунд")
logger.warning("Опасное количество запросов")
logger.error("произошла страшная ошибка!")

# try:
#     1 / 0
# except Exception as err:
#     msg = "произошла страшная ошибка!"
#     db_pool.fetch(msg)
#     logger.error(msg)



# f_o = open("testfile.txt", "r")
# f_o_b = open("sample.pdf", "rb")
# content = f_o.read()
# content_f_o_b = f_o_b.read()
# print(f_o.tell())
# f_o.seek(0)
# print(f_o.tell())
# content = f_o.readline()
# print(content, end='')
# content = f_o.readline()
# print(content)
# content = f_o.readline()
# print(content)
# for x in f_o:
#     print(x)
# f_o.close()





import json
#
# # получаем данные из json
# tw = open("t.txt", "w")
with open("json_example./Users/nnsviridov/PycharmProjects/for_my_shiny_students/potok_7/lesson_5/json_example.json", "r") as json_obj:
    data = json.load(json_obj)
    print(data)
    # some_data = {"user_id": 123123,
    # "position": "devloper",
    # "city": "Moscow",
    #              "inner_dict": {"user_id": 123123,
    # "position": "devloper",
    #              "city": "Moscow"}}
    # s = json.dumps(some_data)
    # print(s)
