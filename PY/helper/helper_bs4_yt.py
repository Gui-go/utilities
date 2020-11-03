import requests
import pandas as pd
from bs4 import BeautifulSoup


page = requests.get('https://www.youtube.com/')
print('Crawling...')

print('URL: ', page.url)
print('ENCODING: ', page.encoding)
print('STATUS_CODE: ', page.status_code)
# print('HEADERS: ', page.headers) # A bunch of useless information
# print('TEXT: ', page.text)
# print('CONTENT: ', page.content)
# print('JSON: ', page.json) # <bound method Response.json of <Response [200]>>

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# print(type(soup))
# print(soup.prettify())
# print('Title: ', soup.title) # Title:  <title>YouTube</title>
# print('Title: ', soup.title.name) # Title:  title
print('Title: ', soup.title.string) # Title:  YouTube
# print('Parent name: ', soup.title.parent.name) # Title:  YouTube
# print(soup.a)
# print(soup)
# print(soup.find_all('ytd-rich-item-renderer', {'class_':'style-scope ytd-rich-grid-renderer'}))

# print(soup.a.attrs)
# print(soup.a['href'])
# print(soup.a.get('href'))
# print(soup.a['slot'])
# print(soup.a.get('slot'))
# print(soup.a['style'])
# print(soup.a.get('style'))
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text())



#print(list(soup.children))
#print(len(list(soup.children))) #2
#print([type(item) for item in list(soup.children)]) # [<class 'bs4.element.Doctype'>, <class 'bs4.element.Tag'>]

html = list(soup.children)[1]
#print(html)
body = list(html.children)[2]
#print(body.prettify())



