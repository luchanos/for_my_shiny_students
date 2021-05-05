# TOKEN = 0
#
#
# def my_func():
#     global TOKEN
#     TOKEN += 1
#
#
# def my_func2():
#     global TOKEN
#     TOKEN += 1
#
#
# def my_func3():
#     global TOKEN
#     TOKEN += 1
#
#
# my_func()
# my_func2()
# my_func3()
# print(TOKEN)


# def my_func_3():
#     # пример переменной в локальной области видимости объемлющей функции (E - enclosing)
#     a = False
#
#     def my_func_4():
#         nonlocal a
#         a = not a
#         f = 1
#
#     my_func_4()
#     print(a)
#
#
# my_func_3()






# def my_test_func():
#     print("Я тестовая функция")
#
#
# def my_simple_func(f):
#     """Функция, которая на вход принимает другую функцию и вызывает её внутри себя и
#     возвращает результат её исполнения"""
#     print(f"Я функция my_simple_func и я приняла на вход функцию {f}. Сейчас вызову её.")
#     res = f()
#     print("Вызов переданной функции завевршён")
#     return res
#
#
# my_simple_func(my_test_func)

# def my_simple_func_2(f):
#     """Функция, которая на вход принимает другую функцию. Далее внутри себя она собирает новую функцию,
#     которая использует в себе ту, которую мы прокинули. Собранная фукция возвращается как результат работы"""
#     c = 1
#
#     def inner(*args, **kwargs):
#         print(f"Я функция my_simple_func и я приняла на вход функцию {f} с аргументами. Сейчас вызову её.")
#         res = f(*args, **kwargs)
#         print("Вызов переданной функции завершён")
#         return res
#
#     return inner


# давайте представим, что теперь наша передаваемая функция должна иметь аргументы:
# @my_simple_func_2
# def my_test_func_args(a, b):
#     print("Я тестовая функция")
#     return a + b

# c = 1
# res = my_simple_func_2(lambda: None)()
# print(my_test_func_args(1, 2))


# def my_simple_func_5(some_param):
#     """Эта функция принимает на вход параметр, который используется для формирования функции, которая
#     будет возвращена в качестве результата вызова и которая уже В СВОЮ ОЧЕРЕДЬ ЗАДЕКОРИРУЕТ ДРУГУЮ!"""
#     c = 1
#     def my_simple_func_4(f):
#         print(f"Ого! Кто-то задал для функции-декоратора параметр: {some_param}!")
#
#         def inner(*fargs, **fkwargs):
#             print(f"Я функция my_simple_func и я приняла на вход функцию {f} с аргументами {fargs, fkwargs}. "
#                   f"Сейчас вызову её.")
#             res = f(*fargs, **fkwargs)
#             print("Вызов переданной функции завевршён")
#             return res
#
#         return inner
#     return my_simple_func_4
#
#
# @my_simple_func_5(some_param=1010101010)
# def test_func_args(a, b, c, d, *args, **kwargs):
#     print("Я функция с кучей аргументов и возвращаемым результатом")
#     return [a, b, c, d, args, kwargs]


# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))


# class MyShinyClass:
#     """Просто класс, который ничего не делает"""
#     pass
#
#
# # создание экземпляра производится с помощью () - сюда прокидываем параметры при необходимости
# my_class_ex = MyShinyClass
# print(my_class_ex)
# print(my_class_ex())


# class MyClient:
#     def __init__(self, url, secret):
#         self.url = url
#         self.secret = secret
#
#
# my_client = MyClient("youtube.com", "secret_password")


# class Cup:
#     cup_counter = 0
#
#     def __init__(self, color, weight):
#         Cup.cup_counter += 1
#         self.color = color
#         self.weight = weight
#
#     def show_temperature(self):
#         return 100
#
#     @classmethod
#     def show_cup_couner(cls):
#         return cls.cup_counter
#
#     @staticmethod
#     def cup_history():
#         return """История чашек"""


# cup1 = Cup("red", 12)
# cup2 = Cup("blue", 14)
# cup3 = Cup("black", 100)
# cup1.show_temperature()
# print(Cup.show_cup_couner())
# print(Cup.cup_history())
# print(cup3.cup_history())


# class Point2D:
#     """Класс двумерной точки, которая ещё и следит за тем, сколько её экземпляров было создано!"""
#     def __init__(self, coord_x, coord_y):
#         self.coord_x = coord_x  # это поле ЭКЗМПЛЯРА!
#         self.coord_y = coord_y
#
#     def my_shiny_method(self):
#         result = self.coord_x + self.coord_y
#         if result > 0:
#             return result
#         else:
#             raise ValueError("Result is ZERO or BELOW!")
#
#     def show_x_coord(self):
#         return self.coord_x


# class Point3D(Point2D):
#     """Дочерний класс. Вся логика работы родительского связывается с ним. Теперь мы можем добавить новые методы,
#     а также переопределить поведение старых родительских для наследника"""
#     cnt_3d = 0
#
#     def __init__(self, coord_x, coord_y, coord_z):
#         """Ключевое слово super означает, что мы обращаемся к родительскому методу! В нашей постановке задачи
#         мы хотим докинуть новое поле в наш класс, а именно третью координату в пространстве!"""
#         super().__init__(coord_x, coord_y)
#         self.coord_z = coord_z
#
#     def __new__(cls, *args, **kwargs):
#         if cls.cnt_3d == 1:
#             raise ValueError("Too many objects has been created yet!")
#         cls.cnt_3d += 1
#         return super().__new__(cls)


# point = Point3D(1, 2, 3)
# point = Point3D(1, 2, 3)
# print(point.my_shiny_method())



class Point2D:
    """Класс двумерной точки, которая ещё и следит за тем, сколько её экземпляров было создано!"""
    __point_2d_cnt = 0

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x  # это поле ЭКЗМПЛЯРА!
        self.coord_y = coord_y

    def my_shiny_method(self):
        result = self.coord_x + self.coord_y
        print(Point2D.__point_2d_cnt)
        if result > 0:
            return result
        else:
            raise ValueError("Result is ZERO or BELOW!")

    def show_x_coord(self):
        return self.coord_x

    def __add__(self, point):
        x_coord = self.coord_x + point.coord_x
        y_coord = self.coord_y + point.coord_y
        return Point2D(x_coord, y_coord)

    def __str__(self):
        return f"x: {self.coord_x} y: {self.coord_y}"


point_1 = Point2D(1, 2)
point_2 = Point2D(3, 4)
point_4 = point_1 + point_2 + point_2 + point_1
print(point_4)
print(Point2D.__point_2d_cnt)
