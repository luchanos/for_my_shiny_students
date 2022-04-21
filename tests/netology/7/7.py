def cook_book_made(file):
    '''This is general function'''
    with open(file, 'r', encoding="UTF-8") as f:
        cook_book = dict()
        for line in f:
            name = line.rstrip()
            value = int(f.readline()) + 1
            list_ingredients = list()
            for i in range(1, value):
                ingredient_name, quantity, measure =(f.readline().rstrip().replace(' ', '').split('|'))
                list_ingredients.append({'ingredient_name' : ingredient_name, 'quantity' : quantity, 'measure' : measure})
                cook_book[name] = list_ingredients
            f.readline()
        return cook_book


cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
    'Фахитос': [{'ingredient_name': 'Говядина ', 'quantity': 500, 'measure': ' г'},
         {'ingredient_name': 'Перец сладкий ', 'quantity': 1, 'measure': ' шт'},
         {'ingredient_name': 'Лаваш ', 'quantity': 2, 'measure': ' шт'},
         {'ingredient_name': 'Винный уксус ', 'quantity': 1, 'measure': ' ст.л'},
         {'ingredient_name': 'Помидор ', 'quantity': 2, 'measure': ' шт'}]
  }


def test_cook_book_made():
    res = cook_book_made('7/in_book.txt')
    assert cook_book == res


def get_shop_list_by_dishes(dishes, person):
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
        ]
    }
    #dishes = []
    #name = 'Омлет'
    value = len(dishes)
    ingridients_dict = dict()
    ingridients = []

    for dish in dishes:
      for i in cook_book:
        if i == dish:
            x_1 = cook_book.get(dish)
            for i_1 in x_1:
                ingridients.append(i_1)

    for i in ingridients:
        ing_name = i.get('ingredient_name')
        ingridients_dict[ing_name] = i
    for i in ingridients_dict.values():
        i.pop('ingredient_name')

    for i in ingridients_dict.values():
        i['quantity'] *= person

    return ingridients_dict


def test_get_shop_list_by_dishes():
    assert get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2) == {
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}


def test_3_task():
    file_name_1 = '1.txt'
    file_name_2 = '2.txt'
    file_name_3 = '3.txt'

    with open(file_name_1, 'r') as f1:
        row_count_file1 = len(f1.readlines())
    with open(file_name_2, 'r') as f2:
        row_count_file2 = len(f2.readlines())
    with open(file_name_3, 'r') as f3:
        row_count_file3 = len(f3.readlines())

    def read_and_write(file_name_read, file_name_write, row_count_file):
        with open(file_name_read, 'r') as f1:
            file_name_write.write(f'{file_name_read}\n')
            file_name_write.write(f'{row_count_file}\n')
            for i in range(row_count_file):
                file_name_write.write(f'{f1.readline()}')
            file_name_write.write('\n')

    with open('full_file.txt', 'w') as full_file:
        read_and_write(file_name_2, full_file, row_count_file2)
        read_and_write(file_name_1, full_file, row_count_file1)
        read_and_write(file_name_3, full_file, row_count_file3)

    with open('full_file.txt', 'r') as res_f, open('res.txt', 'r') as f_o:
        res_file_data = res_f.read()
        res_data = f_o.read()
    assert res_data == res_file_data
