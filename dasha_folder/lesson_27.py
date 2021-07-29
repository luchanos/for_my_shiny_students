# data_list = []
# while True:
#     data = input("Введите какие-то данные: ")
#     if data == 'q':
#         break
#     data_list.append(data)
# print(data_list)
# print("Завершено")

"""
CREATE TABLE products_for_release (product_id INTEGER, description TEXT);
DROP TABLE products_for_release;


INSERT INTO products_for_release VALUES (1, 'Лук');
INSERT INTO products_for_release VALUES (2, 'Чеснок');
INSERT INTO products_for_release VALUES (3, 'Картошка');
INSERT INTO products_for_release VALUES (4, 'Масло');
INSERT INTO products_for_release VALUES (5, 'Помидор');


CREATE TABLE shops (shop_id INTEGER, shop_name TEXT, address TEXT);
INSERT INTO shops VALUES (1, 'ГУМ');
INSERT INTO shops VALUES (2, 'Елисеевский');
INSERT INTO shops VALUES (3, 'ЦУМ');
INSERT INTO shops VALUES (4, 'СПАР');


UPDATE shops SET address = 'Красная площадь, д.2' WHERE shop_id = 1;
UPDATE shops SET address = 'Тверская, д.20' WHERE shop_id = 2;
UPDATE shops SET address = 'Никольская, д.21' WHERE shop_id = 3;
UPDATE shops SET address = 'Днепропетровская, д.3' WHERE shop_id = 4;


CREATE TABLE stocks (shop_id INTEGER, product_id INTEGER, quantity INTEGER);
INSERT INTO stocks VALUES (1, 1, 100);
INSERT INTO stocks VALUES (1, 2, 100);
INSERT INTO stocks VALUES (2, 3, 100);
INSERT INTO stocks VALUES (1, 4, 100);
INSERT INTO stocks VALUES (2, 2, 200);
INSERT INTO stocks VALUES (3, 5, 250);
INSERT INTO stocks VALUES (3, 1, 250);


SELECT * FROM shops WHERE shop_id = 2;
SELECT * FROM shops WHERE shop_name = 'Елисеевский';
SELECT * FROM shops WHERE address = 'Тверская, д.20';

SELECT address FROM shops WHERE shop_id = 2;

SELECT product_id, quantity, shop_name FROM stocks INNER JOIN shops ON stocks.shop_id = shops.shop_id;

SELECT shop_name, description, quantity FROM (SELECT product_id, quantity, shop_name FROM stocks INNER JOIN shops ON stocks.shop_id = shops.shop_id) t
INNER JOIN products_for_release ON products_for_release.product_id = t.product_id;


SELECT count(quantity) FROM stocks WHERE product_id = 2;
SELECT * FROM stocks;

SELECT product_id, sum(quantity) FROM stocks GROUP BY product_id;
"""

import psycopg2

URL = "postgresql://newuser:qwerty@localhost:5432/postgres"

connection = psycopg2.connect(URL)

STOCKS_SELECT_QUERY = """SELECT * FROM stocks"""
with connection.cursor() as cursor:
    cursor.execute(STOCKS_SELECT_QUERY)
    for el in cursor:
        print(el)
