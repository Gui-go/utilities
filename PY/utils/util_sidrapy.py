

# Tabela 8188 - Índice e variação da receita nominal e do volume de vendas no comércio varejista ampliado, por atividades (2014 = 100) - Chamada de API
# https://apisidra.ibge.gov.br/values/t/8188/n1/all/v/11706/p/all/c11046/all/c85/2759,2762,90671,90672,90673,103155,103156,103157,103159/d/v11706%205

import pandas as pd
import numpy as np
import sidrapy
import janitor

data = sidrapy.get_table(
    table_code="8188", 
    territorial_level="1", 
    ibge_territorial_code="all", 
    variable="11706", 
    period="all", 
    classification="85/2759,2762,90671,90672,90673,103155,103156,103157,103159"
)
df = data.rename(columns=data.iloc[0]).iloc[1:, ]


data.columns
data.describe()

data.MC.unique()
