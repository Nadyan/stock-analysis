import random

def gera_aleatorios(qtd):
    # gera uma lista aleatoria de 0 e 1
    evals = []
    for i in range(qtd):
        evals.append(random.randint(0, 1))
    return evals