def deco(msg):
    c = 1
    def deco_2(f):
        c = 1
        def inner(*args, **kwargs):
            c = 1
            print(msg)
            return f(*args, **kwargs)

        return inner
    return deco_2


def deco_2_single(f):
    def inner_2_single(*args, **kwargs):
        print("Покупайте наших щенят")
        return f(*args, **kwargs)

    return inner_2_single


def retry(f):
    def inner(*args, **kwargs):
        max_atts = 10
        while max_atts != 0:
            try:
                return f(*args, **kwargs)
            except Exception as err:
                max_atts -= 1
                print("Ошибка!", err, "Попыток осталось:", max_atts)
                if max_atts == 0:
                    raise
    return inner


def adv(f):
    def adv_inn(*args, **kwargs):
        print("Покупайте наших щенят")
        return f(*args, **kwargs)

    return adv_inn


# res_deco = deco(summarizer)
# print(res_deco)
# print(res_deco(1, 8))

# res_deco_2 = deco(my_shiny_func)
# print(res_deco_2)
# print(res_deco_2())

# my_shiny_func = deco(my_shiny_func)

c = 1


# @deco(msg="Моё сообщение")  # тут вернется вложенная функция deco_2, которая и будет являться декоратором для f
# @deco(msg="Моё сообщение 2")
# @deco_2_single
# def m_test_func(a, b):
#     print("Сумма двух аргументов:", a + b)
#     print("Это тестовая функция")


# print(m_test_func)
# m_test_func(1, 2)
# m_test_func_2 = deco(m_test_func, "Мое сообщение")  # НЕ ДЕЛАЙТЕ ТАК!
# m_test_func_2 = deco("Моё сообщение")
# print(m_test_func_2)

@retry
@adv
def m_t_f():
    1 / 0


m_t_f()