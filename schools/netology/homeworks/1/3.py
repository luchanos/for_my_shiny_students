"""
Введите заработную плату в месяц: 100000
Введите, какой процент(%) уходит на ипотеку: 30
Введите, какой процент(%) уходит на жизнь: 50

Вывод:
На ипотеку было потрачено: 360000 рублей
Было накоплено: 240000 рублей
"""

sal = int(input("Введите заработную плату в месяц: "))
perc = int(input("Введите, какой процент(%) уходит на ипотеку: "))
life = int(input("Введите, какой процент(%) уходит на жизнь: "))
print("Вывод:")
ipot = sal * 0.3 * 12
print("На ипотеку было потрачено: %d рублей" % ipot)
print("Было накоплено: %d рублей" % ((sal - sal * 0.5) * 12 - ipot))