"""
Изучите API сервиса https://rickandmortyapi.com/
Получите имя, родную планету и список эпизодов всех персонажах начиная с вашего номера в журнале и заканчивая ваш номер*5
Сохраните в .json файл.
"""

import requests
import json

# номер первого персонажа
start = 13
# номер последнего персонажа (включительно)
end = 65

# список для хранения данных о персонажах
characters = []

# проходимся в цикле по персонажам
for i in range(start, end + 1):
    # отправляем GET запрос к API сервиса и получаем информацию о персонаже
    response = requests.get(f'https://rickandmortyapi.com/api/character/{i}').json()

    # получаем необходимые данные из ответа и добавляем их в список персонажей
    name = response['name']
    planet = response['origin']['name']
    episodes = [episode.split('/')[-1] for episode in response['episode']]
    character = {'name': name, 'planet': planet, 'episodes': episodes}
    characters.append(character)

# сохраняем список персонажей в файл
with open('characters.json', 'w') as f:
    json.dump(characters, f, indent=4)