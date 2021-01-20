class Test:
    """
    Это мой кастомрный класс
    """
    __cnt = 0

    @classmethod
    def show_cnt(cls):
        c = 1
        return cls.__cnt

    @staticmethod
    def show_more_info(par1):
        c = 1
        print(par1.__cnt)
        return "Это расширенная инфромация о классе и вообще о предметной области " \
               "в которой он используется"

class SomeC(Test):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

c = SomeC(1, 2, 3)
c.show_cnt()
a = c.__class__
b = a(3, 4, 5)
d = 1