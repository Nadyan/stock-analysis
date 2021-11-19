import pandas as pd
import random

from dados.get_data import get_dados
from modelo.mlp import cria, treina

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

lista = get_dados(siglas)
dados = pd.concat(lista)

evals = []
for i in range(len(dados)):
  evals.append(random.randint(0, 1))
dados['eval'] = evals

modelo = cria(len(dados.columns)-1, 126, 1)

#print('Parametros antes do treino')    
#for name, param in modelo.named_parameters():
    
 #   print(name)
  #  print(param)

modelo = treina(modelo, dados)

#print('Parametros depois do treino')
#for name, param in modelo.named_parameters():
        
        
#        print(name)
#        print(param)
