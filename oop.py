from uuid import uuid4
from abc import ABC, abstractmethod


class Ticket(ABC):

    def __init__(self):
        self.valid = True
        self.ticket_id = uuid4()

    @abstractmethod
    def use_me(self):
        pass

    @abstractmethod
    def annul(self, *args, **kwargs):
        pass

    @abstractmethod
    def _notify_host(self, *args, **kwargs):
        pass

    def show_ticket_primary_info(self):
        return {"valid": self.valid, "ticket_id": self.ticket_id}

    @staticmethod
    def some_func(a, b, c):
        print("вывожу информацию по истории возникновения билетов")


class EmailClient:
    def __init__(self, email):
        self.email = email

    def _send_email(self, data):
        print("отправил письмо")

    def __call__(self, data, *args, **kwargs):
        self._send_email(data)


class AnnulException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class UseMeException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class TheaterTicketAbstract(Ticket, ABC):
    e_mail: str
    sender_email_client: EmailClient

    def use_me(self):
        self.valid = False
        print("Даём человеку бинокль в подарок")
        raise UseMeException("Ошибка", [1, 2, 3], 123, 'adfgsdfg')

    def annul(self, reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")
        self.__class__._notify_host("data")
        raise AnnulException("Ошибка", [1, 2, 3], 123, 'adfgsdfg')


    @classmethod
    def _notify_host(cls, data):
        print(f"Отправляю данные {data} на адрес почты {cls.sender_email_client.email}")
        cls.sender_email_client(data)


class TheaterTicket(TheaterTicketAbstract):
    sender_email_client = EmailClient("some-email@lolkekcheburek.com")


class TheaterTicketBranch(TheaterTicketAbstract):
    sender_email_client = EmailClient("some@lol.com")


class FlightTicket(Ticket):
    url = "http://air-trololo.com"

    def use_me(self):
        self.valid = False
        print("Даём человеку маску в подарок")

    def annul(self, reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")

    def _notify_host(self, data):
        print(f"Отправляю POST запрос с данными {data} на адрес {FlightTicket.url}")


class Controller:

    def __init__(self, controller_id):
        self.controller_id = controller_id

    def _use_ticket(self, ticket: Ticket):
        ticket.use_me()
        print(f"Котролёр id {self.controller_id} осуществил погашение билета {ticket.ticket_id}")

    def _annul_ticket(self, ticket: Ticket, reason: str):
        ticket.annul(reason)
        print(f"Котролёр id {self.controller_id} осуществил аннулирование билета {ticket.ticket_id}")

    def businees_logic(self, event, ticket):
        if event == "событие_1":
            self._use_ticket(ticket)
        elif event == "событие_2":
            self._annul_ticket(ticket, "событие_2")

controller = Controller(1)
t_ticket = TheaterTicket()
# t_ticket.annul("причина")
# t2 = TheaterTicketBranch()
# t2.annul("другая причина")
# f_ticket = FlightTicket()
try:
    controller.businees_logic("событие_1", t_ticket)
except AnnulException as err:
    print(err)
# controller.businees_logic("событие_2", t2)
# Ticket.some_func(1, 2, 3)
