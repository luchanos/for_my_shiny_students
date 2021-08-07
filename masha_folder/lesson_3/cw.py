"""
1. Написать функции, которые будут добавлять, изменять, удалять книги из базы. Написать функции, которые бы делали
выборку книг по id, названию, автору, количеству страниц.

2.* Написать класс для работы с БД (простенький клиент). На вход при создании экземпляра должен подаваться
URL базы, а методами будут функции из задания 1.

3. Доработать методы randomize_book и give_my_books для бота, чтобы можно было ими пользоваться в привязке к
боту.
"""

import psycopg2

DB_URL = "postgres://newuser:qwerty@localhost:5432/postgres"

SELECT_QUERY = """SELECT * FROM books;"""
INSERT_QUERY = """INSERT INTO books (book_name, author, genre, sheets_cnt) VALUES ('%s', '%s', '%s', %d);"""

connect = psycopg2.connect(DB_URL)
with connect.cursor() as cursor:
    cursor.execute(SELECT_QUERY)
    for el in cursor:
        print(el)

with connect.cursor() as cursor:
    cursor.execute(INSERT_QUERY % ('Капитанская дочка', 'Пушкин', 'Роман', 350))
    connect.commit()
