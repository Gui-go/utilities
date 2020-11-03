from selenium.webdriver import Firefox
from selenium import webdriver
from time import sleep
import pandas as pd

url="https://www.vivareal.com.br/venda/santa-catarina/florianopolis/bairros/pantanal/#onde=BR-Santa_Catarina-NULL-Florianopolis-Barrios-Pantanal"

browser = Firefox()

browser.get(url)

sleep(2)

# Elements location
addresses = browser.find_elements_by_class_name("property-card__address")
titulo = browser.find_elements_by_class_name("property-card__title")
price = browser.find_elements_by_class_name("property-card__price")
area = browser.find_elements_by_class_name("property-card__detail-area")
quartos = browser.find_elements_by_class_name("property-card__detail-room")
suites = browser.find_elements_by_class_name("property-card__detail-item-extra")
banheiros = browser.find_elements_by_class_name("property-card__detail-bathroom")
garagem = browser.find_elements_by_class_name("property-card__detail-garage")
amenities = browser.find_elements_by_class_name("property-card__amenities")


# Get them all
listaEnderecos = []
for index, item in enumerate(addresses):
    listaEnderecos.append(item.text)

listaTitulo = []
for index, item in enumerate(titulo):
    listaTitulo.append(item.text)

listaPrice = []
for index, item in enumerate(price):
    listaPrice.append(item.text)

listaArea = []
for index, item in enumerate(area):
    listaArea.append(item.text)

listaQuartos = []
for index, item in enumerate(quartos):
    listaQuartos.append(item.text)

listaSuites = []
for index, item in enumerate(suites):
    listaSuites.append(item.text)

listaBanheiros = []
for index, item in enumerate(banheiros):
    listaBanheiros.append(item.text)

listaGaragem = []
for index, item in enumerate(garagem):
    listaGaragem.append(item.text)

listaAmenities = []
for index, item in enumerate(amenities):
    listaAmenities.append(item.text)

# Put it all in a DF


data = {
    "address": listaEnderecos,
    "title": listaTitulo,
    "price": listaPrice,
    # "area": listaArea,
    "bedrooms": listaQuartos,
    # "suites": listaSuites,
    "Bathrooms": listaBanheiros,
    "garage": listaGaragem#,
    # "amenities": listaAmenities
}

df = pd.DataFrame(data)

print(df)


# print("address"+ len(listaEnderecos)) #36
# print("title"+ len(listaTitulo)) #36
# print("price"+ len(listaPrice)) #36
# print("area"+ len(listaArea)) #72
# print("bedrooms"+ len(listaQuartos)) #36
# print("suites"+ len(listaSuites)) #33
# print("Bathrooms"+ len(listaBanheiros)) #36
# print("garage"+ len(listaGaragem)) #36
# print("amenities"+ len(listaAmenities)) # 28

# print(len(listaAmenities))
# print(listaAmenities)


sleep(1)

browser.quit()


