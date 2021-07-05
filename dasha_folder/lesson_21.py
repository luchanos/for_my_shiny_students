"""
- Запрашиваем у пользователя данные о юзерах: имена, фамилии, адреса, года рождения. Формируем словари и записываем их
в json-файл. То есть мы последовательно запрашиваем у пользака с экрана данные о других людях. Если мы хотим прекратить
ввод данных, то надо задать этот вопрос в соответствующем месте и обработать стоп-слово. С дозаписью разберись сама *.

установить json-viewer в Пайчарм и Хром

- Дополнить класс автомобиля так, чтобы его можно было использовать в менеджере контекста: при передаче в него объекта
автомобиль нужно включать зажигание, а при выходе - выключать.
"""
# JSON

import json

some_dict = {
    "user": "Dasha",
    "password": "qwerty"
}

some_dict_2 = {
    "user": "Nikolai",
    "password": "123456"
}

some_dict_3 = {
    "user": "Alexey",
    "password": "ytrewq"
}

# дамп одного пользователя
# with open("user_data.json", "w") as json_obj:
#     json.dump(obj=some_dict, fp=json_obj)  # дампаем нашу питоновскую структуру в json-файл

# дамп сразу всех пользователей
# users_list = (some_dict, some_dict_2, some_dict_3)
# with open("user_data.json", "w") as json_obj:
#     json.dump(obj=users_list, fp=json_obj)  # дампаем нашу питоновскую структуру в json-файл

# загрузка данных из json
# with open("user_data.json", "r") as json_obj:
#     json_data = json.load(fp=json_obj)  # дампаем нашу питоновскую структуру в json-файл
#     print(type(json_data), json_data)
#     for user_data in json_data:
#         print(type(user_data), user_data)

# users_list = [some_dict, some_dict_2, some_dict_3]
# data = json.dumps(users_list)  # s на конце означает дампнуть в строку (str)
# print(type(data), data)

# string_data = '[{"user": "Dasha", "password": "qwerty"}, ' \
#               '{"user": "Nikolai", "password": "123456"}, ' \
#               '{"user": "Alexey", "password": "ytrewq"}]'
# data = json.loads(string_data)
# print(type(data), data)
# for user_data in data:
#     print(type(user_data), user_data)

# Снова о менеджере контекста
# with 123:
#     pass


# class MyClass:
#     pass
#
#
# obj = MyClass()
# obj.my_method()


class MyClass:
    def __enter__(self):
        print(f"Запустился метод __enter__ из объекта {self} - например произвожу настройку файлового дескриптора")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Запустился метод __exit__ из объекта {self} - например закрытие файла")
        if exc_val:
            print("Действия, которые мы должны выполнить, если упали с ошибкой")
    # pass


try:
    obj = MyClass()
    with obj:
        # 1 / 0
        print("Начал работу внутри контекста")
    print("Работа после контекста")
except Exception as err:
    print("Ошибка", err)
