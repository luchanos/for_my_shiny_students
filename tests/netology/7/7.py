def cook_book_made(file):
    """
    Задача № 1
    """
    cook_book = dict()
    cook_recipe = {}
    cook_ingridients = {}

    with open(file, encoding='utf-8') as recipes:
        for line in recipes:
            cook_recipe[line.strip()] = []
            for i in range(int(recipes.readline().strip())):
                cook_ingridients['ingredient_name'], cook_ingridients['quantity'], cook_ingridients['measure'] = \
                    recipes.readline().strip().split('|')
                cook_ingridients['quantity'] = int(cook_ingridients['quantity'])
                for k in cook_recipe.keys():
                    cook_recipe[k].append(cook_ingridients)
                cook_ingridients = dict()
            cook_book = cook_book | cook_recipe
            cook_recipe = dict()
            recipes.readline()
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
    res = cook_book_made('recipes.txt')
    assert cook_book == res


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """
        Задача № 2
    """
    product_basket = {}
    for dish in dishes:
        if dish in cook_book:
            for item in range(len(cook_book[dish])):
                if cook_book[dish][item]['ingredient_name'] not in product_basket:
                    product_basket.setdefault(cook_book[dish][item]['ingredient_name'],
                                              {'measure': cook_book[dish][item]['measure'],
                                               'quantity': cook_book[dish][item]['quantity'] * person_count})
                else:
                    product_basket[cook_book[dish][item]['ingredient_name']]['quantity'] += \
                        cook_book[dish][item]['quantity'] * person_count

    return product_basket


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
