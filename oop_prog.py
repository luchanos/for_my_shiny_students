from abc import ABC, abstractmethod


class TicketController:
    def __init__(self, controller_id):
        self.controller_id = controller_id

    def use_ticket(self, ticket):
        ticket.be_used()
        print(f"Controller {self.controller_id} used ticket {ticket}")

    def annul_ticket(self, ticket, reason):
        ticket.annul(reason)
        print(f"Controller {self.controller_id} has annul ticket {ticket}")

    def send_data_to_partner(self, ticket):
        """Для отправки данных партнёру"""
        pass


class Ticket(ABC):
    def __init__(self):
        is_valid = True

    @abstractmethod
    def be_used(self):
        pass

    @abstractmethod
    def be_annuled(self, reason):
        pass


class FlightTicket(Ticket):
    """Для самолётов"""
    def __init__(self, air_company):
        super().__init__()
        self.air_company = air_company

    def be_used(self):
        print("Начисляю бонусные баллы пассажиру за перелёт")

    def be_annuled(self, reason):
        print(f"Билет аннулирован по причине: {reason}")


class TheatreTicket(ABC):
    def __init__(self, theatre_name):
        super().__init__()
        self.theatre_name = theatre_name

    def be_used(self):
        print("Идём на спектакль!")

    def be_annuled(self, reason):
        print(f"Билет аннулирован по причине: {reason}")


c = TicketController(123)

l = [TheatreTicket("sddgdf"), FlightTicket("dsvdsfv")]
for ticket in l:
    c.use_ticket(ticket)


# интерфейс БИЛЕТ
# be_used - каждому позволено сделать что-то свое. Например начислить бонусные баллы AEROFLOT, RZD, TICKETLAND.