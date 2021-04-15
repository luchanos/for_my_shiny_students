"""ДЗ 4 Глава
Посравнивать произвольные строки между собой и объяснить результат
Учить приведение типов!!! Как отче наш!!!
Решать задачи!!!"""
from time import sleep

# Если бы нас попросили многократно выводить одно и то же
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)
# print(10)


# Способ вывода через цикл
# До тех пор, пока соблюдается условие мы крутим вертим цикл
cnt = 0
# limit = 7
# name = 'My name is Nikolai'

# print(1 * 100 < 2 - 10)

# бесконечный цикл
# while True:
# конечный цикл

# изменение значения переменной относительно самой себя
# cnt = cnt + 1
# cnt = cnt + 1
# cnt = cnt + 1

# более короткий способ
# cnt += 1


# while cnt <= limit:
#     sleep(.5)
#     print(cnt, name)
#     cnt = cnt + 1

# name = input("Введите своё имя:")
# print(name == 'Коля')

# s = "100000000000"
# i = int(s)


# limit = int(input("Введите количество желаемых циклов: "))

# while cnt <= limit:
#     print(cnt, input("Введите своё имя: "))
#     cnt = cnt + 1
# limit = int(limit)

name_1 = 'Николай'
name_2 = 'Даша'
name_3 = 'Мосес'

current_name = 'Асланбек 1'
current_name_2 = 'Николай'
current_name_3 = 'Даша'
current_name_4 = 'Мосес'

name_for_eq = current_name_4

# if name_1 == name_for_eq or name_2 == name_for_eq or name_3 == name_for_eq:
#     print("привет, Друг!")
# else:
#     print("Не брат ты мне!")

if name_1 == name_for_eq:
    print(f"привет, {name_1}!")
elif name_2 == name_for_eq:
    print(f"привет, {name_2}!")
elif name_3 == name_for_eq:
    print(f"привет, {name_3}!")
else:
    print("Не брат ты мне!")
