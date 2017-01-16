

import requests
from bs4 import BeautifulSoup


def simple_request():
    url = "http://www.npr.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    with open('simple_req.txt', encoding='utf-8', mode='w+') as f:
        f.write(soup.prettify())


def proxy_request():
    california_proxies = ['173.36.245.236:80', '8.37.229.49:8082', '162.243.144.84:80', '74.80.245.73:8000']
    url = "http://www.npr.org"

    response = requests.get(url, california_proxies[0])
    soup = BeautifulSoup(response.text, "html.parser")
    with open('proxy_req.txt', encoding='utf-8', mode='w+') as f:
        f.write(soup.prettify())

simple_request()
proxy_request()
