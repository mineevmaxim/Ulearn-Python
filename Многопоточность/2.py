import threading
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_currencies(url, id, currencies):
    response = requests.get(url)
    if response.status_code == 200:
        secret_code()
        soup = BeautifulSoup(response.text, 'html.parser')
        currency = str(soup.find_all('valute')[id])
        if currency not in currencies:
            currencies.append(currency)


if __name__ == '__main__':
    currencies = []
    id = int(input())

    with ThreadPoolExecutor(max_workers=10) as pool:
        for url in urls:
            future = pool.submit(get_currencies, url, id, currencies)
            future.result()

    currencies_string = ''.join(currencies)
    print(currencies_string)