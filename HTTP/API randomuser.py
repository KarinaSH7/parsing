"""
Изучите API сервиса https://randomuser.me/
Выведите цитату "Hi, im #NAME, im from #COUNTRY, my phone number is #PHONE"
"""
import requests

# отправляем GET запрос к API сервиса и получаем случайного пользователя
response = requests.get('https://randomuser.me/api/').json()
user = response['results'][0]

# получаем необходимые данные из ответа и форматируем строку
name = user['name']['first'] + ' ' + user['name']['last']
country = user['location']['country']
phone = user['phone']
quote = f"Hi, I'm {name}, I'm from {country}, my phone number is {phone}"

print(quote)