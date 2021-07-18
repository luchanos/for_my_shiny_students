from telebot import TeleBot


bot = TeleBot(token="")

# book_dict = {}
book_list = []


@bot.message_handler(commands=['start'])
def hello_func(message):
    print(message)


@bot.message_handler(commands=['add_book'])
def add_book(message):
    """Отправляем боту сообщение вида /add_book <а тут пишем все, что хотим>"""
    book_info = message.text[len("/add_book"):].lstrip()
    book_list.append(book_info)
    bot.reply_to(message, text=f"Книга успешно добавлена: {book_info}")
    print(book_list)


@bot.message_handler(commands=['clear_all_books'])
def clear_all_books(message):
    book_list.clear()
    bot.reply_to(message, text=f"Все книги удалены из списка!")
    print(book_list)


bot.polling()
