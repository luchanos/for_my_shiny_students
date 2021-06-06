"""Генераторы.

ДЗ:
- проверяю, как ты умеешь писать декораторы (основной вопрос будет про параметризованный retry)

Написать генераторную функцию которая на вход принимает число n и которая вернёт объект-генератор,
который по запросу вернёт целые числа от 0 до n.
"""

# l = [x for x in range(10)]  # ЭТО КОМПРЕХЕНШЕНЫ!!!
# print(l)

# постановка задачи: в 1 момент времени мы обрабатываем только 1 элемент последовательности. Как только обработали его
# он нам больше нужен.

import sys
from datetime import datetime

# start = datetime.now()
# l = [x for x in range(100_000_000)]
# print(sys.getsizeof(l))
# print(datetime.now() - start)

# 1 - затраты по памяти на хранение списка
# 2 - затраты по времени на его формирование

# Задача: обклеить все яблоки по одному и не хранить в памяти те, которые уже были обклеены (отправлять их куда-то в
# магазин к примеру)


def give_me_apple(num):
    cnt = 0
    res = []
    while cnt <= num:
        cnt += 1
        res.append(f"яблоко {cnt}")
    return res


def give_me_apple_dream(num):
    cnt = 0
    while cnt <= num:
        cnt += 1
        return f"яблоко {cnt}"  # а вот бы можно было бы получать тут значения и оставлять конфигурацию
    # функции в замороженном состоянии


def give_me_apple_gen(num):
    cnt = 0
    while cnt <= num:
        cnt += 1
        yield f"яблоко {cnt}"  # в этом месте я верну значение и сохраню контекст исполнения


# print(give_me_apple(100_000_000_0000_000000000000))

# def give_me_today():
#     return datetime.now()


# def messager(date):
#     with open(file='date_file.txt', mode='w') as f_o:
#         f_o.write(date)

# def messager(date):
#     f_o = open(file='date_file.txt', mode='w')
#     f_o.write(date)
#     f_o.close()


# messager(str(give_me_today()))


def simple_func():
    return 1
    return 2
    return 3



# print(simple_func)
# print(simple_func())
# print(simple_func())
# print(simple_func())


def simple_func_2():  # это генераторная функция, потому что она содержит в себе yield!!!
    print("кусок кода до возврата 1")
    yield 1
    print("кусок кода до возврата 2")
    yield 2
    print("кусок кода до возврата 3")
    yield 3
    print("кусок кода после всего")


# 1. генераторная функция возвращает объект-генератор
# 2. объект-генератор содержит в себе логику получения очередных элементов по запросу

# print(simple_func_2)
# print(simple_func_2())
# print(simple_func_2())
# print(simple_func_2())

# gen_o = simple_func_2()
# print("Кусок кода до 1 next")
# print(next(gen_o))
# print("Кусок кода до 2 next")
# print(next(gen_o))
# print("Кусок кода до 3 next")
# print(next(gen_o))
# print("Кусок кода после всех next")
# print(next(gen_o))


def give_me_apple_gen_2(num):
    cnt = 0
    while cnt < num:
        cnt += 1
        yield f"яблоко {cnt}"   # в этом месте я верну значение и сохраню контекст исполнения


# start = datetime.now()
# apple_generator_object = give_me_apple_gen_2(100_000_000)
apple_generator_object = give_me_apple_gen_2(100)
# print(sys.getsizeof(apple_generator_object))
# print(datetime.now() - start)

# apple_box = []
# cnt = 0
# while cnt < 10:
#     apple_box.append(next(apple_generator_object))
#     cnt += 1

# print(apple_box)

# print('яблоко 3' in apple_generator_object)
# print('яблоко 3' in apple_generator_object)


# while True:
#     print(next(apple_generator_object))

# если в процессе работы мы высасываем весь генератор, то выигрыша по времени не будет!
# а по памяти выигрыш все равно останется. однако, если есть необходимость хранить целиком всё нагенеренное добро,
# то выигрыша не будет.

# f_o = open(file='date_file.txt', mode='w')
# try:
#     f_o.write("sdfsdfsd")
# except Exception as err:
#     print(f"Ошибка {err}")
# finally:
#     f_o.close()

# [open(file='date_file.txt', mode='w') for _ in range(100000000)]

f_o = open(file='date_file.txt', mode='w')
print(f_o.closed)
with f_o:
    print(f_o.closed)
    f_o.write('dfsdfgs')
print(f_o.closed)

