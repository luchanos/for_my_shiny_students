from http.client import HTTPResponse

from flask import Flask, render_template

# aiohttp, tornado - похожая структура проектов

# создаём основной объект нашего приложения. Всё, что будет происходить дальше - это
# создание обвязки вокруг него.

app = Flask(__name__)


# например функцию обработчик
@app.route("/")  # создаём указание ручки, которая будет использовать нашу функцию
def hello_world():
    """Контроллер 1"""
    return "Hello, World!"


@app.route("/goodbye")
def goodbye():
    """Контроллер 2"""
    return "BYE!"


# @app.route("/haha")
# def create_order():
#     html_text = """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Привет!</title>
# </head>
# <body>
# <h1>Добро пожаловать в прекрасный новый мир!</h1>
# </body>
# </html>
#     """
#     return html_text


@app.route("/haha")
def create_order():
    return render_template("index.html")


# шаблон с аргументами
@app.route("/lol")
def greeting():
    return render_template("greeting.html", name="Николай")


@app.route("/get_orders")
def get_orders():
    lst = [f"заявка {n}" for n in range(100)]
    return render_template("orders.html", orders_list=lst)


users_dict = {1: {"name": "Николай",
             "surname": "Свиридов",
             "position": "developer"},
         2: {"name": "Мария",
             "surname": "Свиридова",
             "position": "lovely wife"},
         3: {"name": "Даша",
             "surname": "Забыл",
             "position": "student"}}


@app.route("/get_user/<int:user_id>")
def get_user(user_id):
    return render_template("user.html", user=users_dict[user_id])


@app.route("/users")
def users():
    return render_template("users.html", users_list=users_dict)


# запутанный момент с понятием СЕРВЕР
# СЕРВЕР - веб приложение, которое обслуживает различные запросы КЛИЕНТОВ к нему.
app.run(debug=True)  # параметр позволяет подробно смотреть что происходит во время каждого запроса
# запустится на  http://127.0.0.1:5000/ - ip адрес + порт

# URL - это то, что у нас в браузере
# URI - адрес без доменного имени
# MVC - model - view - controller

# модель - место для работы с базой
# вьюха - отображение
# контроллер - бизнес-логика

# web-server - скрипт, который сидит и ждёт, пока к нему придет запрос.
# декораторы добавляют нашу функцию в контроллеры по указанному пути (вспоминаем словари + функции)

# HTTP - это протокол передачи данных. Требует адрес обращения (url), метод обращения и т.д.

# все значения приводятся к HTML-разметке


# проблема - размещение HTML внутри питоновских скриптов. Мы можем вынести всё это в шаблоны

# процесс возврата шаблона в ответ пользователю - это рендер тимплейта.
