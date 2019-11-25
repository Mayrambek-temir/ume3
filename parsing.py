import requests
from bs4 import BeautifulSoup
from pprint import pprint
url = 'http://kenesh.kg/ru/deputy/list/35'
def get_html(url):
    r = requests.get(url)
    # print(r)
    pprint(r.text)
    return r.text
links=[]
def get_urls(html):
    soup = BeautifulSoup(html, 'html.parser')
    # td выташили
    tds=soup.find('table', class_='table').find_all('td')
    links = []
    for td in tds:
        a = td.find('a').get('href')
        link = 'http://kenesh.kg' + a
        pprint(link)
        links.append(link)
    # print(soup)
    pprint(tds)
get_urls(get_html(url))
