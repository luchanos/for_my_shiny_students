from io import BufferedReader, TextIOWrapper


# class SimpleClass:
#     def __enter__(self):
#         print("зашли в энтер")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("зашли в экзит")


# simple_class = SimpleClass()
#
# with simple_class:
#     print("работаем!")
#     raise Exception("ОШИБКА ОШИБОК!!!")
#
# print("закончили совсем работать")




# f_o = open("testfile.txt", "r")
# f_o.seek(12)
# print(f_o.tell())
# f_o.readline()
# print(f_o.tell())
























def test_func():
    file_object = open("testfile.txt", "w")
    file_object.write("dsfgsfgsd")
    raise Exception


def second_func():
    try:
        test_func()
    except Exception as err:
        c = 1
        print("error")


# second_func()
# file_object_2 = open("testfile.txt", "w")
# print(file_object_2.tell())
# file_object_2.write('sdasf')
# x = [open("testfile.txt", "w") for _ in range(102300)]








# a = 1
# b = 2
#
# BufferedReader









class SomeClassWithContext:
    def __enter__(self):
        print("Этот метод запускается, когда мы передаём объект в менеджер контекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Этот метод запускается, когда мы заканчиваем работу с объектом в менеджере контекста")
        if exc_type:
            print("Случиласть ошибка!!!")

    def some_meth(self):
        pass

# c = 1
# some_obj = SomeClassWithContext()
# with some_obj:
#     print("какая-то логика")
#     some_obj.some_meth()
#     raise ValueError("Ошибка!!!", 1, 2, [123123412341234, 232345345])
#     c = 1
# c = 1





# file_object = open("testfile.txt", "w")
# with file_object:
#     pass

# with SomeClassWithContext():
#     print("контекст")
#     print("контекст")
#     print("контекст")
#     print("контекст")
#     raise Exception("Error message", 'asfdsf', 'asdasdf', 'asdadsf')
#     print("контекст")
#     print("контекст")
#     print("контекст")







# some_io_wrapper = open("testfile.txt", "w")
#
# # Делаем объект, с которым можно работать в менеджере контекста
# some_context_object = SomeClassWithContext()
# with some_context_object, some_io_wrapper:
#     some_io_wrapper.write("Первая строка\n")
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     print('выполнение контекста')
#     # raise ValueError("Древнее зло вырвалось на свободу!!!")
# print("ЗАВЕРШЕНО")

# ЗАДАЧА МЕтОДОВ enter и exit - автоматизировать процессы работы с какими-то объектами и защитить нас
# от ситуаций, где мы можем что-то недосмотреть.


# Пример с плитой
# class AutomaticPlita():
#     def __enter__(self):
#         print("Плита автоматически включилась")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Плита автоматически выключилась")


# time_to_cook = 5
# autimatic_plite = AutomaticPlita()
# with autimatic_plite:
#     current_time = 0
#     while current_time <= time_to_cook:
#         user_status = input(f"Прошло времени: {current_time}. Вы там случайно не уснули? y/n? : ")
#         if user_status.lower() == "y":
#             raise Exception("ПОЛЬЗОВАТЕЛЬ ПЛИТЫ ЗАСНУЛ!!!")
#         current_time += 1
#     print("пельмешки готовы")
