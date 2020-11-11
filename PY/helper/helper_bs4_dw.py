'''
Crawling and Scraper Class for the Deutsche Welle News website
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup


class DW:
    def __init__(self):
        self.url = 'https://www.dw.com/'
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        print(f'Requesting for {self.page.url}')
        if self.page.status_code == 200:
            print('Código 200, deu boa.')
        else:
            print(f'hmmmm, código {self.page.status_code}, deu ruim')

    def pega_link(self):
        tags = self.soup.find_all('a')
        linkes_list = list()
        for t in tags:
            linkes_list.append(t.get('href', []))
        self.linkes_list = linkes_list
    
    def filter_linkes(self):
        # self.filtered_list = self.linkes_list
        self.filtered_list = [url for url in self.linkes_list if 'en' in url]
        items_to_remove = ['twitter.', 'facebook.', 'linkedin.', 'youtube.', '/contact', 
        'about-dw', 'about-us', 'm.dw', '/training', '/podcasts', '/tv', '/top-stories',
        '/zh', 'de', '#', '/deutsch-lernen', '/radio', 'learn-german',
        '/live-tv', '/media-center', '/service']
        for remove_item in items_to_remove:
            self.filtered_list = [
                url for url in self.filtered_list if remove_item not in url]
        self.filtered_list = self.filtered_list[:6]
    
    def scrap(self):
        self.scrap_list = list()
        for url in self.filtered_list:
            page = requests.get(f'https://www.dw.com{url}')
            # print(f'Scrapiando {page.url}')  # transforma em log
            # print(f'Código {page.status_code}')
            soup = BeautifulSoup(page.content, 'html.parser')
            ul_smallList = soup.find('ul', {'class':'smallList'})
            div_innerFrame = soup.find('div', {'id':'innerFrame'})
            p_intro = div_innerFrame.find('p', {'class':'intro'})
            a_overlayLink = div_innerFrame.find('a', {'class':'overlayLink'})
            self.scrap_list.append([
                page.url,
                ul_smallList.li.text.strip().split('\n')[-1], 
                div_innerFrame.h1.text.strip(),
                p_intro.text.strip(),
                f"https://www.dw.com{a_overlayLink.get('link', ['NA'])}"
            ])
        self.df = pd.DataFrame(self.scrap_list, columns=['url', 'date', 'title', 'intro', 'img'])

    def run(self):
        self.pega_link()
        self.filter_linkes()
        self.scrap()


scrap_dw = DW()
scrap_dw.run()
scrap_dw.df