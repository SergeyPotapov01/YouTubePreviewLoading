import io

import requests
from PIL import Image


def _get_url(url: str):
    if url[0:32] == 'https://www.youtube.com/watch?v=':
        return url[32:43]
    if url[0:24] == 'www.youtube.com/watch?v=':
        return url[24:35]
    if len(url) == 11:
        return url

def save_preview(url: str, i: str):
    url = _get_url(url)
    im = requests.get(f'https://i.ytimg.com/vi_webp/{url}/maxresdefault.webp').content
    im = Image.open(io.BytesIO(im)).convert('RGB')
    im.save(f'img/{i}.jpg', 'jpeg')

if __name__ == '__main__':
    for i in range(256):
        save_preview(input('Введи ссылку на на видео: '), str(i))