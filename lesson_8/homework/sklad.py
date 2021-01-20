from abc import abstractmethod, ABC
from enum import Enum


class Departments(Enum):
    SERVICE = "service"
    SALES = "sales"
    WAREHOUSE = "warehouse"


class Technics(ABC):
    def __init__(self, model, serial_no):
        self.model = model
        self.serial_no = serial_no
        self.department = None

    def _set_department(self, department):
        self.department = department

    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Printer(Technics):
    def print_smth(self, data):
        return f"Printer {self.model} s/n {self.serial_no} printed {data}"


class Scanner(Technics):
    pass


class Xerox(Technics):
    pass


class OverflowError(Exception):
    def __init__(self, txt, *args, **kwargs):
        self.txt = txt


class Warehouse:
    def __init__(self, name, max_volume):
        self.name = name
        self.max_volume = max_volume
        self.storage = {
            "scanners": set(),
            "printer": set(),
            "xeroxes": set()
        }

    def get_tech_to_warehouse(self, technics):
        add_mapper = {
            Scanner: "scanners",
            Printer: "printers",
            Xerox: "xeroxes"
        }