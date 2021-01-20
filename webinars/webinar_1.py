class MobilePhone:

    def __init__(self, some_field, password=None):
        self.__secret_password = password
        self.some_field = some_field

    def set_password(self, password):
        if not self.__secret_password:
            self.__secret_password = password
        else:
            if not self.check_pass(password):
                return
            else:
                self.__secret_password = password

    def show_adult_content(self, password):
        if not self.__secret_password:
            return "AdultContent"
        if not self.check_pass(password):
            return
        return "AdultContent"

    def check_pass(self, password):
        if password == self.__secret_password:
            return True
        print("Wrong password!")
        return False

    @property
    def get_secret_pass(self):
        return self.__secret_password

    @property
    def make_eval(self):
        return self.some_field ** 200000

    def _make_call(self):
        print("Дзынь!")

    def __call__(self):
        self._make_call()


class Pistolet:
    def _make_shoot(self):
        print("Бах!")

    def __call__(self):
        self._make_shoot()


# class ChildMobile(MobilePhone):
#     def __init__(self, password=None):
#         super().__init__(password)
#         self.child = True
#
#     # не сработает
#     @property
#     def get_secret_pass(self):
#         return super().__secret_password + 123123123


phone = MobilePhone(123123123, '123')
print(phone.make_eval)
# print(phone.__secret_password)

# print(phone._MobilePhone__secret_password)
#
# l = [Pistolet(), MobilePhone()]
# for el in l:
#     el()





# print(phone.show_adult_content('13'))

# ph = ChildMobile(123123123)
# print(ph.get_secret_pass)

# print(phone._MobilePhone__secret_password)
# a = ChildMobile()