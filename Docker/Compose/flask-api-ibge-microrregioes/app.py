from flask import Flask, render_template
import requests
import json
import pandas as pd

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    return 'Olá, Mundo!'


@app.route('/micro/<uf>')
def get_local(uf):
    # uf = 42
    res = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        df = pd.json_normalize(json.loads(res.text))
        df = df.rename(columns={
            'municipio.id' : 'cd_mun', 
            'municipio.nome' : 'nm_mun', 
            'municipio.microrregiao.id' : 'cd_micro', 
            'municipio.microrregiao.nome' : 'nm_micro', 
            'municipio.microrregiao.mesorregiao.id' : 'cd_meso',
            'municipio.microrregiao.mesorregiao.nome' : 'nm_meso',
            'municipio.microrregiao.mesorregiao.UF.sigla' : 'uf',
            'municipio.microrregiao.mesorregiao.UF.nome' : 'estado',
            'municipio.microrregiao.mesorregiao.UF.regiao.nome' : 'rg'})
        df = df[['cd_mun', 'nm_mun', 'cd_micro', 'nm_micro', 'cd_meso', 'nm_meso', 'uf', 'estado', 'rg']]
        df = df.drop_duplicates()
        micror = df.nm_micro.unique()
        estado = str(df.estado.unique()[0])
    else:
        print('Deu ruim no request  :/')

    return render_template('index.html', title=estado, members=micror)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
