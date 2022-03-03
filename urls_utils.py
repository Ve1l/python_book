import requests

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url #использовать "yield", чтобы вернуть циклу "for" результат каждого отдельного запроса GET. Не использовать "return" иначе функция завершится, потому что функция ожидает получить кортеж при какждом вызове.
        
urls = ('http://talkpython.fm', 'http://pythonpodcast.com', 'http://python.org')

for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)