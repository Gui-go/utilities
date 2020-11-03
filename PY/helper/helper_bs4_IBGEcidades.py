from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

url='https://cidades.ibge.gov.br/'

browser = Firefox()

browser.get(url)

# sleep(3000)
busca = browser.find_elements_by_class_name('busca')
busca.send_keys('Santa Catarina')
print(busca)
# busca.send_keys(Keys.ENTER)
# busca.submit() 

browser.quit()





# r = requests.get("https://cidades.ibge.gov.br")

# print('URL: ', r.url)
# print('ENCODING: ', r.encoding)
# print('STATUS_CODE: ', r.status_code)

# soup = BeautifulSoup(r.content, 'html.parser')
# print('TITLE: ', soup.title.string)




