from flask import Flask
from flask_restful import Resource, Api
from flask import jsonify
import requests
import pandas as pd
import re
import pprint
import json

app = Flask(__name__)

api = Api(app)

class tspopname(Resource):
    
    df_init = pd.DataFrame(columns = ['nome', 'localidade', 'ate1930', 'd1930a1940', 'd1940a1950', 'd1950a1960', 'd1960a1970', 'd1970a1980', 'd1980a1990', 'd1990a2000', 'd2000a2010'])

    def get(self, nome):
        #nome="Guilherme"
        name = nome.split(",")
        
        df_init = pd.DataFrame(columns = ['nome', 'localidade', 'ate1930', 'd1930a1940', 'd1940a1950', 'd1950a1960', 'd1960a1970', 'd1970a1980', 'd1980a1990', 'd1990a2000', 'd2000a2010'])
        
        for i, v in enumerate(name):
            print(v)
            #url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/julia"
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
            df_init = df_init.append(df, ignore_index=True).dropna()
            print(df_init.to_json())
            jj = df_init.to_json()
            
        return jsonify(jj)

api.add_resource(tspopname, '/<nome>')

if __name__ == '__main__':
    app.run(debug=True)

