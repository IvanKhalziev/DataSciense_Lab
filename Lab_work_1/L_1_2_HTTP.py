# ------------------  HTTP in python: GET, POST, PUT, DELETE ----------------------------
'''

Приклад
https://dev.to/ayabouchiha/sending-get-post-put-delete-requests-in-python-45o8

Навчальний посібник із методів HTTP Python
https://www.pylenin.com/blogs/python-http-methods-tutorial/

Аналіз url: 'https://jsonplaceholder.typicode.com/posts/1'
https://check-host.net/ip-info?host=jsonplaceholder.typicode.com

'''


import pandas as pd
import re
from bs4 import BeautifulSoup
import requests
import json


def GET_test (url: str) -> None:

    '''

    Надсилання запитів GET на сервер з url
    GET : це запит, який використовується для отримання даних або інформації з вказаного сервера.

    :param url: http адреса серверу
    :return:    аж нічого

    '''

    response = requests.get(url)        # ініціалізація доступу до серверу
    print(response.status_code)         # перевірка успішності доступу до серверу, успішна відповідь для get 200
    print(response.text)                # відображення вмісту сторінки за url
    print('url_GET', response.url)     # url

    return


def POST_test (url: str) -> None:

    '''

    Надсилання запитів POST на сервер з url
    POST : це запит, який використовується для надсилання інформації або даних на певний сервер.

    :param url: http адреса серверу
    :return:    аж нічого

    '''

    # інформаціі, що надається до серверу
    data = {'title': 'тестування_POST_для_консультації_5', 'ОК': '_тестування_POST_успішне', 'userId': 5, }
    headers = {'content-type': 'application/json; charset=UTF-8'}

    response = requests.post(url, data=json.dumps(data), headers=headers)  # ініціалізація надfння інформаціі до серверу
    print(response.status_code)            # перевірка успішності доступу до серверу, успішна відповідь для post 201
    print(response.text)                   # відображення вмісту сторінки за url
    print('url_POST', response.url)        # url

    return


def PUT_test (url: str) -> None:

    '''

    Надсилання запитів PUT на сервер з url
    PUT : це запит, який використовується для створення або оновлення ресурсу на певному сервері.

    :param url: http адреса серверу
    :return:    аж нічого

    '''

    # інформаціі, що надається до серверу
    data = {'id': 1, 'userId': 2, 'title': 'тестування_для_PUT_консультації_5', 'body': 'тестування_PU_успішне'}
    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    # ініціалізація надпння інформаціі до серверу
    response = requests.put(url, data=json.dumps(data), headers=headers)
    print(response.status_code)       # перевірка успішності доступу до серверу, успішна відповідь для post 200
    print(response.text)              # відображення вмісту сторінки за url
    print('url_PUT', response.url)    # url

    return


def DELETE_test (url: str) -> None:
    '''

    Надсилання запитів DELETE на сервер з url
    DELETE : це запит, який використовується для видалення певного ресурсу на сервері.

    :param url: http адреса серверу
    :return:    аж нічого

    '''

    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    # ініціалізація ljcnege до серверу
    response = requests.delete(url, headers=headers)
    print(response.status_code)   # перевірка успішності доступу до серверу, успішна відповідь для post 200
    print('url_DELETE', response.url)  # url

    return


#---------------- Парсер САЙТУ для отримання числових даних в dataframe pandas ----------------
def Parsing_Site_coronavirus(url_DS):
    html_source = requests.get(url_DS).text
    html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
    dataframe=pd.read_html(html_source)
    print(dataframe)
    return dataframe

# ---------- Парсер_1 САЙТУ для отримання html структури і вилучення з неї стрічки новин  --------
def Parser_URL_rdk (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')        # аналіз структури html документу
    print(soup)
    quotes = soup.find_all('div', class_='newsline')   # вилучення із html документу ленти новин

    with open('test_1.txt', "w", encoding="utf-8") as output_file:
        print('----------------------- Лента новин', url, '---------------------------------')
        for quote in quotes:
            print(quote.text)
            output_file.write(quote.text)  # запис ленти новин до текстового файлу
        print('------------------------------------------------------------------------------')

    return

# ---------- Парсер_2 САЙТУ для отримання html структури і вилучення з неї стрічки новин  --------
def Parser_URL_pressorg24 (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')        # аналіз структури html документу
    print(soup)
    quotes = soup.find_all('div', class_='event')   # вілучення із html документу ленти новин

    with open('test_2.txt', "w", encoding="utf-8") as output_file:
        print('----------------------- Лента новин', url, '---------------------------------')
        for quote in quotes:
            print(quote.text)
            output_file.write(quote.text)  # запис ленти новин до текстового файлу
        print('------------------------------------------------------------------------------')

    return

'''

ДОВІДКОВО:
Відповіді HTTP-сервера
200: запит виконано успішно.
400: запит не сформовано належним чином.
401: несанкціонований запит, клієнт повинен надіслати дані автентифікації.
404: вказаний у запиті ресурс не знайдено.
500: внутрішня помилка сервера HTTP.
501: запит не реалізований сервером HTTP.
502: служба не доступна.

'''


if __name__ == '__main__':

    print('Оберіть напрям досліджень:')
    print('1 - Методи GET, POST, PUT, DELETE')
    print('2 - Парсинг сайту новин https://www.rbc.ua/rus/news')
    print('3 - Парсинг сайту новин http://pressorg24.com/news')
    print('4 - Парсинг табличних даних https://www.worldometers.info/coronavirus/')
    mode = int(input('mode:'))


    if (mode == 1):
        # ----------------- ПРИКЛАД виклику методів: GET, POST, PUT, DELETE -----------------
        print('Обрано: Методи GET, POST, PUT, DELETE')
        # url = 'https://www.rbc.ua/rus/news'
        url = 'https://jsonplaceholder.typicode.com/posts/1'
        print('-----------------------------------------------------------------------------')
        GET_test(url)   # отримання інформації з сервера.
        print('-----------------------------------------------------------------------------')
        POST_test(url)  # надсилання інформації на сервер
        print('-----------------------------------------------------------------------------')
        PUT_test(url)   # спроба створення або оновлення ресурсу на певному сервері
        print('-----------------------------------------------------------------------------')
        DELETE_test(url) # спроба видалити інформацію на сервері


    if (mode == 2):
        # ----------------- ПРИКЛАД парсингу_1 сайтів новин метод: GET -------------------------
        print('Обрано: Парсинг сайту новин https://www.rbc.ua/rus/news')
        print('Джерело: https://www.rbc.ua/rus/news')
        url = 'https://www.rbc.ua/rus/news'
        Parser_URL_rdk(url)


    if (mode == 3):
        # ----------------- ПРИКЛАД парсингу_2 сайтів новин метод: GET -------------------------
        print('Обрано: Парсинг сайту новин http://pressorg24.com/news')
        print('Обрано інформаційне джерело: http://pressorg24.com/news')
        url = 'http://pressorg24.com/news'
        Parser_URL_pressorg24(url)

    if (mode == 4):
        print('Обрано: Парсинг табличних даних https://www.worldometers.info/coronavirus/')
        url_DS = "https://www.worldometers.info/coronavirus/"
        Parsing_Site_coronavirus(url_DS)

