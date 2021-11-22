from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from dados.get_data import get_dados

def modelo_svc(x, y):
    SEED = 123456

    x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.25, random_state=SEED, stratify=y)

    modelo = SVC(random_state = SEED)
    modelo.fit(x_treino, y_treino)

    previsoes = modelo.predict(x_teste)

    acuracia = accuracy_score(y_teste, previsoes)

    #print(y_teste, previsoes)
    #print('Acurácia de teste SVC: %.2f%%' % (acuracia*100))

    return modelo


def previsao_svc(modelo, siglas):
    
    dados = get_dados(siglas)
    prev = modelo.predict(dados)
    print(prev)
    
    #for idx, sigla in enumerate(siglas):
        #print("Prev ação %s: %d" % (sigla, idx))
