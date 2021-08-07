# API - Aplication Programming Interface. По сути это интерфей для взиамодействия с WEB-приложением.
# Интерфейс - (область программы, которая существет для взаимодействия пользователя с программой) Набор методов для
# взаимодействия с приложением.

# Клиент - это то, что отправляет запросы.
# Сервер - это то, что обрабатывает запросы и отвечает клиенту.

# HTTP - это протокол взаимоействия.
# Протокол - набор правил и соглашений между клиентом и сервером.

from telebot import TeleBot
from random import choice
import psycopg2

TOKEN = "1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg"
DB_URL = "postgres://newuser:qwerty@localhost:5432/postgres"

SELECT_QUERY = """SELECT * FROM books;"""
INSERT_QUERY = """INSERT INTO books (book_name, author, genre, sheets_cnt, added_by) 
VALUES ('%s', '%s', '%s', %d, '%s');"""

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["ping"])
def echo(message):
    print(f"Получено сообщение из чата {message.chat.id} от {message.from_user.full_name}")


@bot.message_handler(commands=["add_book"])
def add_book(message):
    data_for_insert = [book_data.strip() for book_data in message.text.split("|")]
    connect = psycopg2.connect(DB_URL)
    with connect.cursor() as cursor:
        cursor.execute(INSERT_QUERY % (data_for_insert[1],
                                       data_for_insert[2],
                                       data_for_insert[3],
                                       int(data_for_insert[4]),
                                       message.chat.username))
        connect.commit()
    print(f"Книга: {data_for_insert} - добавлена {message.chat.username}")


# @bot.message_handler(commands=["give_my_books"])
# def give_my_books(message):
#     books_to_send = ""
#     cnt = 0
#     for book in book_storage:
#         if book["добавил"] == message.from_user.full_name:
#             cnt += 1
#             books_to_send += f"{cnt}. {book['книга']}\n"
#     bot.reply_to(message, text=str(books_to_send))


# @bot.message_handler(commands=["randomize_book"])
# def randomize_book(message):
#     books_for_randomize = []
#     for book in book_storage:
#         if book["добавил"] == message.from_user.full_name:
#             books_for_randomize.append(book["книга"])
#     random_book = choice(books_for_randomize)
#     bot.reply_to(message, text=random_book)


bot.polling()
