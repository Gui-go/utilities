from selenium.webdriver import Firefox
from selenium import webdriver
from time import sleep
import pandas as pd

url = "https://www.youtube.com/c/JornaldaRecord/videos"

browser = Firefox()
browser.get(url)

sleep(2)

for i in range(3):  # How much down south?
    browser.execute_script(f"window.scrollTo(0,{i*5000})")
    sleep(1)

sleep(2)

tituloVideos = browser.find_elements_by_id("video-title")

listaVideos = []
for index, item in enumerate(tituloVideos):
    listaVideos.append(item.text)

df = pd.DataFrame(listaVideos, columns=['titulo_videos'])
print(df)
df.to_csv(r'noticias.csv')

sleep(1)

browser.quit()

