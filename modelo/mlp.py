import pandas as pd
import torch
from torch import nn
from torch import optim

def cria(input_size, hidden_size, output_size):
    rede = nn.Sequential(
                nn.Linear(in_features=input_size, out_features=hidden_size),
                nn.ReLU(),
                nn.Linear(in_features=hidden_size, out_features=output_size),
                nn.Softmax()
            )

    return rede

def treina(modelo, dados, passos = 5):
    criterio = nn.BCELoss()
    otimizador = optim.SGD(modelo.parameters(), lr = 1e-3)
    
    X = dados.drop(['eval'], axis = 1)
    X = torch.tensor(X.values, dtype = torch.float32)

    Y = dados['eval']
    Y = torch.tensor(Y.values, dtype = torch.float32)
    Y = Y.unsqueeze(1)
    
    for i in range(passos):
        # Forward
        pred = modelo(X)
        loss = criterio(pred, Y)

        # Backpropagation
        loss.backward()
        otimizador.step()

        print('Passo: ', i, 'Loss: ', loss)
    
    return modelo
