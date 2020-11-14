'''
Scrap do VR
'''

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url='https://www.vivareal.com.br/venda/santa-catarina/florianopolis/bairros/balneario/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQiAnb79BRDgARIsAOVbhRr7_V62E2ACSy6sU0W5Wb7oR1APg6FvigB9xsdYCNGiG0V-46MiwawaAtecEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F&__vt=lnv:c'

browser = Firefox()

browser.get(url)

sleep(2)

html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

lista1 = list()
for i in soup.find_all('div', {'data-type' : 'property'}):
    # print('vivareal.com.br'+i.div.article.div.div.a['href'])
    print()
    lista1.append([
        'vivareal.com'+i.find('a')['href'],
        i.find('span', {'class' : 'property-card__address'}).string,
        i.find('h2', {'class' : 'property-card__header'}).text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-area'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip(),
        i.find('div', {'class' : 'property-card__price js-property-card-prices js-property-card__price-small'}).text.strip().split(' ')[1].replace('.', '')
    ])
print(pd.DataFrame(lista1, columns=['url', 'address', 'title', 'area', 'rooms', 'bathrooms', 'garages', 'price']))

nextpage = browser.find_elements_by_class_name('js-change-page')
nextpage[-1].send_keys(Keys.RETURN)

sleep(2)

# ______________________________________________________________________________

html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

lista2 = list()
for i in soup.find_all('div', {'data-type' : 'property'}):
    # print('vivareal.com.br'+i.div.article.div.div.a['href'])
    print()
    lista2.append([
        'vivareal.com'+i.find('a')['href'],
        i.find('span', {'class' : 'property-card__address'}).string,
        i.find('h2', {'class' : 'property-card__header'}).text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-area'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip(),
        i.find('li', {'class' : 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip(),
        i.find('div', {'class' : 'property-card__price js-property-card-prices js-property-card__price-small'}).text.strip().split(' ')[1].replace('.', '')
    ])
print(pd.DataFrame(lista2, columns=['url', 'address', 'title', 'area', 'rooms', 'bathrooms', 'garages', 'price']))

nextpage = browser.find_elements_by_class_name('js-change-page')
nextpage[-1].send_keys(Keys.RETURN)



sleep(2)

# ______________________________________________________________________________


sleep(1)

browser.quit()

