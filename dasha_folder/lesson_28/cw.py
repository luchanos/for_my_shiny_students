"""Добавить в приложение функционал по получению продуктов и удалению продуктов по id из
консоли по аналогии с добавлением новых продуктов. Не забыть слать оповещения пользователю
при этом ;)"""

import psycopg2
import requests

from dasha_folder.lesson_26 import TOKEN

DB_URL = "postgresql://newuser:qwerty@localhost:5432/postgres"


class MyDbClient:
    PRODUCT_SELECT_QUERY = "SELECT * FROM products LIMIT %d"
    PRODUCT_INSERT_QUERY = "INSERT INTO products (description, quantity) VALUES ('%s', %d)"
    PRODUCT_DELETE_BY_ID_QUERY = "DELETE FROM products WHERE product_id = %d"

    def __init__(self, db_url):
        self.db_url = db_url
        self.connect = None

    def setup(self):
        self.connect = psycopg2.connect(self.db_url)

    def _check_connection(self):
        if not self.connect:
            print("Connection has not been set up! Please, user client.setup method to install connection!")
            return

    def get_products(self, limit):
        """Получает заданное количество записей из таблица products"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.PRODUCT_SELECT_QUERY % limit)
            return cursor.fetchall()

    def insert_new_product(self, description, quantity):
        """Создаёт новый продукт в таблице products"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.PRODUCT_INSERT_QUERY % (description, quantity))
            self.connect.commit()

    def delete_product_by_id(self, product_id):
        """Удаляет продукт в таблице products"""
        self._check_connection()
        with self.connect.cursor() as cursor:
            cursor.execute(self.PRODUCT_DELETE_BY_ID_QUERY % product_id)
            self.connect.commit()


class MyTgClient:
    def __init__(self, token, chat_ids):
        self.token = token
        self.chat_ids = chat_ids

    def send_text_message(self, message):
        for chat_id in self.chat_ids:
            requests.get(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={message}")


class MyApplication:
    def __init__(self, db_client, tg_client):
        self.db_client = db_client
        self.tg_client = tg_client

    def setup_all_components(self):
        self.db_client.setup()

    def create_new_product(self):
        params = dict()
        params['description'] = input("Enter description: ")
        params['quantity'] = int(input("Enter quantity: "))
        self.db_client.insert_new_product(**params)
        message = f"New product: {params} has been created"
        self.tg_client.send_text_message(message)

    def run(self):
        self.setup_all_components()
        choice_mapper = {
            "q": exit,
            "1": self.create_new_product
        }

        print("Привет! Это приложение продуктового магазина! Введите команду для работы с ним или q для завершения.")
        print("q - завершить работу с приложением\n"
              "1 - создать новый продукт")
        while True:
            try:
                user_choice = input("Введите ваш выбор: ")
                choice_mapper[user_choice]()
            except KeyError:
                print("Вы ввели что-то не то, попробуйте ещё раз! ")


my_tg_client = MyTgClient(TOKEN, [362857450, 308251648])
my_db_client = MyDbClient(DB_URL)
my_application = MyApplication(db_client=my_db_client, tg_client=my_tg_client)
my_application.run()
