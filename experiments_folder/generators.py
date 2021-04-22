# def ammo(capacity):
#     print("Начинаю стрелять")
#     yield "Первая пуля пошла"
#     print("Отдых")
#     yield "Вторая пуля пошла"
#     print("Отдых")
#     yield "Третья пуля пошла"
#     print("Отдых")
#     yield "Четвёртая пуля пошла"
#     print("Отдых")
#     yield "Пятая пуля пошла"
#     print("Закончил стрелять")
#
#
# print(ammo)
# ammo_object = ammo(10)
# print(ammo_object)
#
# print(next(ammo_object))
# print("Перерыв")
# print(next(ammo_object))
# print("Перерыв")
# print(next(ammo_object))
# print("Перерыв")
# print(next(ammo_object))
# print("Перерыв")
# print(next(ammo_object))
# print("Перерыв")
# print(next(ammo_object))


"""Задача: надо разработать систему накормить 3 подопытных. Правило кормёжки такое: у нас есть скатерть-самобранка,
в которой есть определённое количество единиц еды. Количество потребляемых единиц еды каждым подопытным
параметризованно и при каждой трапезе может меняться.

Условие кормления наших подопытных следующее - сначала кормим первого, затем второго, 
после этого третьего. Кормить будем до отвала. То есть до тех пор, пока первый не наестся мы не переходим ко
второму, а от второго не переходим к третьему.

Очевидно, что кормить наших подопытных мы можем двумя способами:
- сразу вывалить на скатерть всю еду
- отдавать очередную единицу еды по запросу

Площадь скатерти - затраты памяти на хранение объектов на ней.
"""


# def my_shiny_gen(n):
#     cnt = 0
#     while cnt < n:
#         yield cnt
#         cnt += 1
#
#
# def first_eater(n, skat):
#     while n >= 0:
#         print("Первый едок съел: ", next(skat))
#         n -= 1
#
#
# def second_eater(n, skat):
#     while n >= 0:
#         print("Второй едок съел: ", next(skat) * 100)
#         n -= 1
#
#
# def third_eater(n, skat):
#     while n >= 0:
#         print("Третий едок съел: ", str(next(skat)) * 10)
#         n -= 1


# l = [x for x in range(1)]
# g = my_shiny_gen(10)
#
# first_eater(2, g)
# second_eater(3, g)
# third_eater(1, g)


# def skat(n):
#     return list(range(n))
#
#
# def first_eater(eda_list):
#     for eda in eda_list:
#         print("Первый едок съел: ", str(eda))
#
#
# def second_eater(eda_list):
#     for eda in eda_list:
#         print("Второй едок съел: ", eda * 100)
#
#
# def third_eater(eda_list):
#     for eda in eda_list:
#         print("Третий едок съел: ", str(eda) * 10)
#
#
# eda_list = skat(1_000)
# first_eater_cap = 3
# second_eater_cap = 4
# third_eater_cap = 10
# first_eater(eda_list[:first_eater_cap + 1])
# second_eater(eda_list[first_eater_cap:second_eater_cap + first_eater_cap + 1])
# third_eater(eda_list[second_eater_cap + first_eater_cap + 1:second_eater_cap + first_eater_cap + third_eater_cap + 1])
# print(1 in range(10))




# def skat(n):
#     """Функция, которая возвращает объект-генератор, способный предоставить нам элементы по запросу от 0 до n"""
#     cnt = 0
#     while cnt < n:
#         yield cnt
#         cnt += 1
#
#
# def first_eater(n, skat):
#     while n >= 0:
#         print("Первый едок съел и в результате написал: ", next(skat))
#         n -= 1
#
#
# def second_eater(n, skat):
#     while n >= 0:
#         print("Второй едок съел и в результате написал: ", next(skat) * 100)
#         n -= 1
#
#
# def third_eater(n, skat):
#     while n >= 0:
#         print("Третий едок съел и в результате написал: ", str(next(skat)) * 10)
#         n -= 1
#
#
# skat_gen_obj = skat(10)
#
# first_eater_cap = 3
# second_eater_cap = 4
# third_eater_cap = 10
#
# try:
#     first_eater(first_eater_cap, skat_gen_obj)
#     second_eater(second_eater_cap, skat_gen_obj)
#     third_eater(third_eater_cap, skat_gen_obj)
# except StopIteration:
#     print("Заряды в скатерти кончились!")