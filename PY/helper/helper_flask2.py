from flask import Flask
from flask_restful import Resource, Api
import requests
import pandas as pd
import re

app = Flask(__name__)

api = Api(app)

class tspopname(Resource):

    def get(self, name):
        url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{str(name)}"
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
        
        return dc

api.add_resource(tspopname, '/<name>')

if __name__ == '__main__':
    app.run(debug=True)
