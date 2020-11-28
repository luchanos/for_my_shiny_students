class MobilePhone:
    def __init__(self, password=None):
        self.__secret_password = password

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


phone = MobilePhone('123')
print(phone.show_adult_content('13'))

print(phone._MobilePhone__secret_password)