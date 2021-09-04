import requests

"""ДЗ - написать к нашему клиенту ещё парочку методов - отправлять видео и отправлять аудио"""


"https://api.telegram.org/bot1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg/sendMessage?chat_id=362857450&text=1234"
"https://api.telegram.org/bot1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg/getUpdates"


class MyTgBotClient:
    """Клиент для отправки сообщений в телегу"""
    base_tg_url = "https://api.telegram.org/"

    def __init__(self, token: str):
        self.token = token

    def send_message(self, chat_id: int, message):
        url = f"{self.base_tg_url}bot{self.token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    def send_photo(self, chat_id: int, photo):
        url = f"{self.base_tg_url}bot{self.token}/sendPhoto?chat_id={chat_id}&photo={photo}"
        requests.get(url)

    def send_file(self, chat_id: int, document: str):
        data = open("text.txt", "r")
        url = f"{self.base_tg_url}bot{self.token}/sendDocument"
        requests.get(url, data=data, params={"chat_id": -509200374})


token = "1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg"
my_tg_client = MyTgBotClient(token)
# my_tg_client.send_message(chat_id=-509200374, message=123456)
# photo_url = "https://n1s1.elle.ru/48/7b/36/487b36300c62c5f0cb905da52aa874b4/728x486_1_30b570c2f6c0da65bb56095068e05768@940x627_0xc0a839a4_18087198581488362059.jpeg"
# my_tg_client.send_photo(photo=photo_url, chat_id=-509200374)
path_to_doc = "/Users/nnsviridov/PycharmProjects/AcademicProjects/for_my_shiny_students/dasha_folder/lesson_32/text.txt"
my_tg_client.send_file(document=path_to_doc, chat_id=-509200374)

# curl -v -F "chat_id=569502265" -F document=@/Users/users/Desktop/file.txt https://api.telegram.org/bot<TOKEN>/sendDocument


# curl -v -F "chat_id=-509200374" -F document=@/Users/nnsviridov/PycharmProjects/AcademicProjects/for_my_shiny_students/dasha_folder/lesson_32/text.txt https://api.telegram.org/bot1804878764:AAEJc8FAgAaVJHm4xyYDNtizWLhmCk6zxPg/sendDocument
