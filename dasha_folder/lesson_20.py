# полиморфизм - от значения "много форм"

# OLD FASHION VECTOR
# class Vector:
#     def __init__(self, coord_x, coord_y):
#         self.coord_x = coord_x
#         self.coord_y = coord_y
#
#     def add_vect(self, other):
#         """Метод для сложения двух векторов"""
#         coord_x_new = self.coord_x + other.coord_x
#         coord_y_new = self.coord_y + other.coord_y
#         return Vector(coord_x_new, coord_y_new)
#
#     def sub_vect(self, other):
#         """Метод для вычитания двух векторов"""
#         coord_x_new = self.coord_x - other.coord_x
#         coord_y_new = self.coord_y - other.coord_y
#         return Vector(coord_x_new, coord_y_new)
#
#     def mul_vect_to_num(self, num):
#         """Метод для умножения вектора на число"""
#         coord_x_new = self.coord_x * num
#         coord_y_new = self.coord_y * num
#         return Vector(coord_x_new, coord_y_new)
#
#     def div_vect_to_num(self, num):
#         """Метод для деления вектора на число"""
#         coord_x_new = self.coord_x / num
#         coord_y_new = self.coord_y / num
#         return Vector(coord_x_new, coord_y_new)
#
#     def info(self):
#         return f"x: {self.coord_x}, y: {self.coord_y}"

# vector_1 = Vector(3, 4)
# vector_2 = Vector(5, 6)
# vector_3 = Vector(7, 8)
# vect_new = vector_1.add_vect(vector_2)
# vect_new_2 = vect_new.add_vect(vector_3)
# print(vect_new_2)
# print(vect_new_2.info())
# vect_new_3 = vect_new_2.mul_vect_to_num(2)
# print(vect_new_3)
# print(vect_new_3.info())

# NEW FASHION VECTOR
class Vector:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __add__(self, other):
        """Метод для сложения двух векторов"""
        if type(self) == type(other):
            coord_x_new = self.coord_x + other.coord_x
            coord_y_new = self.coord_y + other.coord_y
            return Vector(coord_x_new, coord_y_new)
        raise TypeError(f"Несовместимый для сложения тип: {type(other)}")

    def __sub__(self, other):
        """Метод для вычитания двух векторов"""
        coord_x_new = self.coord_x - other.coord_x
        coord_y_new = self.coord_y - other.coord_y
        return Vector(coord_x_new, coord_y_new)

    def __mul__(self, num):
        """Метод для умножения вектора на число"""
        coord_x_new = self.coord_x * num
        coord_y_new = self.coord_y * num
        return Vector(coord_x_new, coord_y_new)

    def __truediv__(self, num):
        """Метод для деления вектора на число"""
        coord_x_new = self.coord_x / num
        coord_y_new = self.coord_y / num
        return Vector(coord_x_new, coord_y_new)

    def __str__(self):
        """Для вывода информации при попытке напечатать объект"""
        return f"x: {self.coord_x}, y: {self.coord_y}"

    def __repr__(self):
        """Для вывода информации при попытке напечатать объект, который содержит объекты класса Vector"""
        return f"Вектор --- x: {self.coord_x}, y: {self.coord_y}"


class YebuchiyShakal:
    def __init__(self, shakals_counter):
        self.shakals_counter = shakals_counter

    # todo написать декоратор, который будет проверять совместимость типов входных данных
    def __add__(self, other):
        if type(self) == type(other):
            return YebuchiyShakal(self.shakals_counter + other.shakals_counter)
        raise TypeError(f"Несовместимый для сложения тип: {type(other)}")

    def __str__(self):
        return f"shakals_counter: {self.shakals_counter}"

    def __call__(self):
        print(f"Шакал сказал, что их тут {self.shakals_counter}!")

    def shakals_voices(self):
        print(f"Шакал сказал, что их тут {self.shakals_counter}!")


# y_shak = YebuchiyShakal(10)
# y_shak_2 = YebuchiyShakal(20)
# y_shak_2()
# y_shak_2.shakals_voices()
# res_shak = y_shak + y_shak_2
# print(res_shak.shakals_counter)

# vector_1 = Vector(3, 4)
# vector_2 = Vector(5, 6)
# vector_3 = Vector(7, 8)
# vect_new = vector_1 + vector_2 + vector_2
# print(vect_new)
# vect_new_2 = vect_new + vector_3
# print(vect_new_2)
# vect_new_3 = vect_new_2 * 2
# print(vect_new_3)

# vector_2 + y_shak_2
# y_shak_2 + vector_2

# s = {1, 2, 3, 4, 5, 6, 7, 8}
# множество - содержит ТОЛЬКО элементы котрые отосятся к неизменяемому типу данных + все они уникальны + неупорядочены
# st1 = {vector_1, vector_2, vector_3}
# print(st1)
# d = {vector_1: 1}
# print(d[vector_1])


# # 1 способ
# class NotifierSms:
#     def send_sms(self):
#         print("отправил смс")
#
#
# class NotifierTelegram:
#     def send_telegram(self):
#         print("отправил телегу")
#
#
# class NotifierWhatsapp:
#     def send_whatsapp(self):
#         print("отправил воц")
#
#
# class NotifierEmail:
#     def send_email(self):
#         print("отправил имейл")
#
#
# notifier_sms = NotifierSms()
# notifier_telegram = NotifierTelegram()
# notifier_email = NotifierEmail()
# notifier_whatsapp = NotifierWhatsapp()
#
#
# def func():
#     print("Я выполняюсь!")
#     notifier_sms.send_sms()
#     notifier_telegram.send_telegram()
#     notifier_email.send_email()
#     notifier_whatsapp.send_whatsapp()
#
#
# func()


# 2 способ
class NotifierSms:
    def __call__(self, *args, **kwargs):
        print("отправил смс")


class NotifierTelegram:
    def __call__(self, *args, **kwargs):
        print("отправил телегу")


class NotifierWhatsapp:
    def __call__(self, *args, **kwargs):
        print("отправил воц")


class NotifierEmail:
    def __call__(self, *args, **kwargs):
        print("отправил имейл")


NOTIFIERS_LIST = [
    NotifierSms(),
    NotifierTelegram(),
    NotifierEmail(),
    NotifierWhatsapp()
]


def func():
    print("Я выполняюсь!")
    for notifier in NOTIFIERS_LIST:
        notifier()


func()
