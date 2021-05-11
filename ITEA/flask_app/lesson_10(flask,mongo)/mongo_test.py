import mongoengine as me
from datetime import datetime as dt

# полный путь коннекта указывать необязательно!
connect = me.connect("TEST_LESSON_10")


class UserProfile(me.Document):
    login = me.StringField(required=True, min_length=3, max_length=120, unique=True)
    password = me.StringField(required=True, min_length=8)  # в таком виде хранить пароли не стоит, надо хэшировать
    about_me = me.StringField()
    likes = me.IntField(default=0)


# коллекции = индексы
class User(me.Document):
    # объявляем поля коллекций
    first_name = me.StringField(min_length=1, max_length=100, required=True)
    last_name = me.StringField(min_length=1, max_length=100)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()
    user_profile = me.ReferenceField(UserProfile, reverse_delete_rule=me.CASCADE)

    # CASCADE - удалит юзера при удалении профайла
    # подробнее - https://docs.mongoengine.org/apireference.html

    def say_hello(self):
        return f"Hello, {self.first_name}"

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.interests}, {self.age}"

    def save(self, *args, **kwargs):
        self.created_at = dt.now()
        super().save(*args, **kwargs)


# теперь у нас есть коллекция, мы можем в неё добавлять данные
# user = User(first_name='Nikolai',
#             last_name='Sviridov',
#             interests=['mma', 'programming'],
#             age=29)

# user = User(first_name='Maria',
#             last_name='Sviridova',
#             interests=['cooking', 'programming'],
#             age=31)

# пока ещё данных в базе нет! чтобы записать в базу:
# user.save()

# теперь можем пойти в Compass и проверить, что всё записалось нормально! Первичный ключ будет создан самостоятельно

# для получения всех аписей из коллекции:
# users = User.objects()

# теперь мы можем работать с объектами на уровне Python
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)

# построение запросов на чтение данных:

# фильтр по имени
# users = User.objects(first_name='Nikolai')
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)

# фильтр для всех, кроме (__ne - not equal, то есть не равно):
# users = User.objects(first_name__ne='Nikolai')
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)

# оператор in
# users = User.objects(age__in=[29, 33])
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)

# больше - меньше и так далее: __gt - больше, __gte - больше или равно, __lt - меньше, __lte - меньше или равно
# users = User.objects(age__gte=29)
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)

# count
# users_cnt = User.objects(age__gte=29).count()
# print(users_cnt)

# для группировок нужно переходить уже на уровень нативных запросов. Второй вариант - получить данные на уровень
# Python и уже тут продолжить с ними работу.

# НАЧАЛО ДРУГОГО ВИДЕО
# то, что мы получаем в ответ благодаря нашему фреймворку - QuerySet, в котором лежат объекты. 1 объект - 1 документ.
# users = User.objects(id="6097dc19244d4c7a7d800e4d")
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)
#     # обновляем поле
#     user.last_name = 'Sviridov'
#     user.delete()

# комбинация фильтров. Получить всех пользователей, у которых возраст либо больше 20, либо их зовут Nikolai:
# users = User.objects(me.Q(age__gte=30) | me.Q(first_name='Nikolai'))  # амперсанд для "и" (&)
# for user in users:
#     print(user.first_name, user.last_name, user.interests, user.age)
#     print(user.say_hello())

# СВЯЗИ
# user_profile = UserProfile(login='luchanos', password='12345678')
# user_profile.save()
# user = User(first_name='Nikolai',
#             last_name='Sviridov',
#             interests=['mma', 'programming', 'dreams'],
#             age=29,
#             user_profile=user_profile)
# user.save()


# REST API
# API - application programming interface
# REST - общие принципы организации взаимодействия приложения с сервером посредством протокола HTTP/S

# в REST API есть общие для всех имена методов: GET, POST, PUT, UPDATE, DELETE и так далее.
