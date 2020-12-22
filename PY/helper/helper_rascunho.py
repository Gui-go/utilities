import requests
from bs4 import BeautifulSoup
import datetime

page = requests.get("https://www.aviationtoday.com/2020/12/01/british-army-modernizes-first-apache-ah-64e-helicopter-deliveries/")

# print('URL: ', page.url)
# print('STATUS_CODE: ', page.status_code)  # 200 if everything is ok

soup = BeautifulSoup(page.content, 'html.parser')
# print('Title: ', soup.title.string.strip())  # Title:  Google

soup.find('meta',  property="article:published_time")
soup.find('meta',  property="article:modified_time")


soup.find('div', {'id': 'light-bg'}).find('p', recursive=False).get_text()

soup.find('div', {'id': 'light-bg'}).children.split

soup.xpath

soup.find('div', {'id': 'light-bg'}).find_all('text')

soup.find('div', {'class': 'col-md-12'}, recursive=True).p.strong.find_next_sibling

soup.find('h1', recursive=False).text.strip()

soup.find('div', {'id': 'light-bg'}).findNext('p')
soup.find('div', {'id': 'light-bg'}).p.previous_element
soup.find('div', {'id': 'light-bg'}).next_element
soup.find('div', {'id': 'light-bg'}).find_previous_sibling('p')
soup.find('div', {'id': 'light-bg'}).p.find_next_sibling('p')


dd = soup.find('div', {'class': 'author-date'}).text.strip()[:13].strip()
datetime.datetime.strptime(dd, '%b. %d, %Y').strftime('%m/%d/%Y')
soup.find('div', {'class': 'author-date'}).text.strip()[:13].strip()

soup.find('div', {'class': 'post-body'}).find_all('p')

len(soup.find_all('a'))
print('---------------------------------------')
link = soup.find_all('a')

[link.get('href') for link in soup.find_all('a')]


art = soup.find('article')
art.find('h1').text.strip()
date = art.find('time').get('datetime')[:10]
art.find('img').get('src')

datetime.datetime.strptime(date, '%Y-%b-%d').strftime('%m/%d/%Y')
datetime.datetime.strptime(date, '%Y%b%d').strftime('%m/%d/%Y')
print(date.datetime.strftime("%b %d %Y %H:%M:%S"))
date_object = datetime.strptime(date, '%m/%d/%y')


try :
    soup.find('figure').img.get('src')
except AttributeError:
    soup.find('iframe').get('src')


    try:
        
    except:
        soup.find_all('img')[1].get('src')


dd = soup.find('time').get('datetime')[:10]
date = datetime.datetime.strptime(dd, '%Y-%m-%d').strftime('%m/%d/%Y')

from datetime import datetime
date[:10]
date_time_str = '18/09/19 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print "The type of the date is now",  type(date_time_obj)
print "The date is", date_time_obj



soup.find_all('img')[0]['src']

soup.find_all('img')[0]['data-src']

soup.find('div', {'class': 'content-inner'}).find_all('p')

ss = '//i1.ytimg.com/vi/YZON5gqGHsA/default.jpg'

ss[2:]
ss.startswith('//')
ss = []
if ss.startswith('//'):
    print('ouk') 

div = soup.find('div', {'class': 'postdate byline'})
fg = div.a.text

date = datetime.datetime.strptime(fg, '%b %d, %Y').strftime('%m/%d/%Y')
datetime.strptime(figure.strftime('%Y%m%d'), '%Y%m%d')
datetime.datetime(2009, 12, 20)


upd = div.find('div', {'id': 'update'})
list(upd)[1].text
lst1 = list()

for i in upd:
    lst1.append(i)

lst1[1].text
# ss1 = upd.text


div.find_all('img')[0]['data-src']
img.a.text
img.find('img')['src']
img['src']

img = soup.find('figure', {'class': 'figure-image'}).span.img['data-srcset'].split(' ')[0]
len(img)
figure = soup.find('time')['datetime']
figure.span.img['data-src']

date = datetime.datetime.strptime(soup.find('time')['datetime'], '%Y-%m-%d').strftime('%m/%d/%Y')
soup.find('time')['datetime']

date = datetime.datetime.strptime(figure, '%Y-%b-%d').strftime('%m/%d/%Y')
datetime.strptime(figure.strftime('%Y%m%d'), '%Y%m%d')
datetime.datetime(2009, 12, 20)

div.text.strip()[0:10]
date = datetime.datetime.strptime(div.text.strip()[0:10], '%b %d, %y').strftime('%m/%d/%Y')
div.img['src']
div.find_all('p')

soup.find('span', {'class': 'article-content'}).find_all('p')

soup.find('div', {'class': 'image'}).img['src']

for i in soup.find_all('a'):
    print(i['href'])

title = soup.find('h1', {'class' : 'entry-title'})
print(title.get_text())
time = soup.find('time')['datetime']
print(time)
img = soup.find('div', {'class' : 'featured-img'}).img.get('src')
print(img)
# p = soup.find('div', {'class' : 'entry-main-content'})
# print(p.text.strip())



