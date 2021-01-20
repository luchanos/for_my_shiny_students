class Plane:
    _max_cnt = 1
    __current_cnt = 0

    def __init__(self, capacity):
        if Plane.__current_cnt == Plane._max_cnt:
            raise ValueError("Max number of plane is reached! Please sell it or do smth!")
        self._capacity = capacity
        self.current_free_places = self._capacity
        Plane.__current_cnt += 1

    def make_reservation(self, num):
        if num > self.current_free_places:
            raise ValueError(f"Overbooking Error!!! Current free places value is {self.current_free_places}")
        self.current_free_places -= num

    def __check_value_to_be_unbooked(self, num):
        if num + self.current_free_places > self._capacity:
            raise ValueError("Smth went wrong! You try to free more palces, than you have in this plane!")

    def undo_reservation(self, num):
        self.__check_value_to_be_unbooked(num)
        self.current_free_places += num

    def get_max_cnt(self):
        return Plane._max_cnt


class WarehousePlane(Plane):
    def __init__(self, capacity, stuff_capacity):
        super().__init__(capacity)
        self.stuff_capacity = stuff_capacity

    def shoot(self):
        print("ЧТо-то делаю!!!")

    def make_reservation(self, num):
        if num > 3:
            super().make_reservation(num)
        else:
            raise ValueError("Error due to booking")


class Weapon:
    def shoot(self):
        print("Я стреляю!!!")


class MilitaryPlane(WarehousePlane, Weapon):
    pass



# def func():
#     pass

plane_1 = WarehousePlane(10, 100)
plane_1.make_reservation(5, 1)
plane_1.undo_reservation(3)
print(plane_1.current_free_places)
# print(plane_3.current_free_places)
# plane_3.make_reservation(10)
# print(plane_3.current_free_places)
# plane_3.undo_reservation(5)
# print(plane_3.current_free_places)
