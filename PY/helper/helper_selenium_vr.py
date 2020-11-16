'''
Scrap do VR
'''

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import datetime

primeira_pagina='https://www.vivareal.com.br/venda/santa-catarina/florianopolis/bairros/balneario/apartamento_residencial/?utm_source=google&utm_medium=cpc&utm_campaign=Institucional-VivaReal&gclid=Cj0KCQiAnb79BRDgARIsAOVbhRr7_V62E2ACSy6sU0W5Wb7oR1APg6FvigB9xsdYCNGiG0V-46MiwawaAtecEALw_wcB&utm_referrer=https%3A%2F%2Fwww.google.com%2F&__vt=lnv:c'

class VR:
    def __init__(self, primeira_pagina):
        self.primeira_pagina = primeira_pagina
        self.browser = Firefox()
        self.browser.get(primeira_pagina)
        sleep(2)
        self.df = pd.DataFrame()
    
    def scraper(self):
        self.html = self.browser.page_source
        self.soup = BeautifulSoup(self.html, 'html.parser')
        lista = list()
        for i in self.soup.find_all('div', {'data-type' : 'property'}):
            lista.append([
                'vivareal.com'+i.find('a')['href'],
                i.find('span', {'class' : 'property-card__address'}).string,
                i.find('h2', {'class' : 'property-card__header'}).text.strip().split('    ')[0],
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-area'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip(),
                i.find('li', {'class' : 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip(),
                i.find('div', {'class' : 'property-card__price js-property-card-prices js-property-card__price-small'}).text.strip().split(' ')[1].replace('.', '')
            ])
        self.dd = pd.DataFrame(lista, columns=['url', 'address', 'title', 'area', 'rooms', 'bathrooms', 'garages', 'price'])
        self.df = pd.concat([self.df, self.dd], ignore_index=True)

    def next_page(self):
        self.nextpage = self.browser.find_elements_by_class_name('js-change-page')
        self.nextpage[-1].send_keys(Keys.RETURN)
        sleep(2)

    def exit(self):
        sleep(1)
        self.browser.quit()
        print('bye')

    def uniques(self):
        self.uniques = self.df.drop_duplicates()
        print(f'Quantos links? {len(self.df.url)}')
        print(f'Quantos unicos mesmo? {len(self.df.url.drop_duplicates())}')

    def save(self):
        self.df.to_csv(r'bc_imoveis_selenium.csv')
        print('Tá salvo, chefe.')
    
    def adddate(self):
        self.df['date'] = '{:%Y-%m-%d }'.format(datetime.datetime.now())

    def filter(self):
        self.df = self.df[-self.df['price'].isin(['Consulta'])]
        self.df = self.df[-self.df.area.str.contains("-", na=False)]
        print('Filtrado, chefe.')
        
    def run(self, qpages):
        for _ in range(qpages):
            vr.scraper()
            vr.next_page()
        vr.adddate()
        vr.uniques()
        vr.filter()
        vr.save()
        vr.exit()

vr = VR(primeira_pagina)
vr.run(30)



# import datetime

# print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
# print('{:%Y-%m-%d }'.format(datetime.datetime.now()))
# today = datetime.date.today()
# print("Today's date is {:%b, %d %Y}".format(today))

# schedule = '{:%b, %d %Y}'.format(today)

# vr.start()

# for _ in range(6):
#     vr.scraper()
#     vr.next_page()

# vr.uniques()
# vr.save()
# vr.exit()



# a = [['1-2',2,4],[1,3,4],[2,3,4]]
# b = [[1,1,1],[1,6,4],[2,9,4]]
# c = [[1,3,4],[1,1,4],[2,0,4]]
# d = [[1,1,4],[1,3,4],[2,0,4], [2,0,4], [2,0,4]]


# df1 = pd.DataFrame(a,columns=["a","b","c"])
# df2 = pd.DataFrame(b,columns=["a","b","c"])
# df3 = pd.DataFrame(c,columns=["a","b","c"])
# df4 = pd.DataFrame(d,columns=["a","b","c"])
# df4.drop_duplicates()
# df4['a'].drop_duplicates()

# df1[-df1.a.str.contains("-", na=False)]

# df[~df.C.str.contains("XYZ", na=False)]
# unique(df3)

# f.drop(columns=['B', 'C'])


# browser = Firefox()

# browser.get(primeira_pagina)

# sleep(2)

# html = browser.page_source

# soup = BeautifulSoup(html, 'html.parser')

# lista1 = list()
# for i in soup.find_all('div', {'data-type' : 'property'}):
#     # print('vivareal.com.br'+i.div.article.div.div.a['href'])
#     print()
#     lista1.append([
#         'vivareal.com'+i.find('a')['href'],
#         i.find('span', {'class' : 'property-card__address'}).string,
#         i.find('h2', {'class' : 'property-card__header'}).text.strip(),
#         i.find('li', {'class' : 'property-card__detail-item property-card__detail-area'}).span.text.strip(),
#         i.find('li', {'class' : 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).span.text.strip(),
#         i.find('li', {'class' : 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).span.text.strip(),
#         i.find('li', {'class' : 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).span.text.strip(),
#         i.find('div', {'class' : 'property-card__price js-property-card-prices js-property-card__price-small'}).text.strip().split(' ')[1].replace('.', '')
#     ])
# # print(pd.DataFrame(lista1, columns=['url', 'address', 'title', 'area', 'rooms', 'bathrooms', 'garages', 'price']))

# nextpage = browser.find_elements_by_class_name('js-change-page')
# nextpage[-1].send_keys(Keys.RETURN)

# sleep(2)

# sleep(1)

# browser.quit()

