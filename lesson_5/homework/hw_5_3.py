"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
incomes = []
with open('task_3.txt', 'r') as f_o:
    lines = f_o.readlines()

    for line in lines:
        name, income = line.split(",")
        income = int(income)
        incomes.append(income)
        if income < 20000:
            print(name)
    print(sum(incomes) / len(incomes))
