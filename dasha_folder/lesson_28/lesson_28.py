import psycopg2

DB_URL = "postgresql://newuser:qwerty@localhost:5432/postgres"

connect = psycopg2.connect(DB_URL)


def get_all_products(limit):
    """Получает заданное количество записей из таблица products"""
    connect = psycopg2.connect(DB_URL)
    with connect.cursor() as cursor:
        cursor.execute("SELECT * FROM products LIMIT %d" % limit)
        return cursor.fetchall()


def insert_new_product(description, quantity):
    """Создаёт новый продукт в таблице products"""
    # connect = psycopg2.connect(DB_URL)
    with connect.cursor() as cursor:
        cursor.execute("INSERT INTO products (description, quantity) VALUES ('%s', %d)" % (description, quantity))
        # connect.commit()


def delete_product_by_id(product_id):
    """Удаляет продукт в таблице products"""
    # connect = psycopg2.connect(DB_URL)
    with connect.cursor() as cursor:
        cursor.execute("DELETE FROM products WHERE product_id = %d" % product_id)
        connect.commit()


get_all_products(19)
insert_new_product('Макароны2', 500)
delete_product_by_id(4)
