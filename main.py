import pandas as pd

from dados.get_data import get_dados
from modelo.svc import modelo_svc, previsao_svc
from dados.utils import gera_aleatorios

siglas = [
            'MGLU3.SA', 
            'PETR4.SA', 
            #'STOC31.SA', 
            #'CASH3.SA', 
            'WEGE3.SA', 
            'VIIA3.SA', 
            'MULT3.SA', 
            'CYRE3.SA', 
            'YDUQ3.SA', 
            'LREN3.SA', 
            'TOTS3.SA', 
            'FLRY3.SA'
        ]

dados = get_dados(siglas)
dados['eval'] = gera_aleatorios(len(dados))

x = dados.drop(['eval'], axis = 1)
y = dados['eval']

modeloSVC = modelo_svc(x, y)
siglas_teste = ['MGLU3.SA', 'FLRY3.SA']
previsao_svc(modeloSVC, siglas_teste)
