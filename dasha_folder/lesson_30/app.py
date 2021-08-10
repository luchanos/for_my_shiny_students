"""Прочитать про коды ответов HTTP

Добавить функционал для получения продукта по id, удаление продукта по id"""

from flask import Flask, request, Response

import json

from dasha_folder.lesson_28.cw import MyDbClient
from dasha_folder.lesson_28.lesson_28 import DB_URL

my_db_client = MyDbClient(DB_URL)
my_db_client.setup()

app = Flask("products_app")
app.my_db_client = my_db_client


@app.route("/")
def homepage():
    return "OK"


# @app.route("/create_new_product", methods=["POST", "GET"])
# def create_new_product():
#     data_for_new_product = request.json
#     product_id = app.my_db_client.create_new_product(**data_for_new_product)
#     return f"Новый продукт с id {product_id} был создан!"


@app.route("/create_new_product", methods=["POST", "GET"])
def create_new_product():
    data_for_new_product = request.json
    product_id = app.my_db_client.create_new_product(**data_for_new_product)
    answer = {"result": True, "product_id": product_id}
    response = Response(json.dumps(answer), content_type="application/json", status=201)
    return response


app.run()
