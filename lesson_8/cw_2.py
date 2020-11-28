class MyClass:
    __cnt = 0

    def __init__(self):
        MyClass.__cnt += 1

    @classmethod
    def get_cnt(cls):
        return cls.__cnt

    def get_cnt_2(self):
        return self.__cnt

    @classmethod
    def print_info(cls):
        return f"Какая-то важная информация про {cls}"


class MyClass2(MyClass):
    pass


def some_func_3():
    return "Доп метод"



# ex = MyClass()
# some_class = ex.__class__
# MyClass.some_new_func = some_func_3
# print(MyClass.some_new_func())
# print(some_class.some_new_func())












class NewException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]



def division(a, b):
    if not b:
        raise NewException("Делить на 0 нельзя!!", [1, 2, 3])
    return a / b

try:
    division(1, 0)
except Exception as err:
    print(type(err), err)