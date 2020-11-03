import requests
import pandas as pd
from bs4 import BeautifulSoup


r = requests.get('https://pt.wikipedia.org/wiki/Lista_de_capitais_nacionais_por_popula%C3%A7%C3%A3o')
print('Crawling...')

print('URL: ', r.url)
print('ENCODING: ', r.encoding)
print('STATUS_CODE: ', r.status_code)

soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[1]
rows = table.find_all('tr')
row_list = list()

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)


df_bs = pd.DataFrame(row_list,columns=['position', 'country', 'city', 'pop', 'ref'])
df_bs.set_index('country',inplace=True)
print(df_bs.iloc[1:, :-1])
# df_bs.to_csv('beautifulsoup.csv')

