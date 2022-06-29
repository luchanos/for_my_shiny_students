"""
## Блок 2

### Easy

1. Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.

### Medium

1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, котоая была
решена для запуска функции суммирования.
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве 
результата работы из объемлющей функции.
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран.
Что наблюдаете?
4. Осуществите вызов функции суммирования из полученной переменной.

### Hard

4. Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код? Если да, то как поменялся 
смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?

"""

"""
######## EASY #########
"""

# 1. Счетчик, который увеличивается на 1 каждый раз, осуществляется запуск функции суммирования

STUPID_COUNTER = 0


def easy_sum_func(first, second):
    global STUPID_COUNTER
    STUPID_COUNTER += 1
    return first + second


"""
######## Medium #########
"""

# 1. 3 произвольных функции со счетчиками

STUPID_COUNTER_1 = 0
STUPID_COUNTER_2 = 0
STUPID_COUNTER_3 = 0


def easy_sum_func_1(first, second):
    global STUPID_COUNTER_1
    STUPID_COUNTER_1 += 1
    return first + second


def easy_sum_func_2(first, second):
    global STUPID_COUNTER_2
    STUPID_COUNTER_2 += 1
    return first + second


def easy_sum_func_3(first, second):
    global STUPID_COUNTER_3
    STUPID_COUNTER_3 += 1
    return first + second


# 2. Функция, внутри которой объявляется функция суммирования и возвращаться
# в качестве результата работы из объемлющей функции.


def wraper():

    def easy_sum_func(first, second):
        global STUPID_COUNTER
        STUPID_COUNTER += 1
        return first + second

    return easy_sum_func

# 3. Вызвали написанную функцию и сохранили результат её работы
# в переменную.


variable = wraper()
print(variable)
# <function wraper.<locals>.easy_sum_func at 0x0000027C9F3AA700>
# variable теперь функция из локальной зоны видимости wraper


# 4. Вызов функции суммирования из полученной переменной.

print(variable(1, 2))

# Результат выполнения функции easy_sum_func()


"""
######## HARD #########
"""
# 1. Перенесите глобальный счетчик на уровень объемлющей функции.
# Будет ли работать наш код? Если да, то как поменялся смысл написанного кода?
# Если нет, то что надо изменить, чтобы всё заработало?


def wraper_2():
    global STUPID_COUNTER

    def easy_sum_func(first, second):
        STUPID_COUNTER += 1
        return first + second

    return easy_sum_func

a = wraper_2()
print(a)
# Вернулась функция easy_sum_func
try:
    print(a(1, 2))
except UnboundLocalError:
    pass
# UnboundLocalError: local variable 'STUPID_COUNTER' referenced before assignment
# Питон не понимает, что это за переменная STUPID_COUNTER (думает, что она локальная)


def wraper_2():
    stupid_counter = 0

    def easy_sum_func(first, second):
        nonlocal stupid_counter
        stupid_counter += 1
        # print(stupid_counter)
        return first + second

    return easy_sum_func


a = wraper_2()
print(a(1, 2))

# Теперь все работает
