import requests
from bs4 import BeautifulSoup
import json
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

result = {}
for i in range(1, 15):
    print('Scraping page '+ str(i))
    sleep(1)

    response = requests.get('https://zaka-zaka.com/game/new/page'+str(i), headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find('div', class_='tabs-content tab-1 active')
    cards = container.find_all('a', class_='game-block')
    for card in cards:
        name = card.find('div', class_='game-block-name').text
        price = card.find('div', class_='game-block-price').text
        if price is not None:
            new_price = ''
            for i in price:
                if i.isdigit():
                    new_price += i
            result[name] = int(new_price)

print(result)

with open('result.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)