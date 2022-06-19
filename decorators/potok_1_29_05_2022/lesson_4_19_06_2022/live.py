from functools import wraps


def retry(max_atts):
    def middle(f):
        def inner(*args, **kwargs):
            nonlocal max_atts
            while max_atts != 0:
                try:
                    return f(*args, **kwargs)
                except Exception as err:
                    max_atts -= 1
                    print("Ошибка!", err, "Попыток осталось:", max_atts)
                    if max_atts == 0:
                        raise
        return inner
    return middle


def adv_main(msg):
    def adv(cls):
        class MyOtherClass(cls):
            def __str__(self):
                return f"Это класс {cls} который я задекорировал c параметром {msg}"
        return MyOtherClass
    return adv


# @retry(5)  # после запуска приведется к @middle где max_atts = 5
# @adv
# def m_t_f():
#     1 / 0
#
#
# m_t_f()


# def advs(msg):
#     if type(msg) == type(lambda: None):
#         def adv_inn(*args, **kwargs):
#             print("Покупайте наших щенят")
#             return msg(*args, **kwargs)
#         return adv_inn
#
#     def advs_inn(f):
#         def adv_inn(*args, **kwargs):
#             print(msg)
#             return f(*args, **kwargs)
#
#         return adv_inn
#     return advs_inn
#
#
# @advs("Сообщение")
# def some_func():
#     return 1


# @adv_main("Тестовое сообщение")
# def some_func():
#     return 1 / 0


# print(some_func)


@adv_main("Декорирую класс")
class MyHandler:
    def some_meth(self):
        return 1


print(MyHandler)
