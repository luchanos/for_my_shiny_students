"""
Домашнее задание: поиграть с телеграм-ботом. Сделать несколько команд:
1. Команда add_object - добавляет в список принятый следом за командой текст
2. Команда pop_random - случайным образом извлекает из списка текст и отправляет его в ответ на команду. При этом в
списке такого текста больше быть не должно
3*. Попробовать поискать информацию о том, как можно отправлять картинки в ответ на сообщения телеграмма. Написать
команду reply_by_image, которая будет отвечать картинкой.
4. Написать декоратор, который будет писать в текстовый файл логи, когда была вызвана функция обработчик сообщения
и с капкими параметрами

curl 'https://www.avito.ru/web/3/suggest' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Origin: https://www.avito.ru' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://www.avito.ru/' \
  -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6' \
  -H 'Cookie: u=2osxy1x8.pbz25y.115zfo05mugg0; buyer_laas_location=637640; buyer_index_tooltip=1; buyer_location_id=637640; buyer_local_priority_v2=0; no-ssr=1; buyer_selected_search_radius0=0; buyer_popup_location=0; v=1627217592; luri=moskva; sx=H4sIAAAAAAACAwXBOw6AMAgA0LswOyDF%2Fm6jWIli0kkZGu%2FuewMiZd9SkfOwrFk6qrCjKUId8EKFfeVrwfbclE2QvTO6G3Zj7SICEzSoc6QUMJRC3%2FcD%2BmvyFFQAAAA%3D; dfp_group=40; showedStoryIds=68-66-63-62-61-58-50-49-48-47-42-32; lastViewingTime=1627217594391; st=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoidko0TkJ5SlU2TElJTGRDY3VNTkdBYnlzVGk3VTVKRW8wVkZQNXBSVll0ZVlpM0lxVUJ1Q2JQVUtjS0FnSGJvRTlhTEk5Q1FjcUtQWkcwK1hOM29HWjUwdU1nM2RKT0FYVjlyTXNXRzVPc2F3b1JkdDY0azl4TjNETnZrNE10dUcrTHlGMEVtek1FUkQwclpiVHRtMEsraVNRdXNmVCtFdFBhUVMvRHhNY2dUU0Z2U3FTRFRjZ0ZDRjNiVWZJbHEwYkVKcFJmblFGNkZWb2tPSGFMSG9ZcElETFVJd20rVXNpbTB6SEhmWExDeVhWOEF1WHEvNlVZTmhIY25HUE13UmJNR08wcnl1ajBydlNJeXcxUyttM0RScGhWc3RDVnNhWmFXL1VDSXdHMFM4WjZMUXVrNDArY2lvYXlXa0Y3bWpxRXRnUk1nQU1MMHlqN3FZVTBlc2NMZW9PR1hhcWlhTFl4YjVtQXhobWQ0PSIsImlhdCI6MTYyNzIxNzU5NCwiZXhwIjoxNjI4NDI3MTk0fQ.T7duScmHJwGmrAuN7vjQk8YaZH1vm_9V7C1oVytNXX4; buyer_from_page=main; f=5.4d6587121516f11bb32428cf8e3c6b5047e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b9993c021c644dee797a4f9e17b6a8c78d831064c92d93c3903815369ae2d1a81d04dbcad294c152cb0df103df0c26013aba0ac8037e2b74f9dc5322845a0cba1a2da10fb74cac1eab8b1472fe2f9ba6b91d6703cbe432bc2a71e7cb57bbcb8e0f2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd2ebf3cb6fd35a0ac20f3d16ad0b1c546fa967f4e8cd565314e1848a693355322b20a76cf0378763404438f9f51f7fb33eabbb1a921a3727dad3b2c8eb8c79cd4ffeb18e3a384f74660768b50dd5e12c321e9331dd04d3f5bf6d90886864009ff46b8ae4e81acb9fa46b8ae4e81acb9fa02c68186b443a7ac15e402c38704f625fed333c16f1265a92da10fb74cac1eab2da10fb74cac1eab25037f810d2d41a8a8ae6271c86b0a76e09c1b2d328db7bb; ft="YLdloin0rww4RZf05AP65pBdi806E331F4dWlxFEGXSKLGpYjiTRUFaLwrmFo8EiHZwDUY+x7FsmpSf3/tvKFUnT1wJX8ZsJc3Vio9GDbGSAUIwxM43hbggStQWpUq5NvD/FaAJsYO0xMKnAbn1gSD3zAvHJXxyzlncD7Lt7dKSlvSwxAYduYuMVWGFo4TUd"; isWideScreen=false' \
  --data-raw '{"query":"до","locationId":637640}' \
  --compressed
"""

# https://www.avito.ru/ - это доменное имя
# /web/3/suggest - эндпойнт или URI
# доменное имя + URI = URL

# url = 'https://api.telegram.org/bot1818338603:AAEv3AOttf2NqRSSphapItXr-ADv3sbL0tM/sendMessage?chat_id=362857450&text=test_message'

# библиотека PyTelegramBotAPI
from telebot import TeleBot

data_storage = []

TOKEN = "1828225550:AAG1HGag7J2Qjlv92GNA_YcfLbupyPGNV2E"
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['hello'])
def hello(message):
    print(f"Получено сообщение из чата {message.chat.id} от {message.from_user.full_name}")
    bot.reply_to(message, text=f"Получено сообщение из чата {message.chat.id} от {message.from_user.full_name}")


def log_decor(func):
    def inner(*args, **kwargs):
        print(f"Получено сообщение: {args[0].text} от {args[0].from_user.full_name}")
        func(*args, **kwargs)
    return inner


@log_decor
def nachinka(message):
    bot.reply_to(message, text=f"Ты ешь пирожок {message.text}")


@log_decor
def get_pirozhok(message):
    bot.reply_to(message, text="С чем хочешь?")
    bot.register_next_step_handler(message, nachinka)


@bot.message_handler(commands=['get_quiz'])
@log_decor
def quiz(message):
    bot.reply_to(message, text="Будешь пирожок?")
    bot.register_next_step_handler(message, get_pirozhok)


bot.polling()
