"""
1. Exceptions
2. retry декоратор с параметром

Написать логирующий декоратор. Принимает на вход параметр True или False. Если True, то записывать результат
работы программы в текстовый файл. В противном случае - нет.

Дз: выучить как писать параметризованный декоратор с параметром. Ты будешь писать его прямо на уроке.

 - Написать функцию, которая принимает на вход строку символов, которые разделены пробелом. Среди символов могут быть
 целые числа. Нужно посчитать среднее значение, зависящее от количества чисел, которые попались в строке (то есть это
 сумма всех чисел, деленная на их количество). Например: 'a b c 1 2 3' - вернет 2. 'a b c d e f' - должно вернуть 0.

- установить на комп GIT - см. файл glossary
"""


def myzhik(f):
    """Задача мужика - собрать для нас ящик, в котором лежит наш ящик, который мы отдали ему в качестве параметра"""
    def inner_yashik(*args, **kwargs):
        print("Реклама")
        return f(*args, **kwargs)

    return inner_yashik


def simple(a, b):
    return a / b


def simple_2():
    print("Сообщение")


# параметризованный декоратор с параметром.
# постановка задачи: мы хотим иметь декоратор, который при возникновении ошибки в переданной в него функции будет
# пытаться повторить запуск этой функции с теми её параметрами до N раз. В случае неуспеха необходимо будет сделать
# raise ошибки, в случае успеха - прекрастить повторные попытки запуска. А также хочется иметь возможность настраивать
# количество попыток для повторения.

# def make_request():
#     print("Пытаюсь пойти во внешинй сервис")
#     raise ZeroDivisionError("Ты, козел, делишь на НОЛЬ! АХАХАХАХАХАХАА, ЛОХ!")  # моделируем возникновение ошибки


# def func(ls):
#     try:
#         try:
#             print(ls[10])
#         except IndexError:
#             print("Ошибка списка")
#         make_request()
#     except ZeroDivisionError as err:
#         print("Error", err)
#     print("закончили")


# def func(ls):
#     try:
#         print(ls[10])
#         make_request()
#     except ZeroDivisionError as err:
#         print("Error", err)
#     except IndexError as err:
#         print(f"Ошибка списка! {err}")
#     except Exception:
#         print("Всё остальное")
#     print("закончили")


# try:
# func([])
# except Exception as err:
#     print("Ошибка на высшем уровне", err)


# try:
#     print(ls[10])
#     make_request()
# except ZeroDivisionError as err:
#     print("Error", err)
# print("закончили")

# s = input().split()
# res = []
# for el in s:
#     res.append(int(el))
# print(res, s)



# RETRY_CNT = 10


# def retryer(f):
#     def inner(*args, **kwargs):
#         cnt = 0
#         while cnt <= RETRY_CNT:
#             try:
#                 return f(*args, **kwargs)
#             except Exception as err:
#                 print(f"Ошибка!!! Попыток осталось: {RETRY_CNT - cnt}", err)
#             cnt += 1
#     return inner


# @retryer
# def simple(a, b):
#     return a / b


# @retryer
# def simple_2():
#     print("Сообщение")
# print(simple(1, 0))


def retry_with_param(retry_cnt):
    def retryer(f):
        def inner(*args, **kwargs):
            cnt = 0
            while cnt <= retry_cnt:
                try:
                    return f(*args, **kwargs)
                except Exception as err:
                    print(f"Ошибка!!! Попыток осталось: {retry_cnt - cnt}", err)
                cnt += 1
        return inner
    return retryer


# def simple(a, b):
#     return a / b


# def simple_2():
#     print("Сообщение")


# res = retry_with_param(5)(simple)(1, 2)

# res = retry_with_param(5)(simple)  # получили робота, который собирает коробки с коробками


@retry_with_param(10)
def simple_3(a, b):
    return a / b


@retry_with_param(5)
def simple_4():
    raise ValueError
    print("Сообщение")


print(simple_3(1, 0))
print(simple_4())
