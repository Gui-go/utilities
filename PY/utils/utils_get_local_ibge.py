#!/usr/bin/env python3

"""
Python function to get geospatial information about Brazilian states
"""

import requests
import json
import pandas as pd
import janitor


def get_loc(ufs: list) -> pd.DataFrame:
    """
    This function gets spatial information from IBGE's API and return it as a pandas DataFrame.
    INPUT:
        ufs -> list (list with the ufs of interest)
    Output:
        df -> pd.DataFrame
    """

    if ufs == ["all"]:
        ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO", "DF"]
        
    ufsj = "|".join(ufs)

    try:
        response = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{ufsj}/municipios")
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

    df = pd.json_normalize(json.loads(response.text)).clean_names()
    df = df.rename(columns={
        'id':'cd_mun',
        'nome':'nm_mun',
        'microrregiao_id':'cd_micro',
        'microrregiao_nome':'nm_micro',
        'microrregiao_mesorregiao_id':'cd_meso',
        'microrregiao_mesorregiao_nome':'nm_meso',
        'regiao_imediata_id':'cd_rgime',
        'regiao_imediata_nome':'nm_rgime',
        'regiao_imediata_regiao_intermediaria_id':'cd_rgint',
        'regiao_imediata_regiao_intermediaria_nome':'nm_rgint',
        'regiao_imediata_regiao_intermediaria_uf_id':'cd_uf',
        'regiao_imediata_regiao_intermediaria_uf_sigla':'sg_uf',
        'regiao_imediata_regiao_intermediaria_uf_nome':'nm_uf',
        'regiao_imediata_regiao_intermediaria_uf_regiao_id':'cd_rg',
        'regiao_imediata_regiao_intermediaria_uf_regiao_sigla':'sg_rg',
        'regiao_imediata_regiao_intermediaria_uf_regiao_nome':'nm_rg'
    })
    df = df[['cd_mun', 'nm_mun', 'cd_micro', 'nm_micro', 'cd_meso', 'nm_meso', 'cd_rgime', 'nm_rgime', 'cd_rgint', 'nm_rgint', 'cd_uf', 'sg_uf', 'nm_uf', 'cd_rg', 'sg_rg', 'nm_rg']]

    return df


# local = get_loc(["all"])

