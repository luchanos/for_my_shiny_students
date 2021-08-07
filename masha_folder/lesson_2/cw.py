"""
- чем отличается сайт от web-приложения?
- что такое клиент-серверная архитектура?

todo luchanos посмотреть дозапись в json-файл
"""


# API - Aplication Programming Interface. По сути это интерфей для взиамодействия с WEB-приложением.
# Интерфейс - (область программы, которая существет для взаимодействия пользователя с программой) Набор методов для
# взаимодействия с приложением.

# Клиент - это то, что отправляет запросы.
# Сервер - это то, что обрабатывает запросы и отвечает клиенту.

# HTTP - это протокол взаимоействия.
# Протокол - набор правил и соглашений между клиентом и сервером.

from telebot import TeleBot
from random import choice

TOKEN = "1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg"
book_storage = []
# book_storage = [{'книга': 'Пушкин. Капитанская дочка', 'добавил': 'Nikolas Luchanos'},
#                 {'книга': 'Пушкин. Капитанская дочка', 'добавил': 'Nikolas Luchanos'},
#                 {'книга': 'Пушкин. Капитанская дочка', 'добавил': 'Nikolas Luchanos'},
#                 {'книга': 'Набоков. Отчаяние', 'добавил': 'Maria Sviridova'},
#                 {'книга': 'Набоков. Приглашение на казнь', 'добавил': 'Maria Sviridova'}]

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["ping"])
def echo(message):
    print(f"Получено сообщение из чата {message.chat.id} от {message.from_user.full_name}")


@bot.message_handler(commands=["add_book"])
def add_book(message):
    book_storage.append({
        "книга": message.text[9:].strip(),
        "добавил": message.from_user.full_name
    })
    print(book_storage)


@bot.message_handler(commands=["give_my_books"])
def give_my_books(message):
    books_to_send = ""
    cnt = 0
    for book in book_storage:
        if book["добавил"] == message.from_user.full_name:
            cnt += 1
            books_to_send += f"{cnt}. {book['книга']}\n"
    bot.reply_to(message, text=str(books_to_send))


@bot.message_handler(commands=["randomize_book"])
def randomize_book(message):
    books_for_randomize = []
    for book in book_storage:
        if book["добавил"] == message.from_user.full_name:
            books_for_randomize.append(book["книга"])
    random_book = choice(books_for_randomize)
    bot.reply_to(message, text=random_book)


bot.polling()
