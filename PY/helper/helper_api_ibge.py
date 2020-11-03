import requests
import pandas as pd
import pprint
import re
import numpy as np
import matplotlib as plt


url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
data = requests.get(url).json()
#pprint.pprint(data)
df = pd.json_normalize(data)
#type(df)
#df.info()
#df.shape
df2 = df.rename(
    columns={
        "municipio.id": "cd_muni",
        "municipio.nome": "nm_muni",
        "municipio.microrregiao.id": "cd_micro",
        "municipio.microrregiao.nome": "nm_micro",
        "municipio.microrregiao.mesorregiao.id": "cd_meso",
        "municipio.microrregiao.mesorregiao.nome": "nm_meso",
        "municipio.microrregiao.mesorregiao.UF.id": "cd_uf",
        "municipio.microrregiao.mesorregiao.UF.nome": "nm_uf",
        "municipio.microrregiao.mesorregiao.UF.sigla": "sg_uf",
        "municipio.microrregiao.mesorregiao.UF.regiao.id": "cd_rg",
        "municipio.microrregiao.mesorregiao.UF.regiao.nome": "nm_rg",
        "municipio.microrregiao.mesorregiao.UF.regiao.sigla": "sg_rg"
    }
)
df3 = df2[df2.cd_uf.isin(["41", "42", "43"])]
del df3["id"]
del df3["nome"]
df4 = df3.drop_duplicates()

#############################################

url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{str(nome[2])}"
print(f"Requesting: {url}")
request = requests.get(url)
data = request.json()


nome="Guilherme,Julia"
name=nome.split(",")
fgo = dc = pd.DataFrame(columns = ['nome', 'localidade', 'ate1930', 'd1930a1940', 'd1940a1950', 'd1950a1960', 'd1960a1970', 'd1970a1980', 'd1980a1990', 'd1990a2000', 'd2000a2010'])

for i, v in enumerate(name):
    print(v)
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{str(v)}"
    print(f"Requesting: {url}")
    request = requests.get(url)
    data = request.json()
    dc = dict()
    dc["nome"] = re.search(r"'nome': '(.*?)', 'sexo'", str(data))[1]
    dc["localidade"] = re.search(r"'localidade': '(.*?)', 'res'", str(data))[1]
    dc["ate1930"] = re.search(r"'1930\[', 'frequencia': (.*?)}, {'periodo': '\[1930,1940\['", str(data))[1]
    dc["d1930a1940"] = re.search(r"'\[1930,1940\[', 'frequencia': (.*?)}, {'periodo': '\[1940,1950\['", str(data))[1]
    dc["d1940a1950"] = re.search(r"'\[1940,1950\[', 'frequencia': (.*?)}, {'periodo': '\[1950,1960\['", str(data))[1]
    dc["d1950a1960"] = re.search(r"'\[1950,1960\[', 'frequencia': (.*?)}, {'periodo': '\[1960,1970\['", str(data))[1]
    dc["d1960a1970"] = re.search(r"'\[1960,1970\[', 'frequencia': (.*?)}, {'periodo': '\[1970,1980\['", str(data))[1]
    dc["d1970a1980"] = re.search(r"'\[1970,1980\[', 'frequencia': (.*?)}, {'periodo': '\[1980,1990\['", str(data))[1]
    dc["d1980a1990"] = re.search(r"'\[1980,1990\[', 'frequencia': (.*?)}, {'periodo': '\[1990,2000\['", str(data))[1]
    dc["d1990a2000"] = re.search(r"'\[1990,2000\[', 'frequencia': (.*?)}, {'periodo': '\[2000,2010\['", str(data))[1]
    dc["d2000a2010"] = re.search(r"'\[2000,2010\[', 'frequencia': (.*?)}\]}\]", str(data))[1]
    df = pd.json_normalize(dc)
    fgo = fgo.append(df, ignore_index=True).dropna()
    

