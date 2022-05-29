"""
Класс оргтехника - абстрактный

"""
from copy import deepcopy
from logging import getLogger
from abc import ABC, abstractmethod

logger = getLogger(__name__)


class OverflowError(Exception):
    def __init__(self, txt, *args, **kwargs):
        self.txt = txt


class SerialNumberError(Exception):
    def __init__(self, txt, *args, **kwargs):
        self.txt = txt


class Orgtech(ABC):
    serial_number_set: set

    def __init__(self, serial_no):
        if serial_no not in self.serial_number_set:
            self.__class__.serial_no = serial_no
            self.__class__.serial_number_set.add(serial_no)
        else:
            raise SerialNumberError("такой серийник уже есть!")
        self.department = None

    def __str__(self):
        return f"{type(self)} s/n {self.serial_no}"

    def set_department(self, department):
        self.department = department

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class Modem(Orgtech):
    serial_number_set = set()

    def make_send_data(self, data):
        return f"modem with s/n {self.serial_no} send {data}"

    def __call__(self, data, *args, **kwargs):
        return self.make_send_data(data)


class Printer(Orgtech):
    serial_number_set = set()

    def make_print(self, data):
        return f"printer with s/n {self.serial_no} print {data}"

    def __call__(self, data, *args, **kwargs):
        return self.make_print(data)


class Scanner(Orgtech):
    serial_number_set = set()

    def make_scan(self, data):
        return f"scanner with s/n {self.serial_no} scan {data}"

    def __call__(self, data, *args, **kwargs):
        return self.make_scan(data)


class Xerox(Orgtech):
    serial_number_set = set()

    def make_copy(self, data):
        return f"xerox with s/n {self.serial_no} copy {data}"

    def __call__(self, data, *args, **kwargs):
        return self.make_copy(data)


class Warehouse:

    def __init__(self, max_volume, tech_mapper, department):
        self.max_volume = max_volume
        self.tech_buffer = tech_mapper
        self.department = department

    def put_to_warehouse(self, technic):
        if len(self.tech_buffer) == self.max_volume:
            raise OverflowError("Склад переполнен!")
        technic.set_department(self.department)
        self.tech_buffer[technic.__class__].add(technic)

    def get_from_warehouse(self, tech_type):
        tech_from_warehouse = self.tech_buffer[tech_type].pop()
        tech_from_warehouse.set_department(None)
        return tech_from_warehouse

    def print_info_about_stocks(self):
        for el in self.tech_buffer:
            print(el)



# data = "какие-то данные"
# for el in tech_list:
#     print(el(data))

try:
    mapper = {Scanner: set(),
              Printer: set(),
              Modem: set(),
              Xerox: set()}
    sklad = Warehouse(40, mapper, "storage and logistics")
    sales_department_sklad = Warehouse(5, deepcopy(mapper), "sales and marketing")

    tech_list = [Scanner(1), Printer(2), Xerox(31), Modem(4), Xerox(3), Xerox(39), Xerox(30)]
    for el in tech_list:
        sklad.put_to_warehouse(el)
    printer = sklad.get_from_warehouse(Printer)
    sales_department_sklad.put_to_warehouse(printer)
    c = 1
except OverflowError as err:
    logger.error("Возникла ошибка при попытке поместить технику на склад", err)
except SerialNumberError as err:
    logger.error("Возникла ошибка при попытке создать технику", err)
