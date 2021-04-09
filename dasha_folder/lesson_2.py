"""ДЗ долги по перй домашке
Смотреть 1 урок ГБ + материалы.
3 первые задачи из методички ГБ.
Научиться произносить слово КОНКАТЕНАЦИЯ.
4 Глава
"""

# s = 'some string'
# name = 'My name is Nikolai'
# name_2 = 'My name is Daria'
# name_3 = 'My name is Moses'

# КОНКАТЕНАЦИЯ
dasha_its_just_string_with_any_name = 'My name is'
name_1 = 'Nikolai'
name_2 = 'Daria'
name_3 = 'Moses'

# мы объявили строку, но никуда не присвоили (объявление "на лету").
# Память аллоцируется, но придёт уборщица и освободит холодильник
'wgerbertertert'

# print(base_str + ' ' + name_1)
# print(base_str + ' ' + name_2)
# print(base_str + ' ' + name_3)

# в памяти хранятся все промежуточные результаты (уборщица разумеется их потом уберет)
# print(dasha_its_just_string_with_any_name + ' ' + name_1 + '\n',
#       dasha_its_just_string_with_any_name + ' ' + name_2 + '\n',
#       dasha_its_just_string_with_any_name + ' ' + name_3 + '\n')


# АЛЬТЕРНАТИВЫ КОН-КА-ТЕ-НА-ЦИ-И
# Способ 1. Форматирование методом .format
# методы строк (объекты строк):
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
# print('wgerbertertert {} {} {} {} {}')
# print('wgerbertertert {} {} {} {} {}'.format(1, 2, 3, 4, 5))
# print('{} {} {}'.format(1, 2, 3, 4, 5))
# print('{4} {1} {2}'.format(1, 2, '3', 4, '5'))

# print(dasha_its_just_string_with_any_name + ' {} {} {}\n'.format(name_1, name_2, name_3))
# print(type('{}'))
# print(type({}))

# Способ 2:
# cash_balance = 100
# sample_str = '%s your deposit is: %d' % (name_1, cash_balance)
# print(sample_str)

# 3 способ
s = f'Hello! We are friends: {name_1}, {name_2}, {name_3}'
s_1 = f'{dasha_its_just_string_with_any_name} {name_1}\n'
print(s_1)
