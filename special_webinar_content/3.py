# from abc import ABC, abstractmethod
#
#
# class AbstractTicket(ABC):
#     @abstractmethod
#     def use_me(self):
#         """Ожидаем тут логику использования (погашения нашего билета)"""
#         pass
#
#     @abstractmethod
#     def cancel_me(self):
#         pass
#
#
# class EventTicket(AbstractTicket):
#     def __init__(self, event, company_name):
#         self.event = event
#         self.company_name = company_name
#         self.is_valid = True
#
#     def use_me(self):
#         print(f"погашение билета на мероприятие: {self.event}")
#         self.is_valid = False
#
#     def cancel_me(self):
#         self.is_valid = False
#         print("Билет на мероприятие аннулирован")
#
#     def __str__(self):
#         return f"билет на мероприятие: {self.event}"
#
#
# class TransportTicket(AbstractTicket):
#     def __init__(self, company_name, trip_num):
#         self.event = "Проездной"
#         self.company_name = company_name
#         self.trip_num = trip_num
#
#     def use_me(self):
#         if self.trip_num == 0:
#             print("поездок не осталось")
#         self.trip_num -= 1
#         print(f"гашу очередную поездку. осталось поездок: {self.trip_num}")
#
#     def cancel_me(self):
#         self.trip_num = 0
#         print("Проездной аннулирован")
#
#     def __str__(self):
#         return f"билет на транспорт с количеством поездок: {self.trip_num}"
#
#
# class BaseContext(ABC):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#
# class SellTransportTicketContext(BaseContext):
#     def create_ticket(self):
#         return TransportTicket(*self.args, **self.kwargs)
#
#
# class SellEventTicketContext(BaseContext):
#     def create_ticket(self):
#         if self.kwargs == {}:
#             raise ValueError("Слишком мало параметров, я думаю, что вы не сможете далеко уйти с этим билетом)")
#         return EventTicket(*self.args, **self.kwargs)
#
#
# class TicketSeller:
#     def __init__(self, company_name):
#         self.company_name = company_name
#
#     def sell_ticket(self, context):
#         return context.create_ticket()
#
#
# class TicketController:
#     def __init__(self, host_name):
#         self.host_name = host_name
#
#     def use_ticket(self, ticket):
#         print(f"{self.host_name} работает с билетом: {ticket}")
#         ticket.use_me()
#
#     def cancel_ticket(self, ticket):
#         print(f"{self.host_name} пытается аннулировать билет: {ticket}")
#         ticket.cancel_me()
#
#
# seller = TicketSeller("Рога и копыта")
# sell_event_context = SellEventTicketContext(company_name="Рога и Копыта", event="концерт Король и Шут")
# transport_context = SellTransportTicketContext(company_name="Моя фирма", trip_num=11)
# tr_ticket = seller.sell_ticket(transport_context)
# ticket = seller.sell_ticket(sell_event_context)
# controller = TicketController("Какая-то организация")
# controller.use_ticket(tr_ticket)
# controller.cancel_ticket(tr_ticket)
# controller.use_ticket(tr_ticket)

### ЧАСТЬ ВТОРАЯ: АТАКА ПРИВАТНЫХ И ЗАЩИЩЕННЫХ ПОЛЕЙ


class SomeClass:
    __some_field = 1

    def __init__(self, some_field):
        self.some_field = some_field

    @classmethod
    def some_func(cls):
        print(cls.__some_field)


class AnotherClass(SomeClass):
    __some_field = 10

    def a_func(self):
        self.__some_field


a = SomeClass("test")
b = AnotherClass("one more test")
# c = SomeClass()

# b.some_func()
# a.some_func()

print(a._SomeClass__some_field)
print(b._AnotherClass__some_field)