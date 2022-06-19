"""
Написать класс автомобиль с атрибутами: цвет, модель, год выпуска, количество л/с. У него должны быть методы ехать
вперед, назад, вправо, влево. При этом, если машина уже едет в том направлении, в котором её хочет послать пользователь
нужно выдавать информационное сообщение пользователю об этом. Кроме того, предусмотреть метод, который заводит машину
и который глушит её. На незаведенной машине ехать нельзя, о чем следует информировать пользователя. Также нельзя
заводить уже заведенную машину и глушить уже заглушенную.
"""


class Tiger:
    def __init__(self, weight, age, color):
        """Раскрашивает нашу болванку"""
        self.weight = weight
        self.age = age
        self.color = color

    def __new__(cls, *args, **kwargs):
        """Изготавливает пустую болванку"""
        return super().__new__(*args, **kwargs)  # результатом будет пустая заготовка


# print(Tiger)
my_tiger = Tiger(1, 2, 3)
print(my_tiger)
#
# tiger_list = [Tiger() for _ in range(10)]
# print(tiger_list)

"""
Завод матрешек:

Есть аппарат, который изготавливает матрешки. Ему нужно знать технологию изготовления матрешки (заготовки) и параметры, 
которые уникальны для каждой из них (цвет, запах, масса и т.д.). У нас есть чертёж и желаемые параметры.

В чертеже написано, что заготовка будет грушеобразного вида и из дерева. А также указаны места для подстановки в них
цвета, массы и т.д. и технология для покраски и т.д.

1. Даём аппарату (интерпретатору) чертеж (сам класс) и, если этого требует технология изготовления параметры для
нашего изделия (аргументы/значения полей).
2. Аппарат (интерпретатор) смотрит в чертеж и сначала делает грушевидную деревянную заготовку (результат работы
метода __new__) и возвращает эту заготовку в качестве результата работы.
3. Аппарат (интерпретатор) берет заготовку и смотрит, а надо ли в соответствии с технологией её красить и присваивать 
ей какие-то уникальные параметры, задаваемые пользователем? Например цвет, масса и т.д. Если нет, то заготовка и будет
финальным изделием, которое будет возвращено аппаратом. Если же есть необходимость придать заготовке индивидуальные 
свойства, согласно желанию пользователя и чертежу, то аппарат запускает цикл по наделению заготовки персональными 
свойствами (метод __init__). После наделения возвращает получившуюся раскрашенную заготовку с цветом, массой и т.д.
пользователю.
"""


class Matryoshka:
    def __init__(self, weight, age, color):
        """Раскрашивает нашу болванку"""
        c = 1
        self.weight = weight  # у конкретной заготовки делаю поле weight и присваиваю туда то значение, которое дал юзер
        self.age = age
        self.color = color
        c = 1

    def __new__(cls, *args, **kwargs):
        """Изготавливает пустую болванку"""
        c = 1
        res = super().__new__(cls)  # тут соберется пустая болванка
        c = 1
        return res  # результатом будет пустая заготовка


# matryoshka = Matryoshka(weight=120, age=29, color='red')
# c = 1

class Elephant:
    def __init__(self, color, age, weight, name):
        self.weight = weight
        self.age = age
        self.color = color
        self.name = name
        self.is_moving = False

    def go(self):
        if self.is_moving:
            print("Our elephant has moving yet!")
        else:
            print(f"{self.name} is going fast!")
            self.is_moving = True

    def stop(self):
        if not self.is_moving:
            print("Our elephant has stopped yet!")
        else:
            print(f"{self.name} has been stopped!")
            self.is_moving = False


# elephant = Elephant('grey', 15, 25, 'Trevor')
# elephant_2 = Elephant('grey', 15, 25, 'German')
# print(Elephant)
# print(elephant)
# elephant.go()
# elephant_2.go()
# elephant_2.go()
# elephant_2.go()
# elephant_2.go()
# elephant_2.stop()
# elephant_2.stop()
# elephant_2.stop()
# elephant_2.stop()
# elephant_2.go()
# elephant_2.stop()
# elephant_2.go()
# elephant_2.stop()
# print(1, elephant.is_moving)
# print(2, elephant_2.is_moving)

from uuid import uuid4
from datetime import datetime


# задача: сделать приложение для продажи театральных билетов и их учета.
class Ticket:
    def __init__(self, event_date, event_address, event_name, price):
        self.event_date = event_date
        self.event_address = event_address
        self.event_name = event_name
        self.price = price
        self.unique_id = uuid4()  # сгенерит уникальный рандомный идентификатор
        self.is_active = True


class TicketSeller:
    """Продаватель билетов"""
    def sell_ticket(self, *args, **kwargs):
        ticket = Ticket(*args, **kwargs)
        self.notify_head_office(ticket)
        self.notify_client(ticket)
        self.write_data_to_database(ticket)
        return ticket

    def notify_head_office(self, ticket):
        print(f"TO HEAD OFFICE: Ticket with id {ticket.unique_id} has been sold at {datetime.now()}")

    def notify_client(self, ticket):
        print(f"TO CLIENT: Ticket with id {ticket.unique_id} has been sold at {datetime.now()}")

    def write_data_to_database(self, ticket):
        print(f"TO DATABASE: Ticket with id {ticket.unique_id} has been sold at {datetime.now()}")


class TicketUsabler:
    def use_ticket(self, ticket):
        ticket.is_active = False
        self.notify_database(ticket)

    def notify_database(self, ticket):
        print(f"TO DATABASE: {ticket.unique_id} has been used!")


ticket_data = [
    {
        "event_date": "2021-07-07 20:00:00",
        "event_address": "Moscow",
        "event_name": "Kish Concert",
        "price": 100000
    },
    {
        "event_date": "2021-11-07 19:00:00",
        "event_address": "Omsk",
        "event_name": "Kipelov",
        "price": 200000
    },
    {
        "event_date": "2021-12-07 19:00:00",
        "event_address": "St.Petersburg",
        "event_name": "Ariya",
        "price": 300000
    },
]

# seller = TicketSeller()  # создал продавателя билетов
# usabler = TicketUsabler()
# l = [seller.sell_ticket(**ticket_params) for ticket_params in ticket_data]
# for ticket in l:
#     usabler.use_ticket(ticket)
# c = 1
