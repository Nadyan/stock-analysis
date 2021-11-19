import yfinance as yf
import datetime
import pandas as pd

def get_dados(siglas, num_dias = 588, intervalo = '1wk', inicio = '',  fim = ''):

    """
        siglas -> []
        
        Retorna uma lista de DataFrames 
        com os valores de fechamento das siglas passadas
    """

    if inicio == '':
        inicio = (datetime.date.today() - datetime.timedelta(num_dias))
    if fim == '':
        fim = datetime.date.today()

    dados = []
    for sigla in siglas:
        df = yf.download(sigla, start = inicio, end = fim, interval = intervalo)
        
        df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis = 1, inplace = True)
        df = df.transpose()
        df.dropna(axis = 1, inplace = True)
        df.index = [sigla]

        dados.append(df)
    
    return dados
