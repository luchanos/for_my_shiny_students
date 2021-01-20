from datetime import datetime
from time import sleep


class PlaneCabin:
    _max_cnt = 1
    __current_cnt = 0

    __auth = {"secret": "Nikolai Sviridov",
              "some pass": "Vladislav Makeev"}

    def __init__(self, capacity, extra_places):
        self._capacity = capacity
        self.extra_places = extra_places
        self.current_free_places = self._capacity
        PlaneCabin.__current_cnt += 1

    def make_reservation(self, num):
        if num > self.current_free_places:
            raise ValueError(f"Overbooking Error!!! Current free places value is {self.current_free_places}")
        self.current_free_places -= num

    @property
    def succeed_koef(self):
        sleep(5)
        return (self._capacity + self.extra_places - self.current_free_places) /\
               (self._capacity + self.extra_places)

    def __check_value_to_be_unbooked(self, num):
        if num + self.current_free_places > self._capacity:
            raise ValueError("Smth went wrong! You try to free more palces, than you have in this plane!")

    def undo_reservation(self, num):
        self.__check_value_to_be_unbooked(num)
        self.current_free_places += num

    def get_max_cnt(self):
        return PlaneCabin._max_cnt

    def get_current_cnt(self, password):
        if password in PlaneCabin.__auth:
            with open("access_log.txt", "a") as log:
                log.write(f"{datetime.now()}: {PlaneCabin.__auth[password]}\n")
            print("ПРОИЗОШЕЛ ДОСТУП К ПРИВАТНОМУ ПАРАМЕТРУ! ДЕЛАЮ ЗАПИСЬ В БАЗУ")
            return PlaneCabin.__current_cnt
        else:
            raise ValueError("Неверный пароль!")

    def __repr__(self):
        return f"Capacity: {self._capacity}\nFree places: {self.current_free_places}\nExtra: {self.extra_places}"

    def __str__(self):
        return f"Capacity: {self._capacity}\nFree places: {self.current_free_places}\nExtra: {self.extra_places}"

    def __add__(self, other):
        capacity = self._capacity + other._capacity
        extra = self.extra_places + other.extra_places
        return PlaneCabin(capacity, extra)

    def __mul__(self, other):
        pass

    def __iter__(self):
        yield {"name": "capacity", "value": self._capacity}
        yield {"name": "extra_places", "value": self.extra_places}
        yield {"name": "current_free_places", "value": self.current_free_places}

    def __eq__(self, other):
        return (self.extra_places == other.extra_places) and (self._capacity == other._capacity)

klm = PlaneCabin(10, 2)
c = 2
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")
# klm.get_current_cnt("secret")
# klm.get_current_cnt("some pass")



# lufthanza = PlaneCabin(10, 2)
# print(id(klm), id(lufthanza), klm == lufthanza)
# turkish_airlines = PlaneCabin(7, 5)
# common_cabin = klm + lufthanza + turkish_airlines
# print(common_cabin)

# klm_iterator = iter(klm)
# print(klm_iterator)

# for field in klm:
#     print(field)
#
#
# l = [1, 2, 3]
# print(iter(l))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for el in l:
#     print(l)

# iterator = iter(l)
# try:
#     while True:
#         print(next(iterator))
# except StopIteration as err:
#     print("итерация завершена")


# class SlaboyeZveno:
#     def __init__(self):
#         self.start_priz = 0
#         self.finish_priz = 10_000
#
#     def __iter__(self):
#         return SlaboyeZvenoIterator(self.start_priz, self.finish_priz, 1000)
#
#
# class SlaboyeZvenoIterator:
#     def __init__(self, start, finish, step):
#         self.start = start
#         self.finish = finish
#         self.step = step
#         self.current_value = self.start
#
#     def __next__(self):
#         if self.current_value < self.finish:
#             self.current_value += self.step
#             return self.current_value
#         else:
#             raise StopIteration("Итерация завершена!")
#
#     def to_start(self):
#         self.current_value = 0
#
#     def to_value(self, value):
#         self.current_value = value
#
#     def __iter__(self):
#         return self
#
#
# from time import sleep
#
# sl_z = SlaboyeZveno()
# iterator = iter(sl_z)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# iterator.to_start()
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))





