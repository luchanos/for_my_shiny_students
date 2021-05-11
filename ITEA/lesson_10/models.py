# MVC - model - view - controller
# Это файл с моделями

import mongoengine as me
me.connect("REST_API_TEST")


class User(me.Document):
    # объявляем поля коллекций
    first_name = me.StringField(min_length=1, max_length=100, required=True)
    last_name = me.StringField(min_length=1, max_length=100)
    interests = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()


if __name__ == '__main__':
    user = User(first_name='Nikolai',
                last_name='Sviridov',
                interests=['mma', 'programming'],
                age=29)
    user.save()
    user = User(first_name='Maria',
                last_name='Sviridova',
                interests=['cooking', 'programming'],
                age=31)
    user.save()
