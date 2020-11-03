import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.google.com/")

print('URL: ', page.url)
# print('ENCODING: ', page.encoding)  # utf-8
print('STATUS_CODE: ', page.status_code)  # 200 if everything is ok
# print('HEADERS: ', page.headers)  # A bunch of useless information
# print('TEXT: ', page.text)
# print('CONTENT: ', page.content)
# print('JSON: ', page.json)  # <bound method Response.json of <Response [200]>>

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup.prettify())
print('Title: ', soup.title.string)  # Title:  Google
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a['href'])
# print(soup.a.get('href'))
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text())



#print(list(soup.children))
#print(len(list(soup.children))) #2
#print([type(item) for item in list(soup.children)]) # [<class 'bs4.element.Doctype'>, <class 'bs4.element.Tag'>]

#html = list(soup.children)[1]
#print(html)
#body = list(html.children)[2]
#print(body.prettify())



