"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def user_info(name, surname, birth_date, city, email, phone):
    return f"Name: {name}\n" \
           f"Surname: {surname}\n" \
           f"Birth date: {birth_date}\n" \
           f"City: {city}\n" \
           f"Email: {email}\n" \
           f"Phone: {phone}"


print(user_info(name="Nikolai",
                surname="Sviridov",
                birth_date="03.07.1991",
                city="Los Gigantes",
                email="nikolasluchanos@leprosorium.ru",
                phone="+345828421245"))
