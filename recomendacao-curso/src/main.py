import pandas as pd
import random
usuarios_dataset = pd.read_csv('../resources/datasets/users.csv')
classificacoes_dataset = pd.read_csv('../resources/datasets/ratings.csv')

students = usuarios_dataset['UserID'].unique().tolist()
courses = classificacoes_dataset['Item'].unique().tolist()

TAMANHO_POPULACAO = 10
QT_GERACOES = 50
TAXA_MUTACAO = 0.1 #TODO esses valores podem ser alterados para serem recebidos dinamicamente na execucao

def gerar_populacao():
    return [(random.choice(students), random.choice(courses)) for _ in range(TAMANHO_POPULACAO)]

def exec_process():
    populacao = gerar_populacao()

    #TODO implementar
    best_recommendation = []
    return best_recommendation

melhor_recomendacao = exec_process()
print(f"melhor recomendação: Estudante: {melhor_recomendacao[0]} -> curso: {melhor_recomendacao[1]}")
