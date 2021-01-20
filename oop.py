from uuid import uuid4
from abc import ABC, abstractmethod
import requests


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
    def notify_host(self, *args, **kwargs):
        pass

    def show_ticket_primary_info(self):
        return {"valid": self.valid, "ticket_id": self.ticket_id}


class TheaterTicket(Ticket):
    e_mail = "some-email@lolkekcheburek.com"

    def use_me(self):
        self.valid = False
        print("Даём человеку бинокль в подарок")

    def annul(self, reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")

    def notify_host(self, data):
        print(f"Отправляю данные {data} на адрес почты {TheaterTicket.e_mail}")


class FlightTicket(Ticket):
    url = "http://air-trololo.com"

    def use_me(self):
        self.valid = False
        print("Даём человеку маску в подарок")

    def annul(self, reason):
        self.valid = False
        print(f"Билет id {self.ticket_id} был аннулирован по причине {reason}")


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
f_ticket = FlightTicket()
controller.businees_logic("событие_1", f_ticket)
