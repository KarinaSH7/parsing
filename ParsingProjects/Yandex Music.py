import requests
import json

# Задаем параметры запроса
params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.23800355071570123',
}

# Отправляем GET-запрос на API и получаем данные в формате JSON
response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params)
chart_data = response.json()['chartPositions']

# Создаем список для хранения данных
chart_list = []

# Проходимся по данным и извлекаем нужную информацию
for track in chart_data:
    position = track['track']['chart']['position']
    title = track['track']['title']
    artist = track['track']['artists'][0]['name']

    # Добавляем данные в список
    chart_list.append({
        'position': position,
        'artist': artist,
        'title': title
    })

# Сохраняем данные в файле chart_data.json
with open('chart_data.json', 'w', encoding='utf-8') as f:
    json.dump(chart_list, f, ensure_ascii=False, indent=4)

