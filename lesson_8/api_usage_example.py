from random import choice
from requests import request
from envparse import env

# Получаем множество прокомментировавших на Ютубе
youtube_comments = request(method='GET', url=env('YT_URL'))
youtube_comments = youtube_comments.json()
youtube_commentators = {list(youtube_comments['items'][i].values())[3]['topLevelComment']
                        ['snippet']['authorDisplayName'] for i in range(len(youtube_comments['items']))}

# Получаем множество прокомментировавших в VK
vk_comments = request(method='GET', url=env('VK_URL'))
vk_comments = vk_comments.json()
vk_commentators = \
[[vk_comments['response']['items'][x]['from_id'] for x in range(len(vk_comments['response']['items']))]][0]

# Маппер для связи id с именами пользователей, исключаю себя из списка
VK_USER_MAPPER = env.str('VK_MAPPER_URL') % ','.join(map(str, vk_commentators))
vk_users = request(method='GET', url=VK_USER_MAPPER)
vk_users = vk_users.json()
users = {f"{x['first_name']} {x['last_name']}" for x in vk_users['response'] if x['last_name'] != 'Luchanos'}

# Вывод на экран
all_commentators = users.union(youtube_commentators)
for x in all_commentators:
    print(x)

print('THE WINNER IS:', choice(tuple(all_commentators)))
