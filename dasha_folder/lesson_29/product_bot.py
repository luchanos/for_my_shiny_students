import telebot

from dasha_folder.lesson_26 import TOKEN
from dasha_folder.lesson_28.cw import MyDbClient
from dasha_folder.lesson_28.lesson_28 import DB_URL
import requests

bot = telebot.TeleBot(token=TOKEN)
ADMIN_CHAT_ID = 308251648  # чат id Даши

my_db_client = MyDbClient(DB_URL)
my_db_client.setup()


@bot.message_handler(commands=["get_products_with_limit"], content_types=["text"])
def get_products_with_limit(message):
    limit = int(message.text.split()[1])
    products = my_db_client.get_products(limit)
    answer_message = "Reuslt: \n"
    for product in products:
        answer_message += f"{product[0]} {product[1]} {product[2]}\n"
    bot.reply_to(message, answer_message)


# ВАЖНЫЙ КУСОК - РАЗОБРАТЬ ПО ВИДЕОУРОКУ ПО КИРПИЧИКАМ!!!
def process_product_quantity(message, product_name):
    while True:
        try:
            product_quantity = int(message.text)
            break
        except ValueError:
            bot.reply_to(message, text=f"Введите число!")
            bot.register_next_step_handler(message, process_product_quantity, product_name)
            return
    my_db_client.create_new_product(description=product_name, quantity=product_quantity)
    answer_msg = f"Продукт успешно создан:\n{product_name} {product_quantity}"
    bot.reply_to(message, text=answer_msg)


def process_product_name(message):
    product_name = message.text
    bot.reply_to(message, text="Введите количество продукта на складе: ")
    bot.register_next_step_handler(message, process_product_quantity, product_name)


@bot.message_handler(commands=["create_new_product"])
def create_new_product(message):
    bot.reply_to(message, text="Введите название продукта: ")
    bot.register_next_step_handler(message, process_product_name)


try:
    bot.polling()
except Exception as err:
    err_msg = f"Бот перезаведен! Возникла ошибка: {err}\n"
    print(err_msg)
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ADMIN_CHAT_ID}&text={err_msg}")
    with open("logfile.txt", "w") as logfile:
        logfile.write(err_msg)
    bot.polling()
