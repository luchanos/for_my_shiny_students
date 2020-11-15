# with open("testfile.txt", "w") as file_obj:
#     # путь можно указывать как абсолютный, так и относительно указателя, на который смотрит наш интерпретатор.
#     file_obj.write("Первая строка\n")
#     file_obj.write("Вторая строка\n")
#     file_obj.write("Третья строка\n")
#     file_obj.write("Четвертая строка\n")
#
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



# f_o = open("testfile.txt", "r")
# content = f_o.read()
# print(type(content))
# f_o.seek(0)
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

# получаем данные из json
with open("json_example.json", "w") as json_obj:
    # data = json.load(json_obj)
    # print(data)

    some_data = {"user_id": 123123,
    "position": "devloper"}
    json.dump(some_data, json_obj)
