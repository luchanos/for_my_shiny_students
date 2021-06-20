"""
На основе ДЗ из 17 урока создать дочерние классы автомобилей (служебный, скорая помощь и т.д.). Я хочу, чтобы ты
реализовала метод, который будет проверять превышает ли автомобиль скорость, рекомендованную производителем.
По сути, чтобы был метод check_velocity, который говорил бы, превышаем мы скорость или нет.
"""


def handler_func(request: dict):
    name = request['name']
    age = request['age']
    action = request['action']
    print(f'{name} возраста {age} делает {action}')


# request = {'name': 'Daria',
#            'age': 18,
#            'action': 'test_action'}
#
# handler_func(request)


def ticket_action(request: dict):
    buyer = request['buyer']
    action = request['action']
    print(f'{buyer} делает {action}')


def ticket_action_2(request):
    buyer = request['buyer']
    action = request['action']
    seller = request['seller']
    print(f'{buyer} делает {action} от {seller}')


def ticket_action_3(request):
    client = request['client']
    action = request['action']
    print(f'{client} делает {action}')


class TicketRequestHandler:
    def ticket_action(self, request):
        buyer = request['buyer']
        action = request['action']
        return {"method": True}

    def setup(self):
        print("Этот метод всегда будет отрабатывать при каких-то условиях")

    def validate_user(self):
        print("Этот метод проверяет, что пользователь авторизован")


class TicketRequestHandlerV2(TicketRequestHandler):
    def ticket_action(self, request):
        buyer = request['buyer']
        action = request['action']
        return {"method_2": True}


request = {'buyer': 'Daria',
           'action': 'test_action'}

# ticket_request_handler = TicketRequestHandler()
# print(ticket_request_handler.ticket_action(request))
# ticket_request_handler_v2 = TicketRequestHandlerV2()
# print(ticket_request_handler_v2.ticket_action(request))


class Animal:
    type_name = 'Животное'

    def __init__(self, weight, color, age, height):
        self.weight = weight
        self.color = color
        self.age = age
        self.height = height

    def go(self):
        print(f"{self.__class__.type_name} пришло в движение")

    def stop(self):
        print(f"{self.__class__.type_name} остановилось")

    def eat(self):
        print(f"{self.__class__.type_name} поело")

    def voice(self):
        print(f"{self.__class__.type_name} подаёт голос")


class Tiger(Animal):
    type_name = 'Тигр'

    def __init__(self, weight, color, age, height, name):
        # ЭТО МЕТО ДЛЯ ВЫЗОВА МЕТОДА РОДИТЕЛЯ И ПРОКИДЫВАНИЯ ЕМУ УЖЕ ЗАДАННЫХ В НЁМ ПОЛЕЙ
        super().__init__(weight, color, age, height)
        self.name = name

    def hunt(self):
        print("Тигр охотится")


class TigerChild(Tiger):
    type_name = 'Тигриный пездюк'

    def __init__(self, weight, color, age, height, name, is_mudak):
        super().__init__(weight, color, age, height, name)
        self.is_mudak = is_mudak


class Zebra(Animal):
    type_name = 'Клёвая зебра'

    def be_cool(self):
        print("Зебра клёвая")

animal = Animal(80, 'red', 1, 100)

tiger = Tiger(80, 'red', 30, 100, 'Petr')
tiger_2 = Tiger(80, 'red', 30, 100, 'Ivan')
# print(tiger.name)
# tiger.name = 'Mudak'
# print(tiger.name)
# print(tiger.type_name)
# print(Animal.type_name)
tiger.type_name = 'Жид-медведь'
# print(tiger.type_name)
# print(tiger_2.type_name)
# print(Animal.type_name)
# Animal.type_name = 'LOL'
# print(tiger.type_name)
# print(tiger_2.type_name)
# print(Animal.type_name)

t_c = TigerChild(80, 'red', 30, 100, 'Petr', True)
tiger.voice()
t_c.voice()
