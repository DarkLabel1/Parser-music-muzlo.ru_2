import requests
from bs4 import BeautifulSoup as bs

URL = [
    'http://muzl0.ru/mp3/2018/',
    'http://muzl0.ru/mp3/2019/',
    'http://muzl0.ru/mp3/%D0%9C%D1%83%D0%B7%D1%8B%D0%BA%D0%B0%20%D0%B2%20%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D1%83%202018/',
    'http://muzl0.ru/mp3/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80%D1%8D%D0%BF%202018/',
    'http://muzl0.ru/mp3/%D0%A8%D0%B0%D0%BD%D1%81%D0%BE%D0%BD/'
]

for i in URL:
    response = requests.get(i)
    soup = bs(response.content, 'html.parser')
    divs = soup.find_all('li', attrs={'class': 'track'})
    for div in divs:
        href = div['data-mp3']
        nazvanie = href.split('/')
        r = requests.get('http://muzl0.ru' + href)
        with open('Music/' + nazvanie[4], 'wb') as w:
            w.write(r.content)
        print('Записано: ' + nazvanie[4])