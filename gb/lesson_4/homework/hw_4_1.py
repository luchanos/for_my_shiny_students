"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для 
 конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def salary(time, stavka, premia):
    try:
        return time * stavka + premia
    except TypeError as err:
        print("Error: ", err)


if __name__ == "__main__":
    print(f"Salary - {salary(*map(int, argv[1:]))}")
