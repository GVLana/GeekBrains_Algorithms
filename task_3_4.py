"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

from uuid import uuid4
from hashlib import sha512

salt = uuid4().hex
cache = {}

url = input('Enter URL: ')

def hash_web_page(url):
    if cache.get(url):
        print(f'This web-page was already hashed: {url}')
    else:
        res = sha512(salt.encode() + url.encode()).hexdigest()
        cache[url] = res
        print(f'This web-page was hashed {res} and added to the cache.')
    return cache


hash_web_page(url)
hash_web_page(url)

