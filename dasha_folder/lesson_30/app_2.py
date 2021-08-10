from flask import Flask, request, Response
import requests


app = Flask("products_app_b2b")



@app.route("/create_new_product_b2b", methods=["POST", "GET"])
def create_new_product_via_b2b():
    custom_data = {"description": "b2b_product3", "quantity": 100}
    res = requests.post("http://127.0.0.1:5000/create_new_product", json=custom_data)
    return "OK"


app.run(host="127.0.0.1", port=5001)
