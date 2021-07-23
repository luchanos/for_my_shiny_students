"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open("task_7.json", "w") as j_file:
    with open("task_7.txt", "r") as f_o:
        subjects = {}
        analytics = {}
        total_profit, profitable_cmp = 0, 0
        lines = f_o.read().split("\n")
        for company_info in lines:
            company_info = company_info.split()
            profit = int(company_info[2]) - int(company_info[3])
            subjects[company_info[0]] = profit
            if profit > 0:
                total_profit += profit
                profitable_cmp += 1
            analytics["average"] = total_profit / profitable_cmp
        all_list = [subjects, analytics]
    json.dump(all_list, j_file)
