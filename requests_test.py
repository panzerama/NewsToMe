

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


def multiple_requests():
    sites = ['http://www.slate.com', 'http://www.npr.org', 'http://www.politico.com', 'http://www.nytimes.com',
             'http://www.huffingtonpost.com', 'http://www.cnn.com', 'http://www.usatoday.com',
             'http://www.yahoo.com/news/', 'http://www.wsj.com', 'http://www.breitbart.com/big-government/',
             'http://www.drudgereport.com', 'http://www.foxnews.com', 'http://www.theblaze.com', 'https://apnews.com/',
             'http://www.bbc.com']



    for site in sites:
        response = requests.get(site)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.text
        links = soup.find_all('a')
        with open('{}.txt'.format(title), encoding='utf-8', mode='a') as f:
            for link in links:
                if link.get('href'):
                    f.write(link.get('href') + '\n')

multiple_requests()
