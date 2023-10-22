"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests
from PIL import Image

def save_random_cat_image():
    response = requests.get('https://cataas.com/cat')
    with open('random_cat.jpg', 'wb') as f:
        f.write(response.content)

def save_original_size_image():
    response = requests.get('https://cataas.com/cat')
    image = Image.open(BytesIO(response.content))
    image.save('original_size_cat.jpg')


def save_pixelated_image():
    response = requests.get('https://cataas.com/cat')
    image = Image.open(BytesIO(response.content))
    pixelated_image = image.resize((100, 100), resample=Image.BOX)
    pixelated_image.save('pixelated_cat.jpg')

save_random_cat_image()
save_random_cat_image()
save_original_size_image()
save_original_size_image()
save_pixelated_image()
save_pixelated_image()