from flask import Flask, request, jsonify, Response
from models import User

app = Flask(__name__)


# к этому методу можно будет обратиться по 2м URI
@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/user/<string:user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id=None):
    if request.method == 'GET':
        # получаем данные о пользователе, превращаем в json и отдаём на клиент
        users = User.objects()
        users_json = users.to_json()  # сделает строку
        # jsonka = json.loads(users_json)
        # return jsonify(jsonka)  # по умолчанию возвращает content-type HTML
        return Response(users_json, content_type='application/json', status=200)
    elif request.method == 'POST':
        # записываем данные о пользователе в базу
        res = User(**request.json).save()
        return Response(f'User with id {res.id} has been created', status=200)
    elif request.method == 'PUT':
        # редактируем данные о пользователе
        user = User.objects().get(id=user_id)
        user.update(**request.json)  # для обновления данных в базе по пользователю
        user.reload()  # синхронизируем объект в базе с тем, который у нас сейчас на стороне Python
        return Response(f'User with id {user_id} has been updated', status=200)
        # принято в ответах отдавать сам объект, с которым мы работаем
    elif request.method == 'DELETE':
        # удаляем данные о пользователе
        user = User.objects().get(id=user_id)
        user.delete()  # удаление объекта
        return Response(f'User with id {user_id} has been deleted', status=200)


app.run(debug=True)


# http заголовки - там много всяких полезных штук, например куки
