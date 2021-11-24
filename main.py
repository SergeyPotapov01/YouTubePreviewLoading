import io

import requests
from PIL import Image


def save_preview(url: str, i: str):
    im = requests.get(f'https://i.ytimg.com/vi_webp/{url}/maxresdefault.webp').content
    im = Image.open(io.BytesIO(im)).convert('RGB')
    im.save(f'{i}.jpg', 'jpeg')

if __name__ == '__main__':
    for i in range(100):
        save_preview(input('Введи ссыль на видос: '), str(i))