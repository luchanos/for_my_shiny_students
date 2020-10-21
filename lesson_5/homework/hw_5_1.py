"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open('task_1.txt', 'r') as f_o:
    while True:
        line = f"{input('Введите текст: ')}\n"
        if line == "\n":
            break
        f_o.write(line)
        lines = f_o.readlines()
        print(lines)
