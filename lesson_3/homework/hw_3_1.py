"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as err:
        print("Error: ", err)


print(division(1, 0))
