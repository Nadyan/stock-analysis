import pandas as pd

from dados.get_data import get_dados

siglas = ['MGLU3.SA', 'PETR4.SA', 'STOC31.SA', 'CASH3.SA', 'WEGE3.SA']

dados = get_dados(siglas)
print(dados)
