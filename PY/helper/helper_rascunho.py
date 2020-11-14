import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.wearethemighty.com/mighty-trending/habits-veterans-break-immediately/")

print('URL: ', page.url)
print('STATUS_CODE: ', page.status_code)  # 200 if everything is ok

soup = BeautifulSoup(page.content, 'html.parser')
print('Title: ', soup.title.string)  # Title:  Google

title = soup.find('h1', {'class' : 'entry-title'})
print(title.get_text())
time = soup.find('time')['datetime']
print(time)
img = soup.find('div', {'class' : 'featured-img'}).img.get('src')
print(img)
# p = soup.find('div', {'class' : 'entry-main-content'})
# print(p.text.strip())



