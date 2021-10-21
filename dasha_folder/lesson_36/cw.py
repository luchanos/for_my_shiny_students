"""Домашнее задание: выучить базовые типы исключений"""

from flask import Flask

app = Flask('MyApp')

phones = {
    1347037755: "+7 903 625 98 77"
}


@app.route("/dasha/<int:param>")
def homepage(param):
    try:
        phone = phones[param]
    except KeyError as err:
        print(err)
        phone = None
    if phone is None:
        return {"success": False, "result": f"param {param} has not been found in phones dictionary"}
    return {
            "success": True,
            "result": {
                        "phone": phone,
                        "is_replaced": True
                      }
            }


app.run()
