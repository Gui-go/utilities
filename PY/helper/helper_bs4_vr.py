import requests
import pandas as pd
from bs4 import BeautifulSoup


print('Crawling...')

urls = list()
for i in range(276):
    urls.append(f'https://www.vivareal.com.br/venda/santa-catarina/balneario-camboriu/apartamento_residencial/?pagina={i+1}')


linkses = list()
for url in urls:
    page = requests.get(url)
    print('URL: ', page.url)
    print('STATUS_CODE: ', page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    print('TITLE: ', soup.title.string)
    for h2 in soup.find_all('h2', {'class':'property-card__header'}):
        linkses.append(f'https://www.vivareal.com.br{h2.a.get("href", [])}')


lista = list()
for urles in linkses:  # fazer com enumerate para saber em qual numero ta
    page = requests.get(urles)
    print('Scraping ', page.url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_ac = soup.find('div', {'class':'address-container'})
    li_area = soup.find('li', {'class':'features__item features__item--area js-area'})
    li_bedrooms = soup.find('li', {'class':'features__item features__item--bedroom js-bedrooms'})
    li_bathrooms = soup.find('li', {'class':'features__item features__item--bathroom js-bathrooms'})
    li_parking = soup.find('li', {'class':'features__item features__item--parking js-parking'})
    div_price = soup.find('div', {'class':'price__content-wrapper'})
    lista.append([
        page.url, 
        div_ac.section.div.h1.text.strip(), 
        div_ac.section.div.div.p.text,
        li_area.span.text,
        li_bedrooms.span.text,
        li_bathrooms.span.text,
        li_parking.text,
        div_price.h3.text.strip()
    ])


df = pd.DataFrame(lista, columns=['url', 'title', 'address', 'area', 'bedrooms', 'bathrooms', 'parking', 'price'])


df.to_csv(r'bc_imoveis.csv')



